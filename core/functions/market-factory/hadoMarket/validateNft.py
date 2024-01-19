from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.system_program import SYS_PROGRAM_ID, SYSVAR_RENT_PUBKEY
from your_project.helpers import return_anchor_program
from your_project.types import NftValidationWhitelistType

async def validate_nft(program_id: PublicKey, connection: Client, user_pubkey: PublicKey, classic_validation_whitelist: PublicKey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    nft_validation_adapter = Keypair()

    # Assuming the `validateNft` method is implemented in the Python version of the anchor program
    validate_nft_instruction = program.validateNft().accounts_strict({
        'nftValidationAdapter': nft_validation_adapter.public_key,
        'validationWhitelist': classic_validation_whitelist,
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(validate_nft_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [nft_validation_adapter]
    await send_txn(transaction, signers)
    return {'account': nft_validation_adapter.public_key, 'instructions': instructions, 'signers': signers}
