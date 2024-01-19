


async def deposit_nft_to_pair(program_id: PublicKey, connection: Client, args, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair'].to_bytes()]
    nfts_owner = await PublicKey.find_program_address(nfts_owner_seed, program.program_id)

    nft_pair_box = Keypair.generate()

    user_nft_token_account = await find_associated_token_address(accounts['user_pubkey'], accounts['nft_mint'])
    vault_nft_token_account = await find_associated_token_address(nfts_owner, accounts['nft_mint'])

    metadata_info = get_metaplex_metadata_pda(accounts['nft_mint'])
    edition_info = get_metaplex_edition_pda(accounts['nft_mint'])
    owner_token_record = find_token_record_pda(accounts['nft_mint'], user_nft_token_account)
    dest_token_record = find_token_record_pda(accounts['nft_mint'], vault_nft_token_account)
    rule_set = METADATA_PROGRAM_PUBKEY
    if args.get('pnft') and args['pnft'].get('payer_rule_set') and args['pnft'].get('name_for_rule_set'):
        rule_set = await find_rule_set_pda(args['pnft']['payer_rule_set'], args['pnft']['name_for_rule_set'])

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)
    instructions.append(modify_compute_units)

    deposit_nft_instruction = await program.deposit_nft_to_pair(
        args.get('proof', []), None
    ).accounts_strict({
        'nftPairBox': nft_pair_box.public_key,
        'nftValidationAdapter': accounts['nft_validation_adapter'],
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'nftsOwner': nfts_owner,
        'nftMint': accounts['nft_mint'],
        'nftUserTokenAccount': user_nft_token_account,
        'vaultTokenAccount': vault_nft_token_account,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_info,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
    }).remaining_accounts(
        [{'pubkey': accounts['nft_validation_adapter_v2'], 'is_signer': False, 'is_writable': False},
         {'pubkey': rule_set, 'is_signer': False, 'is_writable': False}] if 'nft_validation_adapter_v2' in accounts else
        [{'pubkey': rule_set, 'is_signer': False, 'is_writable': False}]
    ).instruction()
    instructions.append(deposit_nft_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [nft_pair_box])
    return {'account': nft_pair_box.public_key, 'instructions': instructions}
