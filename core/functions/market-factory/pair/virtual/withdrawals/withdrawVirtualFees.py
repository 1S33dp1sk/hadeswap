

async def withdraw_virtual_fees(program_id: PublicKey, connection: Client, accounts, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), accounts['pair'].to_bytes()]
    fee_sol_vault = await PublicKey.find_program_address(fee_sol_vault_seed, program.program_id)

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
