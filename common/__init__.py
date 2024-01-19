from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from solana.rpc.api import Client
from solana.transaction import TransactionInstruction
from spl.token.constants import TOKEN_PROGRAM_ID, ASSOCIATED_TOKEN_PROGRAM_ID
from spl.token.instructions import create_associated_token_account
from classes.nodewallet import NodeWallet
from typing import List


def create_fake_wallet() -> NodeWallet:
    secret_key = [
        208, 175, 150, 242, 88, 34, 108, 88, 177, 16, 168, 75, 115, 181, 199, 242, 120, 4, 78, 75, 19, 227, 13, 215, 184,
        108, 226, 53, 111, 149, 179, 84, 137, 121, 79, 1, 160, 223, 124, 241, 202, 203, 220, 237, 50, 242, 57, 158, 226,
        207, 203, 188, 43, 28, 70, 110, 214, 234, 251, 15, 249, 157, 62, 80,
    ]
    leaked_kp = Keypair.from_secret_key(bytes(secret_key))
    return NodeWallet(leaked_kp)


async def find_associated_token_address(wallet_address: PublicKey, token_mint_address: PublicKey) -> PublicKey:
    return (await PublicKey.find_program_address(
        [bytes(wallet_address), bytes(TOKEN_PROGRAM_ID), bytes(token_mint_address)],
        ASSOCIATED_TOKEN_PROGRAM_ID
    ))[0]


async def get_token_balance(pubkey: PublicKey, connection: Client) -> int:
    balance = await connection.get_token_account_balance(pubkey)
    return int(balance['result']['value']['amount'])


def create_associated_token_account_instruction(
    associated_token_address: PublicKey,
    payer: PublicKey,
    wallet_address: PublicKey,
    spl_token_mint_address: PublicKey
) -> List[TransactionInstruction]:
    return [create_associated_token_account(
        payer=payer,
        owner=wallet_address,
        mint=spl_token_mint_address,
        address=associated_token_address
    )]
