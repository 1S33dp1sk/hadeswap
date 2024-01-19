from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.system_program import SYS_PROGRAM_ID, SYSVAR_RENT_PUBKEY
from hadeswap.helpers import return_anchor_program

async def create_merkle_tree_whitelist(program_id: PublicKey, connection: Client, user_pubkey: PublicKey, hado_market: PublicKey, root: bytes, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    nft_validation_adapter_v2 = Keypair()

    # Assuming the `addMerkleTreeWhitelist` method is implemented in the Python version of the anchor program
    add_merkle_tree_whitelist_instruction = program.addMerkleTreeWhitelist(list(root)).accounts_strict({
        'nftValidationAdapter': nft_validation_adapter_v2.public_key,
        'hadoMarket': hado_market,
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(add_merkle_tree_whitelist_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [nft_validation_adapter_v2]
    await send_txn(transaction, signers)
    return {'account': nft_validation_adapter_v2.public_key, 'instructions': instructions, 'signers': signers}

# Example usage
# await create_merkle_tree_whitelist(program_id, connection, user_pubkey, hado_market, root, send_txn)
