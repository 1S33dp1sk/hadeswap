


async def initialize_pair(program_id: PublicKey, connection: Client, delta: int, spot_price: int, fee: int, bonding_curve_type: BondingCurveType, pair_type: PairType, hado_market: PublicKey, user_pubkey: PublicKey, send_txn, pair_kp: Optional[Keypair] = None):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    pair = pair_kp or Keypair.generate()

    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), pair.public_key.to_bytes()]
    fee_sol_vault = await PublicKey.find_program_address(fee_sol_vault_seed, program.program_id)

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair.public_key.to_bytes()]
    sol_funds_vault = await PublicKey.find_program_address(sol_funds_vault_seed, program.program_id)

    nfts_owner_seed = [ENCODER.encode(NFTS_OWNER_PREFIX), pair.public_key.to_bytes()]
    nfts_owner = await PublicKey.find_program_address(nfts_owner_seed, program.program_id)

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
        'pair': pair.public_key,
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
    return {'pair': pair.public_key, 'instructions': instructions}

