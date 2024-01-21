from ..common import *



async def close_virtual_pair(program_id: Pubkey, connection: Client, pair: Pubkey, authority_adapter: Pubkey, user_pubkey: Pubkey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair.to_bytes()]
    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)

    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), pair.to_bytes()]
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)

    close_virtual_pair_instruction = program.close_virtual_nft_swap_pair().accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'fundsSolVault': sol_funds_vault,
        'feeSolVault': fee_sol_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()
    instructions.append(close_virtual_pair_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'instructions': instructions}

async def create_classic_authority_adapter(program_id: Pubkey, connection: Client, pair: Pubkey, user_pubkey: Pubkey, authority_adapter_kp: Keypair, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    authority_adapter = authority_adapter_kp or Keypair()

    create_adapter_instruction = program.create_classic_authority_adapter().accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter.pubkey(),
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()
    instructions.append(create_adapter_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [authority_adapter])
    return {'authorityAdapter': authority_adapter.pubkey(), 'instructions': instructions}

async def initialize_pair(program_id: Pubkey, connection: Client, delta: int, spot_price: int, fee: int, bonding_curve_type: BondingCurveType, pair_type: PairType, hado_market: Pubkey, user_pubkey: Pubkey, send_txn, pair_kp: Optional[Keypair] = None):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    pair = pair_kp or Keypair()
    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), pair.to_bytes_array()]
    fee_sol_vault = await Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)
    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair.to_bytes_array()]
    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)
    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), pair.to_bytes_array()]
    nfts_owner = await Pubkey.find_program_address(nfts_owner_seed, program.program_id)
    initialize_pair_instruction = program.initialize_pair(
        {
            'feeVaultSeed': fee_sol_vault_seed,
            'fundsSolVaultSeed': sol_funds_vault_seed,
            'nftsSeed': nfts_owner_seed,
        },
        {
            'delta': delta,
            'spotPrice': spot_price,
            'fee': fee,
        },
        enum_to_anchor_enum(bonding_curve_type),
        enum_to_anchor_enum(pair_type),
    ).accounts_strict({
        'pair': pair.pubkey(),
        'hadoMarket': hado_market,
        'user': user_pubkey,
        'pairAuthorityAdapterProgram': program_id,
        'partialAdapterProgram': EMPTY_PUBKEY,
        'partialAssetReceiver': EMPTY_PUBKEY,
        'feeSolVault': fee_sol_vault,
        'feeTokenAccount': EMPTY_PUBKEY,
        'fundsSolVault': sol_funds_vault,
        'fundsTokenAccount': EMPTY_PUBKEY,
        'assetReceiver': user_pubkey,
        'assetReceiverTokenAccount': EMPTY_PUBKEY,
        'nftsOwner': nfts_owner,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()
    instructions.append(initialize_pair_instruction)
    await send_txn(Transaction().add(initialize_pair_instruction), [pair])
    return {'pair': pair.pubkey(), 'instructions': instructions}

async def modify_pair(program_id: Pubkey, connection: Client, pair: Pubkey, authority_adapter: Pubkey, user_pubkey: Pubkey, delta: int, spot_price: int, fee: int, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair.to_bytes()]
    sol_funds_vault = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=1000000)
    add_priority_fee = ComputeBudgetProgram.set_compute_unit_price(micro_lamports=1)

    instructions.append(modify_compute_units)
    instructions.append(add_priority_fee)

    modify_pair_instruction = program.modify_pair({
        'delta': delta,
        'spotPrice': spot_price,
        'fee': fee
    }).accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'fundsSolVault': sol_funds_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()
    instructions.append(modify_pair_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'instructions': instructions}

async def put_pair_on_market(program_id: Pubkey, connection: Client, pair: Pubkey, authority_adapter: Pubkey, user_pubkey: Pubkey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    put_pair_on_market_instruction = program.put_pair_on_market().accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()
    instructions.append(put_pair_on_market_instruction)

    await send_txn(Transaction().add(put_pair_on_market_instruction), [])
    return {'instructions': instructions}






