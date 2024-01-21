from ..common import *


async def withdraw_liquidity_from_balanced_pair(program_id: Pubkey, connection: Client, args, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair'].to_bytes()]
    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]

    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)
    nfts_owner = await Pubkey.find_program_address(nfts_owner_seed, program.program_id)
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)

    user_nft_token_account = await find_associated_token_address(accounts['user_pubkey'], accounts['nft_mint'])
    vault_nft_token_account = await find_associated_token_address(nfts_owner, accounts['nft_mint'])

    edition_id = get_metaplex_edition_pda(accounts['nft_mint'])
    metadata_info = get_metaplex_metadata_pda(accounts['nft_mint'])
    owner_token_record = find_token_record_pda(accounts['nft_mint'], vault_nft_token_account)
    dest_token_record = find_token_record_pda(accounts['nft_mint'], user_nft_token_account)
    rule_set = METADATA_PROGRAM_PUBKEY
    if args.get('pnft') and args['pnft'].get('payer_rule_set') and args['pnft'].get('name_for_rule_set'):
        rule_set = await find_rule_set_pda(args['pnft']['payer_rule_set'], args['pnft']['name_for_rule_set'])

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)
    instructions.append(modify_compute_units)

    withdraw_instruction = await program.withdraw_liquidity_from_balanced_pair(
        None
    ).accounts_strict({
        'nftPairBox': accounts['nft_pair_box'],
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'fundsSolVault': sol_funds_vault,
        'feeSolVault': fee_sol_vault,
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
        'editionInfo': edition_id,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
    }).remaining_accounts([{'pubkey': rule_set, 'is_signer': False, 'is_writable': False}]).instruction()
    instructions.append(withdraw_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'account': None, 'instructions': instructions}

async def withdraw_liquidity_from_buy_orders_pair(program_id: Pubkey, connection: Client, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]

    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)
    instructions.append(modify_compute_units)

    withdraw_instruction = await program.withdraw_liquidity_from_buy_orders_pair().accounts_strict({
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'fundsSolVault': sol_funds_vault,
        'feeSolVault': fee_sol_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY
    }).remaining_accounts([{'pubkey': Keypair().public_key, 'is_signer': False, 'is_writable': False}]).instruction()
    instructions.append(withdraw_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'account': None, 'instructions': instructions}

async def withdraw_liquidity_from_sell_orders_pair(program_id: Pubkey, connection: Client, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]

    nfts_owner = await Pubkey.find_program_address(nfts_owner_seed, program.program_id)
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)

    user_nft_token_account_first = await find_associated_token_address(accounts['user_pubkey'], accounts['nft_mint_first'])
    vault_nft_token_account_first = await find_associated_token_address(nfts_owner, accounts['nft_mint_first'])

    user_nft_token_account_second = await find_associated_token_address(accounts['user_pubkey'], accounts['nft_mint_second'])
    vault_nft_token_account_second = await find_associated_token_address(nfts_owner, accounts['nft_mint_second'])

    metadata_info_first = get_metaplex_metadata_pda(accounts['nft_mint_first'])
    edition_info_first = get_metaplex_edition_pda(accounts['nft_mint_first'])
    owner_token_record_first = find_token_record_pda(accounts['nft_mint_first'], vault_nft_token_account_first)
    dest_token_record_first = find_token_record_pda(accounts['nft_mint_first'], user_nft_token_account_first)

    metadata_info_second = get_metaplex_metadata_pda(accounts['nft_mint_second'])
    edition_info_second = get_metaplex_edition_pda(accounts['nft_mint_second'])
    owner_token_record_second = find_token_record_pda(accounts['nft_mint_second'], vault_nft_token_account_second)
    dest_token_record_second = find_token_record_pda(accounts['nft_mint_second'], user_nft_token_account_second)

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)
    instructions.append(modify_compute_units)

    withdraw_instruction = await program.withdraw_liquidity_from_sell_orders_pair().accounts_strict({
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'nftsOwner': nfts_owner,
        'feeSolVault': fee_sol_vault,
        'nftPairBoxFirst': accounts['nft_pair_box_first'],
        'nftMintFirst': accounts['nft_mint_first'],
        'nftUserTokenAccountFirst': user_nft_token_account_first,
        'vaultNftTokenAccountFirst': vault_nft_token_account_first,
        'nftPairBoxSecond': accounts['nft_pair_box_second'],
        'nftMintSecond': accounts['nft_mint_second'],
        'nftUserTokenAccountSecond': user_nft_token_account_second,
        'vaultNftTokenAccountSecond': vault_nft_token_account_second,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfoFirst': metadata_info_first,
        'ownerTokenRecordFirst': owner_token_record_first,
        'destTokenRecordFirst': dest_token_record_first,
        'editionInfoFirst': edition_info_first,
        'metadataInfoSecond': metadata_info_second,
        'ownerTokenRecordSecond': owner_token_record_second,
        'destTokenRecordSecond': dest_token_record_second,
        'editionInfoSecond': edition_info_second,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'metadataProgram': METADATA_PROGRAM_PUBKEY
    }).instruction()
    instructions.append(withdraw_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'account': None, 'instructions': instructions}

