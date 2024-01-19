
from solana.keypair import Keypair
from solana.transaction import Transaction
from typing import List


class Wallet:
    def __init__(self, public_key):
        self.public_key = public_key

    async def sign_transaction(self, tx: Transaction) -> Transaction:
        raise NotImplementedError

    async def sign_all_transactions(self, txs: List[Transaction]) -> List[Transaction]:
        raise NotImplementedError


class NodeWallet(Wallet):
    def __init__(self, payer: Keypair):
        super().__init__(payer.public_key)
        self.payer = payer

    async def sign_transaction(self, tx: Transaction) -> Transaction:
        tx.partial_sign(self.payer)
        return tx

    async def sign_all_transactions(self, txs: List[Transaction]) -> List[Transaction]:
        return [self.sign_transaction(tx) for tx in txs]
