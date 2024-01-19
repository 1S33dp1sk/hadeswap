

async def deposit_liquidity_single_sell_order(program_id: PublicKey, connection: Client, pair: PublicKey, authority_adapter: PublicKey, user_pubkey: PublicKey, nft_mint: PublicKey, nft_validation_adapter: PublicKey, proof: list, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    funds_sol_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair]
    funds_sol_vault = await PublicKey.find_program_address(funds_sol_vault_seed, program.program_id)
    
    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), pair]
    nfts_owner = await PublicKey.find_program_address(nfts_owner_seed, program.program_id)

    nft_pair_box = Keypair.generate()

    user_nft_token_account = await find_associated_token_address(user_pubkey, nft_mint)
    vault_nft_token_account = await find_associated_token_address(nfts_owner, nft_mint)

    metadata_info = get_metaplex_metadata_pda(nft_mint)
    edition_info = get_metaplex_edition_pda(nft_mint)
    owner_token_record = find_token_record_pda(nft_mint, user_nft_token_account)
    dest_token_record = find_token_record_pda(nft_mint, vault_nft_token_account)

    rule_set = METADATA_PROGRAM_PUBKEY  # Default rule set, modify as needed

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)  # Example, adjust as needed
    instructions.append(modify_compute_units)

    deposit_liquidity_single_sell_order_instruction = program.depositLiquiditySingleSellToPair(proof or [], None).accounts_strict({
        'nftPairBox': nft_pair_box.public_key,
        'nftValidationAdapter': nft_validation_adapter,
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'fundsSolVault': funds_sol_vault,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_info,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'nftsOwner': nfts_owner,
        'nftMint': nft_mint,
        'nftUserTokenAccount': user_nft_token_account,
        'vaultTokenAccount': vault_nft_token_account,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).remaining_accounts([
        {'pubkey': rule_set, 'isSigner': False, 'isWritable': False},
    ]).instruction()

    instructions.append(deposit_liquidity_single_sell_order_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [nft_pair_box]
    await send_txn(transaction, signers)
    return {'nftPairBox': nft_pair_box.public_key, 'instructions': instructions, 'signers': signers}
