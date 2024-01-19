

async def deposit_sol_to_pair(program_id: PublicKey, connection: Client, pair: PublicKey, authority_adapter: PublicKey, user_pubkey: PublicKey, amount_of_orders: int, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair]
    sol_funds_vault = await PublicKey.find_program_address(sol_funds_vault_seed, program.program_id)

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
