from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.system_program import SYS_PROGRAM_ID, SYSVAR_RENT_PUBKEY
from hadeswap.helpers import return_anchor_program, enum_to_anchor_enum
from hadeswap.types import NftValidationWhitelistType

async def add_classic_whitelist_to_market(program_id: PublicKey, connection: Client, user_pubkey: PublicKey, hado_market: PublicKey, whitelisted_address: PublicKey, whitelist_type: NftValidationWhitelistType, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    validation_whitelist = Keypair()

    # Convert Python enum to a format suitable for the Anchor program
    anchor_enum_whitelist_type = enum_to_anchor_enum(whitelist_type)

    # Assuming the `addClassicWhitelistToMarket` method is implemented in the Python version of the anchor program
    add_classic_whitelist_to_market_instruction = program.addClassicWhitelistToMarket(anchor_enum_whitelist_type).accounts_strict({
        'validationWhitelist': validation_whitelist.public_key,
        'hadoMarket': hado_market,
        'user': user_pubkey,
        'whitelistedAddress': whitelisted_address,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(add_classic_whitelist_to_market_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [validation_whitelist]
    await send_txn(transaction, signers)
    return {'account': validation_whitelist.public_key, 'instructions': instructions, 'signers': signers}

# Example usage
# await add_classic_whitelist_to_market(program_id, connection, user_pubkey, hado_market, whitelisted_address, NftValidationWhitelistType.YOUR_TYPE, send_txn)
