from solana.rpc.api import Client
from solana.publickey import PublicKey

from .helpers import return_anchor_program, anchor_raw_BNs_and_pubkeys_to_nums_and_strings

async def get_specific_accounts(account_id: str, program_id: PublicKey, connection: Client):
    program = await return_anchor_program(program_id, connection)

    # Retrieve specific accounts based on the account identifier
    any_accounts_raw = await getattr(program.account, account_id).all()
    any_accounts = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in any_accounts_raw]

    return any_accounts
