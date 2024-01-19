

async def close_nft_validation_adapter(program_id: PublicKey, connection: Client, nft_validation_adapter: PublicKey, admin: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    close_nft_validation_adapter_instruction = program.closeNftValidationAdapter().accounts_strict({
        'nftValidationAdapter': nft_validation_adapter,
        'admin': admin,
    }).instruction()

    instructions.append(close_nft_validation_adapter_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}
