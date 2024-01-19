from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.system_program import SYS_PROGRAM_ID, SYSVAR_RENT_PUBKEY
from your_project.helpers import return_anchor_program
from your_project.constants import EMPTY_PUBKEY, ENCODER, FEE_PREFIX, NFTS_OWNER_PREFIX, SOL_FUNDS_PREFIX
from your_project.types import BondingCurveType, PairType

async def initialize_hado_market(program_id: PublicKey, connection: Client, user_pubkey: PublicKey, validation_adapter_program: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    hado_market = Keypair()

    # Assuming the `initializeHadoMarket` method is implemented in the Python version of the anchor program
    initialize_hado_market_instruction = program.initializeHadoMarket().accounts_strict({
        'hadoMarket': hado_market.public_key,
        'user': user_pubkey,
        'validationAdapterProgram': validation_adapter_program,
        'pairTokenMint': EMPTY_PUBKEY,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(initialize_hado_market_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [hado_market]
    await send_txn(transaction, signers)
    return {'account': hado_market.public_key, 'instructions': instructions, 'signers': signers}

# Example usage
# await initialize_hado_market(program_id, connection, user_pubkey, validation_adapter_program, send_txn)
