

async def close_nft_validation_adapter_v2(program_id: PublicKey, connection: Client, nft_validation_adapter_v2: PublicKey, admin: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    close_nft_validation_adapter_v2_instruction = program.closeNftValidationAdapterV2().accounts_strict({
        'nftValidationAdapterV2': nft_validation_adapter_v2,
        'admin': admin,
    }).instruction()

    instructions.append(close_nft_validation_adapter_v2_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}