async def withdraw_liquidity_only_buy_orders(program_id: Pubkey, connection: Client, accounts, args, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]

    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)
    instructions.append(modify_compute_units)

    withdraw_instruction = await program.withdraw_liquidity_only_buy_orders(BN(args['amount_of_orders'])).accounts_strict({
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'fundsSolVault': sol_funds_vault,
        'feeSolVault': fee_sol_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY
    }).remaining_accounts([{'pubkey': Keypair().public_key, 'is_signer': False, 'is_writable': False}]).instruction()
    instructions.append(withdraw_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'account': None, 'instructions': instructions}

async def withdraw_liquidity_order_virtual_fees(program_id: Pubkey, connection: Client, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)
    instructions.append(modify_compute_units)

    withdraw_instruction = await program.withdraw_liquidity_order_virtual_fees().accounts_strict({
        'liquidityProvisionOrder': accounts['liquidity_provision_order'],
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'feeSolVault': fee_sol_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY
    }).instruction()
    instructions.append(withdraw_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'account': None, 'instructions': instructions}

async def withdraw_liquidity_single_sell_order(program_id: Pubkey, connection: Client, accounts, args, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair'].to_bytes()]
    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]

    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)
    nfts_owner = await Pubkey.find_program_address(nfts_owner_seed, program.program_id)
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)

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

async def withdraw_nft_from_pair(program_id: Pubkey, connection: Client, args, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair'].to_bytes()]
    nfts_owner = await Pubkey.find_program_address(nfts_owner_seed, program.program_id)

    user_nft_token_account = await find_associated_token_address(accounts['user_pubkey'], accounts['nft_mint'])
    vault_nft_token_account = await find_associated_token_address(nfts_owner, accounts['nft_mint'])

    owner_token_record = find_token_record_pda(accounts['nft_mint'], vault_nft_token_account)
    dest_token_record = find_token_record_pda(accounts['nft_mint'], user_nft_token_account)
    edition_info = get_metaplex_edition_pda(accounts['nft_mint'])
    metadata_info = get_metaplex_metadata_pda(accounts['nft_mint'])
    rule_set = await find_rule_set_pda(args['pnft']['payer_rule_set'], args['pnft']['name_for_rule_set']) if args.get('pnft') else METADATA_PROGRAM_PUBKEY

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=400000)
    instructions.append(modify_compute_units)

    withdraw_instruction = await program.withdraw_nft_from_pair(None).accounts_strict({
        'nftPairBox': accounts['nft_pair_box'],
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
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

async def withdraw_sol_from_pair(program_id: Pubkey, connection: Client, accounts, args, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair'].to_bytes()]
    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=round(100000000))
    add_priority_fee = ComputeBudgetProgram.set_compute_unit_price(micro_lamports=1)

    instructions.append(modify_compute_units)
    instructions.append(add_priority_fee)

    withdraw_instruction = await program.withdraw_sol_from_pair(BN(args['amount_of_orders'])).accounts_strict({
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'fundsSolVault': sol_funds_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY
    }).instruction()
    instructions.append(withdraw_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'account': None, 'instructions': instructions}

async def withdraw_virtual_fees(program_id: Pubkey, connection: Client, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)

    withdraw_instruction = await program.withdraw_virtual_fees().accounts_strict({
        'pair': accounts['pair'],
        'authorityAdapter': accounts['authority_adapter'],
        'user': accounts['user_pubkey'],
        'feeSolVault': fee_sol_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY
    }).instruction()
    instructions.append(withdraw_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'account': None, 'instructions': instructions}













































