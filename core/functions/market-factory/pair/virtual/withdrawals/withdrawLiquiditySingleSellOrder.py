

async def withdraw_liquidity_single_sell_order(program_id: PublicKey, connection: Client, accounts, args, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair'].to_bytes()]
    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]

    sol_funds_vault = await PublicKey.find_program_address(sol_funds_vault_seed, program.program_id)
    nfts_owner = await PublicKey.find_program_address(nfts_owner_seed, program.program_id)
    fee_sol_vault = await PublicKey.find_program_address(fee_sol_vault_seed, program.program_id)

    user_nft_token_account = await find_associated_token_address(accounts['user_pubkey'], accounts['nft_mint'])
    vault_nft_token_account = await find_associated_token_address(nfts_owner, accounts['nft_mint'])

    metadata_info = get_metaplex_metadata_pda(accounts['nft_mint'])
    edition_info = get_metaplex_edition_pda(accounts['nft_mint'])
    owner_token_record = find_token_record_pda(accounts['nft_mint'], vault_nft_token_account)
    dest_token_record = find_token_record_pda(accounts['nft_mint'], user_nft_token_account)
    rule_set = await find_rule_set_pda(args['pnft']['payer_rule_set'], args['pnft']['name_for_rule_set']) if args.get('pnft') else METADATA_PROGRAM_PUBKEY

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)
    instructions.append(modify_compute_units)

    withdraw_instruction = await program.withdraw_liquidity_single_sell_order(None).accounts_strict({
        'nftPairBox': accounts['nft_pair_box'],
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'feeSolVault': fee_sol_vault,
        'fundsSolVault': sol_funds_vault,
        'nftsOwner': nfts_owner,
        'nftMint': accounts['nft_mint'],
        'nftUserTokenAccount': user_nft_token_account,
        'vaultNftTokenAccount': vault_nft_token_account,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_info,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'metadataProgram': METADATA_PROGRAM_PUBKEY
    }).remaining_accounts([
        {'pubkey': rule_set, 'is_signer': False, 'is_writable': False}
    ]).instruction()
    instructions.append(withdraw_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'account': None, 'instructions': instructions}
