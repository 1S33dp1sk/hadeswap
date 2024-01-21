from ..common import *



async def deposit_liquidity_only_buy_orders_to_pair(program_id: Pubkey, connection: Client, pair: Pubkey, authority_adapter: Pubkey, user_pubkey: Pubkey, amount_of_orders: int, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair]
    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)

    deposit_liquidity_only_buy_orders_instruction = program.depositLiquidityOnlyBuyOrders(BN(amount_of_orders)).accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'fundsSolVault': sol_funds_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(deposit_liquidity_only_buy_orders_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}

async def deposit_liquidity_single_sell_order(program_id: Pubkey, connection: Client, pair: Pubkey, authority_adapter: Pubkey, user_pubkey: Pubkey, nft_mint: Pubkey, nft_validation_adapter: Pubkey, proof: list, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    funds_sol_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair]
    funds_sol_vault = await Pubkey.find_program_address(funds_sol_vault_seed, program.program_id)
    
    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), pair]
    nfts_owner = await Pubkey.find_program_address(nfts_owner_seed, program.program_id)

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

async def deposit_liquidity_to_pair(program_id: Pubkey, connection: Client, pair: Pubkey, authority_adapter: Pubkey, user_pubkey: Pubkey, nft_mint: Pubkey, nft_validation_adapter: Pubkey, proof: list, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    funds_sol_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair]
    funds_sol_vault = await Pubkey.find_program_address(funds_sol_vault_seed, program.program_id)
    
    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), pair]
    nfts_owner = await Pubkey.find_program_address(nfts_owner_seed, program.program_id)

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

    deposit_liquidity_to_pair_instruction = program.depositLiquidityToPair(proof or [], None).accounts_strict({
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

    instructions.append(deposit_liquidity_to_pair_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [nft_pair_box]
    await send_txn(transaction, signers)
    return {'nftPairBox': nft_pair_box.public_key, 'instructions': instructions, 'signers': signers}

async def deposit_nft_to_pair(program_id: Pubkey, connection: Client, args, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair'].to_bytes()]
    nfts_owner = await Pubkey.find_program_address(nfts_owner_seed, program.program_id)

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

async def deposit_sol_to_pair(program_id: Pubkey, connection: Client, pair: Pubkey, authority_adapter: Pubkey, user_pubkey: Pubkey, amount_of_orders: int, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair]
    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=70000000 * (amount_of_orders // 10) + 1)
    add_priority_fee = ComputeBudgetProgram.set_compute_unit_price(micro_lamports=1)

    instructions.append(modify_compute_units)
    instructions.append(add_priority_fee)

    deposit_sol_to_pair_instruction = program.depositSolToPair(BN(amount_of_orders)).accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'fundsSolVault': sol_funds_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(deposit_sol_to_pair_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}


