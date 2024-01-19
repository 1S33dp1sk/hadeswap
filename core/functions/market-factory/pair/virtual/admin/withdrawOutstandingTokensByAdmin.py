

async def withdraw_outstanding_tokens_by_admin(program_id: PublicKey, connection: Client, pair: PublicKey, admin: PublicKey, token_mint: PublicKey, payer_rule_set: PublicKey, name_for_rule_set: str, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), pair]
    nfts_owner = await PublicKey.find_program_address(nfts_owner_seed, program.program_id)

    admin_token_account = await find_associated_token_address(admin, token_mint)
    pair_token_account = await find_associated_token_address(nfts_owner, token_mint)

    edition_id = get_metaplex_edition_pda(token_mint)
    metadata_info = get_metaplex_metadata(token_mint)
    owner_token_record = find_token_record_pda(token_mint, pair_token_account)
    dest_token_record = find_token_record_pda(token_mint, admin_token_account)
    rule_set = await find_rule_set_pda(payer_rule_set, name_for_rule_set)

    withdraw_outstanding_tokens_instruction = program.withdrawOutstandingTokensByAdmin(None).accounts_strict({
        'pair': pair,
        'nftsOwner': nfts_owner,
        'nftMint': token_mint,
        'user': admin,
        'nftUserTokenAccount': admin_token_account,
        'vaultNftTokenAccount': pair_token_account,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_id,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).remaining_accounts([{
        'pubkey': rule_set,
        'isSigner': False,
        'isWritable': False,
    }]).instruction()

    instructions.append(withdraw_outstanding_tokens_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}
