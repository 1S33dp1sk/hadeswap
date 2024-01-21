from ..common import *


async def buy_nft_from_pair(program_id: Pubkey,connection: Client,args: dict,accounts: dict,send_txn):
    program = return_anchor_program(program_id, connection)
    instructions = []

    # Finding program addresses
    sol_funds_vault, _ = await Pubkey.find_program_address(
        [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair']], program_id
    )
    nfts_owner, _ = await Pubkey.find_program_address(
        [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair']], program_id
    )
    fee_sol_vault, _ = await Pubkey.find_program_address(
        [ENCODER.encode(FEE_PREFIX), accounts['pair']], program_id
    )

    # Finding associated token addresses and PDAs
    user_nft_token_account = await find_associated_token_address(accounts['userPubkey'], accounts['nftMint'])
    owner_token_record = find_token_record_pda(accounts['nftMint'], accounts['vaultNftTokenAccount'])
    dest_token_record = find_token_record_pda(accounts['nftMint'], user_nft_token_account)
    edition_info = get_metaplex_edition_pda(accounts['nftMint'])
    metadata_info = get_metaplex_metadata(accounts['nftMint'])
    metadata_account = await Metadata.from_account_address(connection, metadata_info)

    # Determining the rule set
    rule_set = METADATA_PROGRAM_PUBKEY
    if args.get('pnft'):
        if args['pnft'].get('payerRuleSet') and args['pnft'].get('nameForRuleSet'):
            rule_set = await find_rule_set_pda(args['pnft']['payerRuleSet'], args['pnft']['nameForRuleSet'])
        elif metadata_account.programmable_config:
            rule_set = metadata_account.programmable_config.rule_set

    # Handling creators
    creators = metadata_account.data.creators if metadata_account.data else None
    creator_account_metas = [
        AccountMeta(pubkey=creator.address, is_signer=False, is_writable=True)
        for creator in creators if creator.share > 0
    ] if creators else []

    # Modify compute units instruction (adjust units as needed)
    modify_compute_units = AccountMeta(pubkey=Pubkey('ComputeBudget111111111111111111111111111111'), is_signer=False, is_writable=False)
    instructions.append(modify_compute_units)

    # Construct the buyNftFromPair instruction
    buy_nft_instruction = await program.buy_nft_from_pair(
        args['maxAmountToPay'], args['skipFailed'], None
    ).accounts_strict({
        'nftPairBox': accounts['nftPairBox'],
        'pair': accounts['pair'],
        'user': accounts['userPubkey'],
        'fundsSolVault': sol_funds_vault,
        'nftsOwner': nfts_owner,
        'feeSolVault': fee_sol_vault,
        'nftMint': accounts['nftMint'],
        'vaultNftTokenAccount': accounts['vaultNftTokenAccount'],
        'nftUserTokenAccount': user_nft_token_account,
        'assetReceiver': accounts['assetReceiver'],
        'protocolFeeReceiver': accounts['protocolFeeReceiver'],
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
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
    }).remaining_accounts([
        {'pubkey': rule_set or METADATA_PROGRAM_PUBKEY, 'isSigner': False, 'isWritable': False}
    ] + creator_account_metas).instruction()

    # Add the instruction to the instructions list
    instructions.append(buy_nft_instruction)

    # Create and populate the transaction
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    # Define the signers (if any)
    signers = []

    # Send the transaction
    await send_txn(transaction, signers)

    # Return the result
    return {'account': None, 'instructions': transaction.instructions, 'signers': signers}

async def sell_nft_to_liquidity_pair(program_id: Pubkey,connection: Client,args: dict,accounts: dict,send_txn):
    program = return_anchor_program(program_id, connection)
    nft_pair_box = Keypair.generate()

    user_nft_token_account = await find_associated_token_address(accounts['userPubkey'], accounts['nftMint'])

    nfts_owner, _ = await Pubkey.find_program_address(
        [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair']], program_id
    )
    fee_sol_vault, _ = await Pubkey.find_program_address(
        [ENCODER.encode(FEE_PREFIX), accounts['pair']], program_id
    )
    sol_funds_vault, _ = await Pubkey.find_program_address(
        [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair']], program_id
    )

    new_vault_token_account = await find_associated_token_address(nfts_owner, accounts['nftMint'])
    owner_token_record = find_token_record_pda(accounts['nftMint'], user_nft_token_account)
    dest_token_record = find_token_record_pda(accounts['nftMint'], new_vault_token_account)
    edition_info = get_metaplex_edition_pda(accounts['nftMint'])
    metadata_info = get_metaplex_metadata_pda(accounts['nftMint'])
    metadata_account = await Metadata.from_account_address(connection, metadata_info)

    rule_set = METADATA_PROGRAM_PUBKEY
    if args.get('pnft'):
        if args['pnft'].get('payerRuleSet') and args['pnft'].get('nameForRuleSet'):
            rule_set = await find_rule_set_pda(args['pnft']['payerRuleSet'], args['pnft']['nameForRuleSet'])
        elif metadata_account.programmable_config:
            rule_set = metadata_account.programmable_config.rule_set

    creators = metadata_account.data.creators if metadata_account.data else None
    creator_account_metas = [
        AccountMeta(pubkey=creator.address, is_signer=False, is_writable=True)
        for creator in creators if creator.share > 0
    ] if creators else []

    modify_compute_units = AccountMeta(pubkey=Pubkey('ComputeBudget111111111111111111111111111111'), is_signer=False, is_writable=False)

    # Construct the sellNftToLiquidityPair instruction
    sell_nft_instruction = await program.sell_nft_to_liquidity_pair(
        args['minAmountToGet'], args['skipFailed'], args.get('proof', []), None
    ).accounts_strict({
        'nftPairBox': nft_pair_box.public_key,
        'nftValidationAdapter': accounts['nftValidationAdapter'],
        'pair': accounts['pair'],
        'user': accounts['userPubkey'],
        'nftMint': accounts['nftMint'],
        'nftUserTokenAccount': user_nft_token_account,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'nftsOwner': nfts_owner,
        'feeSolVault': fee_sol_vault,
        'newVaultTokenAccount': new_vault_token_account,
        'protocolFeeReceiver': accounts['protocolFeeReceiver'],
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'fundsSolVault': sol_funds_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_info,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
    }).remaining_accounts(
        [{'pubkey': accounts.get('nftValidationAdapterV2', rule_set), 'isSigner': False, 'isWritable': False}] + creator_account_metas
    ).instruction()

    # Create and populate the transaction
    transaction = Transaction()
    transaction.add(modify_compute_units)
    transaction.add(sell_nft_instruction)

    # Define the signers
    signers = [nft_pair_box]

    # Send the transaction
    await send_txn(transaction, signers)

    # Return the result
    return {'account': nft_pair_box.public_key, 'instructions': transaction.instructions, 'signers': signers}

async def sell_nft_to_token_to_nft_pair(program_id: Pubkey,connection: Client,args: dict,accounts: dict,send_txn):
    program = return_anchor_program(program_id, connection)
    instructions = []

    user_nft_token_account = await find_associated_token_address(accounts['userPubkey'], accounts['nftMint'])
    asset_receiver_token_account = await find_associated_token_address(accounts['assetReceiver'], accounts['nftMint'])

    sol_funds_vault, _ = await Pubkey.find_program_address(
        [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair']], program_id
    )

    owner_token_record = find_token_record_pda(accounts['nftMint'], user_nft_token_account)
    dest_token_record = find_token_record_pda(accounts['nftMint'], asset_receiver_token_account)
    edition_info = get_metaplex_edition_pda(accounts['nftMint'])
    metadata_info = get_metaplex_metadata_pda(accounts['nftMint'])
    metadata_account = await Metadata.from_account_address(connection, metadata_info)

    rule_set = METADATA_PROGRAM_PUBKEY
    if args.get('pnft'):
        if args['pnft'].get('payerRuleSet') and args['pnft'].get('nameForRuleSet'):
            rule_set = await find_rule_set_pda(args['pnft']['payerRuleSet'], args['pnft']['nameForRuleSet'])
        elif metadata_account.programmable_config:
            rule_set = metadata_account.programmable_config.rule_set

    creators = metadata_account.data.creators if metadata_account.data else None
    creator_account_metas = [
        AccountMeta(pubkey=creator.address, is_signer=False, is_writable=True)
        for creator in creators if creator.share > 0
    ] if creators else []

    modify_compute_units = AccountMeta(pubkey=Pubkey('ComputeBudget111111111111111111111111111111'), is_signer=False, is_writable=False)
    instructions.append(modify_compute_units)

    # Construct the sellNftToTokenToNftPair instruction
    sell_nft_instruction = await program.sell_nft_to_token_to_nft_pair(
        args['minAmountToGet'], args['skipFailed'], args.get('proof', []), None
    ).accounts_strict({
        'nftValidationAdapter': accounts['nftValidationAdapter'],
        'pair': accounts['pair'],
        'user': accounts['userPubkey'],
        'nftMint': accounts['nftMint'],
        'nftUserTokenAccount': user_nft_token_account,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'assetReceiver': accounts['assetReceiver'],
        'protocolFeeReceiver': accounts['protocolFeeReceiver'],
        'assetReceiverTokenAccount': asset_receiver_token_account,
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'fundsSolVault': sol_funds_vault,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_info,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
    }).remaining_accounts(
        [{'pubkey': accounts.get('nftValidationAdapterV2', rule_set), 'isSigner': False, 'isWritable': False}] + creator_account_metas
    ).instruction()

    # Add the instruction to the instructions list
    instructions.append(sell_nft_instruction)

    # Create and populate the transaction
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    # Define the signers (if any)
    signers = []

    # Send the transaction
    await send_txn(transaction, signers)

    # Return the result
    return {'account': None, 'instructions': transaction.instructions, 'signers': signers}


