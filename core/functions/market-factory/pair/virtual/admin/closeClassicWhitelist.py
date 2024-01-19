


async def close_classic_whitelist(program_id: PublicKey, connection: Client, validation_whitelist: PublicKey, admin: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    close_classic_whitelist_instruction = program.closeClassicWhitelist().accounts_strict({
        'validationWhitelist': validation_whitelist,
        'admin': admin,
    }).instruction()

    instructions.append(close_classic_whitelist_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}


