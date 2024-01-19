

async def create_classic_authority_adapter(program_id: PublicKey, connection: Client, pair: PublicKey, user_pubkey: PublicKey, authority_adapter_kp: Keypair, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    authority_adapter = authority_adapter_kp or Keypair.generate()

    create_adapter_instruction = program.create_classic_authority_adapter().accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter.public_key,
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()
    instructions.append(create_adapter_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [authority_adapter])
    return {'authorityAdapter': authority_adapter.public_key, 'instructions': instructions}
