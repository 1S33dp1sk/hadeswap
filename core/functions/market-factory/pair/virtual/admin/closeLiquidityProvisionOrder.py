


async def close_liquidity_provision_order(program_id: PublicKey, connection: Client, liquidity_provision_order: PublicKey, admin: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    close_liquidity_provision_order_instruction = program.closeLiquidityProvisionOrder().accounts_strict({
        'liquidityProvisionOrder': liquidity_provision_order,
        'admin': admin,
    }).instruction()

    instructions.append(close_liquidity_provision_order_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}
