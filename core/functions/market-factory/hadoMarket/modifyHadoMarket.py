from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import SYS_PROGRAM_ID, SYSVAR_RENT_PUBKEY
from your_project.helpers import return_anchor_program
from your_project.constants import EMPTY_PUBKEY, ENCODER, FEE_PREFIX, NFTS_OWNER_PREFIX, SOL_FUNDS_PREFIX
from your_project.types import BondingCurveType, PairType

async def modify_hado_market(program_id: PublicKey, connection: Client, user_pubkey: PublicKey, hado_market: PublicKey, validation_adapter_authority: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    # Assuming the `modifyHadoMarket` method is implemented in the Python version of the anchor program
    modify_hado_market_instruction = program.modifyHadoMarket().accounts_strict({
        'hadoMarket': hado_market,
        'user': user_pubkey,
        'validationAdapterProgram': validation_adapter_authority,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(modify_hado_market_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}

# Example usage
# await modify_hado_market(program_id, connection, user_pubkey, hado_market, validation_adapter_authority, send_txn)
