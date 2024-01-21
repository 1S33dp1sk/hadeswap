
from ..common import *

async def generate_initialize_pair_instructions(program_id: Pubkey, connection: Client, delta: int, spot_price: int, fee: int, bonding_curve_type: BondingCurveType, pair_type: PairType, hado_market: Pubkey, user_pubkey: Pubkey, pair_kp: Optional[Keypair] = None):
    program = return_anchor_program(program_id, connection)
    instructions = []
    pair = pair_kp or Keypair()
    fee_sol_vault_seed = [FEE_PREFIX.encode(ENCODER), bytes(pair.pubkey())]
    fee_sol_vault, fee_sol_vault_bump = Pubkey.find_program_address(fee_sol_vault_seed, program.program_id)
    sol_funds_vault_seed = [SOL_FUNDS_PREFIX.encode(ENCODER), bytes(pair.pubkey())]
    sol_funds_vault, sol_funds_vault_bump = Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)
    nfts_owner_seed = [NFTS_OWNER_PREFIX.encode(ENCODER), bytes(pair.pubkey())]
    nfts_owner, nfts_owner_bump = Pubkey.find_program_address(nfts_owner_seed, program.program_id)

    # Access the method and set arguments
    init_pair = program.methods["initialize_pair"]
    combined_args = {
        'bumps': {
            'feeVault': fee_sol_vault_bump,
            'fundsSolVault': sol_funds_vault_bump,
            'nftsOwner': nfts_owner_bump
        },
        'params': {
            'delta': delta,
            'spotPrice': spot_price,
            'fee': fee
        },
        "bondingCurveType":enum_to_anchor_enum(bonding_curve_type),
        "pairType":enum_to_anchor_enum(pair_type)
    }

    init_pair_args = init_pair.args(combined_args)

    # Build the instruction
    initialize_pair_instruction = init_pair_args.accounts({
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
    })

    instructions.append(initialize_pair_instruction)

    return {'pair': pair.pubkey(), 'instructions': instructions}


async def generate_deposit_sol_to_pair_instructions(program_id: Pubkey, connection: Client, pair: Pubkey, authority_adapter: Pubkey, user_pubkey: Pubkey, amount_of_orders: int):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [SOL_FUNDS_PREFIX.encode(ENCODER), bytes(pair.pubkey())]
    sol_funds_vault, sol_funds_vault_bump = await Pubkey.find_program_address(sol_funds_vault_seed, program.program_id)

    modify_compute_units = ComputeBudgetProgram.set_compute_unit_limit(units=70000000 * (amount_of_orders // 10) + 1)
    add_priority_fee = ComputeBudgetProgram.set_compute_unit_price(micro_lamports=1)

    instructions.append(modify_compute_units)
    instructions.append(add_priority_fee)

    # Access the method and set arguments
    deposit_sol_to_pair = program.methods["depositSolToPair"]
    deposit_sol_to_pair_args = deposit_sol_to_pair.args(BN(amount_of_orders))

    # Build the instruction
    deposit_sol_to_pair_instruction = deposit_sol_to_pair_args.accounts({
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'fundsSolVault': sol_funds_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    })

    instructions.append(deposit_sol_to_pair_instruction)

    return {'account': None, 'instructions': instructions, 'signers': []}
