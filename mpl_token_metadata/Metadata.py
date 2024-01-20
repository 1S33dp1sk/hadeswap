import asyncio
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.transaction import AccountMeta, TransactionInstruction, Transaction

async def from_account_address(connection, account_address):
    """Fetches and parses metadata information of a token from a given account address."""
    program_id = PublicKey("metaqbxxUerdDd1a7Qo8Luv6tqKx1dSC2Vm")  # Metaplex Metadata program ID
    account_pubkey = PublicKey(account_address)

    # Create an instruction to fetch metadata
    instruction = TransactionInstruction(
        keys=[
            AccountMeta(pubkey=account_pubkey, is_signer=False, is_writable=False),
        ],
        program_id=program_id,
    )

    # Create and send the transaction
    transaction = Transaction()
    transaction.add(instruction)
    response = await connection.send_transaction(transaction, [])

    # Fetch and parse metadata account data
    account_info = await connection.get_account_info(account_pubkey)
    metadata_account = Metadata.parse(account_info['result']['value']['data'])

    return metadata_account


# Example usage
# async def main():
#     connection = Client("https://api.mainnet-beta.solana.com")
#     metadata_info = "PUT_METADATA_ACCOUNT_ADDRESS_HERE"
#     metadata_account = await from_account_address(connection, metadata_info)
#     print(metadata_account)



# asyncio.run(main())