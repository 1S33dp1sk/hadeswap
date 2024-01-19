

async def withdraw_liquidity_only_buy_orders(program_id: PublicKey, connection: Client, accounts, args, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]

    sol_funds_vault = await PublicKey.find_program_address(sol_funds_vault_seed, program.program_id)
    fee_sol_vault = await PublicKey.find_program_address(fee_sol_vault_seed, program.program_id)

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
