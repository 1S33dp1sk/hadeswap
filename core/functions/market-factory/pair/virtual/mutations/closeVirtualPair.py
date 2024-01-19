
async def close_virtual_pair(program_id: PublicKey, connection: Client, pair: PublicKey, authority_adapter: PublicKey, user_pubkey: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    sol_funds_vault_seed = [ENCODER.encode(SOL_FUNDS_PREFIX), pair.to_bytes()]
    sol_funds_vault = await PublicKey.find_program_address(sol_funds_vault_seed, program.program_id)

    fee_sol_vault_seed = [ENCODER.encode(FEE_PREFIX), pair.to_bytes()]
    fee_sol_vault = await PublicKey.find_program_address(fee_sol_vault_seed, program.program_id)

    close_virtual_pair_instruction = program.close_virtual_nft_swap_pair().accounts_strict({
        'pair': pair,
        'authorityAdapter': authority_adapter,
        'user': user_pubkey,
        'fundsSolVault': sol_funds_vault,
        'feeSolVault': fee_sol_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()
    instructions.append(close_virtual_pair_instruction)

    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    await send_txn(transaction, [])
    return {'instructions': instructions}
