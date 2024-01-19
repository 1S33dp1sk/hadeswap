

async def put_pair_on_market(program_id: PublicKey, connection: Client, pair: PublicKey, authority_adapter: PublicKey, user_pubkey: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    put_pair_on_market_instruction = program.put_pair_on_market().accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()
    instructions.append(put_pair_on_market_instruction)

    await send_txn(Transaction().add(put_pair_on_market_instruction), [])
    return {'instructions': instructions}
