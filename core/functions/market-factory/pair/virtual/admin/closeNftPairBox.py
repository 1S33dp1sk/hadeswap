


async def close_nft_pair_box(program_id: PublicKey, connection: Client, nft_pair_box: PublicKey, admin: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    close_nft_pair_box_instruction = program.closeNftPairBox().accounts_strict({
        'nftPairBox': nft_pair_box,
        'admin': admin,
    }).instruction()

    instructions.append(close_nft_pair_box_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}
