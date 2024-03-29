from solana.rpc.api import Client  # Equivalent to web3.Connection in TypeScript
from solders.pubkey import Pubkey  # Equivalent to web3.Pubkey and @solana/web3.js Pubkey
from solana.transaction import Transaction
from solana.rpc.types import TxOpts  # Transaction options
from solders.keypair import Keypair
from solders.instruction import Instruction

# Define the ReturnAnchorProgram type
# In Python, this could be represented as a function signature using type hints
from typing import Callable
from construct import Struct, Int8ul, Int64ul, Padding, Bytes, Byte, IfThenElse, Array

from anchorpy import Program, Provider
from anchorpy import Idl

from solders.instruction import Instruction
from solders.pubkey import Pubkey
from solders.system_program import (
    create_account, 
    transfer, 
    allocate, 
    assign, 
    create_account_with_seed, 
)

from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple
import base58  # For base58 encoding/decoding

from pathlib import Path

from ._hadeswap_idl import Hadeswap as HadeswapIDL  # Import the IDL dictionary from the specified module
import json


# Define the structure for a creator entry
Creator = Struct(
    "address" / Bytes(32),
    "verified" / Int8ul,
    "share" / Int8ul,
)

# Define the structure for the metadata account data
MetadataStruct = Struct(
    Padding(1),  # Discard the first byte (discriminator)
    "key" / Byte,
    "update_authority" / Bytes(32),
    "mint" / Bytes(32),
    "name_length" / Int8ul,
    "name" / IfThenElse(lambda ctx: ctx.name_length > 0, Bytes(lambda ctx: ctx.name_length), Padding(0)),
    "symbol_length" / Int8ul,
    "symbol" / IfThenElse(lambda ctx: ctx.symbol_length > 0, Bytes(lambda ctx: ctx.symbol_length), Padding(0)),
    "uri_length" / Int8ul,
    "uri" / IfThenElse(lambda ctx: ctx.uri_length > 0, Bytes(lambda ctx: ctx.uri_length), Padding(0)),
    "seller_fee_basis_points" / Int64ul,
    "creator_array_length" / Int8ul,
    "creators" / Array(lambda ctx: ctx.creator_array_length, Creator),
)


@dataclass
class TokenExtensions:
    website: Optional[str] = None
    bridge_contract: Optional[str] = None
    asset_contract: Optional[str] = None
    address: Optional[str] = None
    explorer: Optional[str] = None
    twitter: Optional[str] = None
    github: Optional[str] = None
    medium: Optional[str] = None
    tgann: Optional[str] = None
    tggroup: Optional[str] = None
    discord: Optional[str] = None
    serum_v3_usdt: Optional[str] = None
    serum_v3_usdc: Optional[str] = None
    coingecko_id: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None

@dataclass
class TokenInfo:
    chain_id: int
    address: str
    name: str
    decimals: int
    symbol: str
    logo_uri: Optional[str] = None
    tags: Optional[List[str]] = None
    extensions: Optional[TokenExtensions] = None


@dataclass
class TokenView:
    token_account_pubkey: str
    mint: str
    owner: str
    amount: int
    amount_bn: float
    delegate_option: bool
    delegate: str
    state: int
    is_native_option: bool
    is_native: int
    delegated_amount: int
    close_authority_option: bool
    close_authority: str


class Wallet:
    def __init__(self, public_key):
        self.public_key = public_key

    async def sign_transaction(self, tx: Transaction) -> Transaction:
        raise NotImplementedError

    async def sign_all_transactions(self, txs: List[Transaction]) -> List[Transaction]:
        raise NotImplementedError


class NodeWallet(Wallet):
    def __init__(self, payer: Keypair):
        super().__init__(payer.pubkey())
        self.payer = payer

    async def sign_transaction(self, tx: Transaction) -> Transaction:
        tx.partial_sign(self.payer)
        return tx

    async def sign_all_transactions(self, txs: List[Transaction]) -> List[Transaction]:
        return [self.sign_transaction(tx) for tx in txs]


class BondingCurveType:
    """Enum for Bonding Curve Types."""
    Linear = 'linear'
    Exponential = 'exponential'
    XYK = 'xyk'


class PairType:
    """Enum for Pair Types."""
    TokenForNFT = 'tokenForNft'
    NftForToken = 'nftForToken'
    LiquidityProvision = 'liquidityProvision'


class NftValidationWhitelistType:
    """Enum for NFT Validation Whitelist Types."""
    Creator = 'creator'
    Nft = 'nft'


class OrderType:
    """Enum for Order Types."""
    Buy = 'buy'
    Sell = 'sell'


class SystemProgram:
    @staticmethod
    def create_account(from_pubkey, to_pubkey, lamports, space, owner):
        """Create a new account."""
        return create_account(from_pubkey, to_pubkey, lamports, space, owner)

    @staticmethod
    def transfer(from_pubkey, to_pubkey, lamports):
        """Transfer lamports."""
        return transfer(from_pubkey, to_pubkey, lamports)

    @staticmethod
    def allocate(pubkey, space):
        """Allocate space in an account without funding."""
        return allocate(pubkey, space)

    @staticmethod
    def assign(pubkey, owner):
        """Assign account to a program."""
        return assign(pubkey, owner)

    @staticmethod
    def create_account_with_seed(from_pubkey, to_pubkey, base, seed, lamports, space, owner):
        """Create account with seed."""
        return create_account_with_seed(from_pubkey, to_pubkey, base, seed, lamports, space, owner)



def create_fake_wallet() -> NodeWallet:
    secret_key = [
        208, 175, 150, 242, 88, 34, 108, 88, 177, 16, 168, 75, 115, 181, 199, 242, 120, 4, 78, 75, 19, 227, 13, 215, 184,
        108, 226, 53, 111, 149, 179, 84, 137, 121, 79, 1, 160, 223, 124, 241, 202, 203, 220, 237, 50, 242, 57, 158, 226,
        207, 203, 188, 43, 28, 70, 110, 214, 234, 251, 15, 249, 157, 62, 80,
    ]
    leaked_kp = Keypair.from_secret_key(bytes(secret_key))
    return NodeWallet(leaked_kp)

async def find_associated_token_address(wallet_address: Pubkey, token_mint_address: Pubkey) -> Pubkey:
    return (await Pubkey.find_program_address(
        [bytes(wallet_address), bytes(TOKEN_PROGRAM_ID), bytes(token_mint_address)],
        ASSOCIATED_TOKEN_PROGRAM_ID
    ))[0]

def create_connection(url: str) -> Client:
    """
    Create a connection to the Solana blockchain.

    :param url: URL of the Solana cluster to connect to.
    :return: A Client instance representing the connection.
    """
    return Client(url)

async def get_token_balance(pubkey: Pubkey, connection: Client) -> int:
    balance = await connection.get_token_account_balance(pubkey)
    return int(balance['result']['value']['amount'])

def create_associated_token_account_instruction(
    associated_token_address: Pubkey,
    payer: Pubkey,
    wallet_address: Pubkey,
    spl_token_mint_address: Pubkey
) -> List[Instruction]:
    return [create_associated_token_account(
        payer=payer,
        owner=wallet_address,
        mint=spl_token_mint_address,
        address=associated_token_address
    )]

def Publickey(pubkey_str: str) -> Pubkey:
    """
    Creates a Solana Pubkey object from a base58-encoded string.

    Args:
        pubkey_str (str): The base58-encoded public key string.

    Returns:
        Pubkey: The Pubkey object corresponding to the given string.
    """
    try:
        decoded_bytes = base58.b58decode(pubkey_str)
        if len(decoded_bytes) != 32:
            raise ValueError("Decoded public key bytes must be 32 bytes long.")
        return Pubkey(decoded_bytes)
    except ValueError as e:
        raise ValueError(f"Invalid public key string: {e}")

def load_json_idl(idl_path: str) -> Idl:
    """Load the IDL from the specified file path."""
    with open(idl_path, "r") as idl_file:
        idl_json = idl_file.read()
    return Idl.from_json(idl_json)

def create_fake_wallet():
    """Create a fake wallet (Keypair) for testing purposes."""
    return Keypair()

def create_anchor_provider(connection: Client, wallet) -> Provider:
    """Create an AnchorProvider with the given connection and wallet."""
    return Provider(connection, wallet)

def get_metaplex_edition_pda(mint_pubkey: Pubkey) -> Pubkey:
    # Calculate the edition PDA
    seeds = [
        bytes(METADATA_PREFIX, 'utf-8'),
        METADATA_PROGRAM_PUBKEY.__bytes__(),
        mint_pubkey.__bytes__(),
        bytes(EDITION_PREFIX, 'utf-8'),
    ]
    edition_pda = find_program_address_sync(seeds, METADATA_PROGRAM_PUBKEY)
    return edition_pda[0]

def anchor_raw_BNs_and_pubkeys_to_nums_and_strings(raw_account: dict) -> dict:
    copy_raw_account = raw_account.copy()
    new_account = parse_raw_account(raw_account['account'])
    return {**new_account, 'publicKey': copy_raw_account['publicKey'].to_base58()}

def parse_raw_account(raw_account: dict) -> dict:
    copy_raw_account = raw_account.copy()
    for key in copy_raw_account:
        value = copy_raw_account[key]
        if value is None:
            continue

        if hasattr(value, 'to_number'):
            copy_raw_account[key] = value.to_number()
        elif hasattr(value, 'to_base58'):
            copy_raw_account[key] = value.to_base58()
        elif isinstance(value, dict):
            if len(value) == 1:
                copy_raw_account[key] = next(iter(value.keys()))
            else:
                copy_raw_account[key] = parse_raw_account(value)

    return copy_raw_account

def enum_to_anchor_enum(any_enum: any) -> dict:
    return {any_enum: {}}

def calculate_next_spot_price(order_type, spot_price, delta, bonding_curve_type, counter):
    """
    Calculate the next spot price based on order type, current spot price, delta, bonding curve type, and counter.

    :param order_type: OrderType (Buy/Sell)
    :param spot_price: Current spot price (float)
    :param delta: Delta value (float)
    :param bonding_curve_type: BondingCurveType (Linear/Exponential/XYK)
    :param counter: Current counter value (int)
    :return: Calculated next spot price (float)
    """
    if bonding_curve_type == BondingCurveType.Linear:
        current_price = spot_price
        target_counter = counter + (1 if order_type == OrderType.Buy else -1)

        if target_counter >= 0:
            for _ in range(abs(target_counter)):
                current_price += delta
        else:
            for _ in range(abs(target_counter)):
                current_price -= delta

        return current_price

    elif bonding_curve_type == BondingCurveType.Exponential:
        new_counter = counter + (1 if order_type == OrderType.Buy else -1)
        new_delta = (delta + 1e4) / 1e4 if new_counter > 0 else 1 / ((delta + 1e4) / 1e4)

        return spot_price * (new_delta ** abs(new_counter))

    elif bonding_curve_type == BondingCurveType.XYK:
        nft_tokens_balance = delta * spot_price
        counter_updated = counter if order_type == OrderType.Buy else counter - 1
        current_delta = delta + 1 - counter_updated
        diff_amount = (counter_updated * nft_tokens_balance) / current_delta
        new_nft_tokens_balance = nft_tokens_balance + diff_amount

        return new_nft_tokens_balance / (current_delta - 1 if order_type == OrderType.Buy else current_delta + 1)

    return 0

def derive_xyk_base_spot_price_from_current_spot_price(current_spot_price, delta, counter):
    """
    Derive the base spot price for an XYK bonding curve from the current spot price.

    :param current_spot_price: Current spot price (float)
    :param delta: Delta value (float)
    :param counter: Current counter value (int)
    :return: Derived base spot price (float)
    """
    if delta == 0:
        return current_spot_price

    corrected_counter = counter - 1
    delta_corrected = delta - corrected_counter

    return (current_spot_price * delta_corrected) / (delta + (corrected_counter * delta) / (delta_corrected + 1))

def get_sum_of_orders_series(amount_of_orders, order_type, spot_price, delta, bonding_curve_type, counter):
    """
    Calculate the sum of a series of orders based on order type, initial spot price, delta, bonding curve type, and counter.

    :param amount_of_orders: Number of orders in the series (int)
    :param order_type: OrderType (Buy/Sell)
    :param spot_price: Initial spot price (float)
    :param delta: Delta value (float)
    :param bonding_curve_type: BondingCurveType (Linear/Exponential/XYK)
    :param counter: Initial counter value (int)
    :return: Sum of the series of orders (float)
    """
    series_sum = 0
    current_spot_price = spot_price

    new_counter = counter
    for _ in range(amount_of_orders):
        series_sum += current_spot_price
        current_spot_price = calculate_next_spot_price(
            order_type=order_type,
            spot_price=current_spot_price,
            delta=delta,
            bonding_curve_type=bonding_curve_type,
            counter=new_counter
        )

        new_counter = new_counter + 1 if order_type == OrderType.Buy else new_counter - 1

    return series_sum

def calculate_prices_array(starting_spot_price, delta, amount, bonding_curve_type, order_type, counter):
    """
    Calculate an array of prices and the total sum based on the given parameters.

    :param starting_spot_price: Starting spot price (float)
    :param delta: Delta value (float)
    :param amount: Number of prices to calculate (int)
    :param bonding_curve_type: BondingCurveType (Linear/Exponential/XYK)
    :param order_type: OrderType (Buy/Sell)
    :param counter: Initial counter value (int)
    :return: A dictionary with the array of prices and the total sum
    """
    prices_array = []
    new_counter = counter + 1 if order_type == OrderType.Sell else counter

    for _ in range(amount):
        next_price = calculate_next_spot_price(
            order_type=order_type,
            spot_price=starting_spot_price,
            delta=delta,
            bonding_curve_type=bonding_curve_type,
            counter=new_counter
        )
        prices_array.append(next_price)

        new_counter = new_counter + 1 if order_type == OrderType.Buy else new_counter - 1

    total = sum(prices_array)

    return {'array': prices_array, 'total': total}

async def find_rule_set_pda(payer: Pubkey, name: str) -> Pubkey:
    """
    Asynchronously find the rule set PDA for a given payer public key and name.

    :param payer: Payer public key (Pubkey)
    :param name: Name (str)
    :return: Rule set PDA (Pubkey)
    """
    seeds = [bytes('rule_set', 'utf-8'), payer.__bytes__(), bytes(name, 'utf-8')]
    rule_set_pda, _ = await find_program_address(seeds, AUTHORIZATION_RULES_PROGRAM)
    return rule_set_pda

def find_token_record_pda(mint: Pubkey, token: Pubkey) -> Pubkey:
    """
    Find the token record PDA for a given mint and token public keys.

    :param mint: Mint public key (Pubkey)
    :param token: Token public key (Pubkey)
    :return: Token record PDA (Pubkey)
    """
    seeds = [
        bytes(METADATA_PREFIX, 'utf-8'),
        METADATA_PROGRAM_PUBKEY.__bytes__(),
        mint.__bytes__(),
        bytes(TOKEN_RECORD, 'utf-8'),
        token.__bytes__()
    ]
    token_record_pda, _ = find_program_address_sync(seeds, METADATA_PROGRAM_PUBKEY)
    return token_record_pda

def get_metaplex_metadata(mint_pubkey: Pubkey) -> Pubkey:
    """
    Get the metadata PDA for a given mint public key.

    :param mint_pubkey: Mint public key (Pubkey)
    :return: Metadata PDA (Pubkey)
    """
    seeds = [
        bytes(METADATA_PREFIX, 'utf-8'),
        METADATA_PROGRAM_PUBKEY.__bytes__(),
        mint_pubkey.__bytes__()
    ]
    metadata, _ = find_program_address_sync(seeds, METADATA_PROGRAM_PUBKEY)
    return metadata

# Load Keypair from file
def load_keypair_from_file(file_path):
    with Path(file_path).open(mode="r") as f:
        secret_key = json.load(f)
    return Keypair.from_secret_key(bytes(secret_key))


class Metadata:
    def __init__(self, key, update_authority, mint, name, symbol, uri, seller_fee_basis_points, creators):
        self.key = key
        self.update_authority = Publickey(update_authority)
        self.mint = Publickey(mint)
        self.name = name
        self.symbol = symbol
        self.uri = uri
        self.seller_fee_basis_points = seller_fee_basis_points
        self.creators = [
            {
                "address": Publickey(creator.address),
                "verified": bool(creator.verified),
                "share": creator.share,
            }
            for creator in creators
        ]

    @staticmethod
    def parse(account_data):
        decoded_data = base64.b64decode(account_data)
        parsed_data = MetadataStruct.parse(decoded_data)

        return Metadata(
            key=parsed_data.key,
            update_authority=parsed_data.update_authority,
            mint=parsed_data.mint,
            name=parsed_data.name,
            symbol=parsed_data.symbol,
            uri=parsed_data.uri,
            seller_fee_basis_points=parsed_data.seller_fee_basis_points,
            creators=parsed_data.creators,
        )

    @staticmethod
    async def from_account_address(connection, account_address):
        """Fetches and parses metadata information of a token from a given account address."""
        program_id = Publickey("metaqbxxUerdDd1a7Qo8Luv6tqKx1dSC2Vm")  # Metaplex Metadata program ID
        account_pubkey = Publickey(account_address)

        # Fetch metadata account data
        account_info = await connection.get_account_info(account_pubkey)
        metadata_account = Metadata.parse(account_info['result']['value']['data'][0])

        return metadata_account


Hadeswap_IDL_PATH = "_hadeswap_idl.py"

GetMetaplexEditionPda = Callable[[Pubkey], Pubkey]

# Import necessary modules from solana-py
SYSVAR_RENT_PUBKEY = Publickey("SysvarRent111111111111111111111111111111111")

SYS_PROGRAM_ID = Pubkey(bytes(32))  # 32 zero bytes

# METADATA_PROGRAM_PUBKEY: Pubkey instance for the metadata program
METADATA_PROGRAM_PUBKEY = Publickey('metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s')

# AUTHORIZATION_RULES_PROGRAM: Pubkey instance for the authorization rules program
AUTHORIZATION_RULES_PROGRAM = Publickey("auth9SigNpDKz4sJJ1DfCTuZrZNSAgh9sFD3rboVmgg")

# METADATA_PREFIX: Prefix for metadata
METADATA_PREFIX = 'metadata'

# EDITION_PREFIX: Prefix for edition
EDITION_PREFIX = 'edition'

# FEE_PREFIX: Prefix for the fee vault
FEE_PREFIX = 'fee_vault'

# TOKEN_RECORD: String representing the token record
TOKEN_RECORD = 'token_record'

# SOL_FUNDS_PREFIX: Prefix for the SOL funds vault
SOL_FUNDS_PREFIX = 'sol_funds_vault'

# NFTS_OWNER_PREFIX: Prefix for NFTs owner
NFTS_OWNER_PREFIX = 'nfts_owner'

# EMPTY_PUBKEY: Pubkey instance representing an empty public key
EMPTY_PUBKEY = Publickey('11111111111111111111111111111111')

# ENCODER: TextEncoder instance for encoding text
ENCODER = 'utf-8'  # In Python, specify the encoding directly

# BASE_POINTS: Integer representing the base points
BASE_POINTS = 10000

# Type hint for a function returning an AnchorPy Program instance
ReturnAnchorProgram = Callable[[Pubkey, Client], Program]

NEW_DEVNET_PROGRAM = Publickey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')


__HADESWAP_IDL = '''{
   "version":"0.1.0",
   "name":"hadeswap",
   "instructions":[
      {
         "name":"initializePair",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"hadoMarket",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"pairAuthorityAdapterProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"partialAdapterProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"partialAssetReceiver",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"feeTokenAccount",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"fundsTokenAccount",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"assetReceiver",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"assetReceiverTokenAccount",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"bumps",
               "type":{
                  "defined":"PairBumps"
               }
            },
            {
               "name":"params",
               "type":{
                  "defined":"PairParams"
               }
            },
            {
               "name":"bondingCurveType",
               "type":{
                  "defined":"BondingCurveType"
               }
            },
            {
               "name":"pairType",
               "type":{
                  "defined":"PairType"
               }
            }
         ],
         "returns":null
      },
      {
         "name":"createClassicAuthorityAdapter",
         "accounts":[
            {
               "name":"authorityAdapter",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"depositSolToPair",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"amountOfOrders",
               "type":"u64"
            }
         ],
         "returns":null
      },
      {
         "name":"validateNft",
         "accounts":[
            {
               "name":"nftValidationAdapter",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"validationWhitelist",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"depositNftToPair",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftValidationAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"proof",
               "type":{
                  "vec":{
                     "array":[
                        "u8",
                        32
                     ]
                  }
               }
            },
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"initializeHadoMarket",
         "accounts":[
            {
               "name":"hadoMarket",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"validationAdapterProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"pairTokenMint",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"finishHadoMarket",
         "accounts":[
            {
               "name":"hadoMarket",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"addClassicWhitelistToMarket",
         "accounts":[
            {
               "name":"validationWhitelist",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"hadoMarket",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"whitelistedAddress",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"whitelistType",
               "type":{
                  "defined":"NftValidationWhitelistType"
               }
            }
         ],
         "returns":null
      },
      {
         "name":"depositLiquidityToPair",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftValidationAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"proof",
               "type":{
                  "vec":{
                     "array":[
                        "u8",
                        32
                     ]
                  }
               }
            },
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"putPairOnMarket",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"buyNftFromPair",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultNftTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"assetReceiver",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"protocolFeeReceiver",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"maxAmountToPay",
               "type":"u64"
            },
            {
               "name":"skipFailed",
               "type":"bool"
            },
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"sellNftToTokenToNftPair",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftValidationAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"assetReceiverTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"assetReceiver",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"protocolFeeReceiver",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"minAmountToGet",
               "type":"u64"
            },
            {
               "name":"skipFailed",
               "type":"bool"
            },
            {
               "name":"proof",
               "type":{
                  "vec":{
                     "array":[
                        "u8",
                        32
                     ]
                  }
               }
            },
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"sellNftToLiquidityPair",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftValidationAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"newVaultTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"protocolFeeReceiver",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"minAmountToGet",
               "type":"u64"
            },
            {
               "name":"skipFailed",
               "type":"bool"
            },
            {
               "name":"proof",
               "type":{
                  "vec":{
                     "array":[
                        "u8",
                        32
                     ]
                  }
               }
            },
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"withdrawSolFromPair",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"quantityOfOrders",
               "type":"u64"
            }
         ],
         "returns":null
      },
      {
         "name":"withdrawNftFromPair",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultNftTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"withdrawLiquidityFromBalancedPair",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultNftTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"modifyPair",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"params",
               "type":{
                  "defined":"PairParams"
               }
            }
         ],
         "returns":null
      },
      {
         "name":"withdrawLiquidityFromBuyOrdersPair",
         "accounts":[
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"withdrawLiquidityFromSellOrdersPair",
         "accounts":[
            {
               "name":"nftPairBoxFirst",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftMintFirst",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultNftTokenAccountFirst",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccountFirst",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftPairBoxSecond",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfoFirst",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfoFirst",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecordFirst",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"destTokenRecordFirst",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"editionInfoSecond",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfoSecond",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecordSecond",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"destTokenRecordSecond",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftMintSecond",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultNftTokenAccountSecond",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccountSecond",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"withdrawLiquidityOrderVirtualFees",
         "accounts":[
            {
               "name":"liquidityProvisionOrder",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"closeVirtualNftSwapPair",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"withdrawVirtualFees",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"closeNftPairBox",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"admin",
               "isMut":true,
               "isSigner":true
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"closeLiquidityProvisionOrder",
         "accounts":[
            {
               "name":"liquidityProvisionOrder",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"admin",
               "isMut":true,
               "isSigner":true
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"customValidateNft",
         "accounts":[
            {
               "name":"nftValidationAdapter",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"hadoMarket",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"whitelistedAddress",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"adapterProgramSigner",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"duration",
               "type":"u64"
            },
            {
               "name":"nftValidationWhitelistType",
               "type":{
                  "defined":"NftValidationWhitelistType"
               }
            }
         ],
         "returns":null
      },
      {
         "name":"modifyHadoMarket",
         "accounts":[
            {
               "name":"hadoMarket",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"validationAdapterProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"addMerkleTreeWhitelist",
         "accounts":[
            {
               "name":"nftValidationAdapter",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"hadoMarket",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"root",
               "type":{
                  "array":[
                     "u8",
                     32
                  ]
               }
            }
         ],
         "returns":null
      },
      {
         "name":"closeNftValidationAdapter",
         "accounts":[
            {
               "name":"nftValidationAdapter",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"admin",
               "isMut":true,
               "isSigner":true
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"closeClassicWhitelist",
         "accounts":[
            {
               "name":"validationWhitelist",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"admin",
               "isMut":true,
               "isSigner":true
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"closeNftValidationAdapterV2",
         "accounts":[
            {
               "name":"nftValidationAdapterV2",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"admin",
               "isMut":true,
               "isSigner":true
            }
         ],
         "args":[
            
         ],
         "returns":null
      },
      {
         "name":"withdrawOutstandingTokensByAdmin",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultNftTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"depositLiquidityOnlyBuyOrders",
         "accounts":[
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"quantityOfOrders",
               "type":"u64"
            }
         ],
         "returns":null
      },
      {
         "name":"withdrawLiquidityOnlyBuyOrders",
         "accounts":[
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"quantityOfOrders",
               "type":"u64"
            }
         ],
         "returns":null
      },
      {
         "name":"depositLiquiditySingleSellToPair",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftValidationAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"proof",
               "type":{
                  "vec":{
                     "array":[
                        "u8",
                        32
                     ]
                  }
               }
            },
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      },
      {
         "name":"withdrawLiquiditySingleSellOrder",
         "accounts":[
            {
               "name":"nftPairBox",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftMint",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"vaultNftTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"nftUserTokenAccount",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"authorityAdapter",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"pair",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"user",
               "isMut":true,
               "isSigner":true
            },
            {
               "name":"nftsOwner",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"feeSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"fundsSolVault",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"editionInfo",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataInfo",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"ownerTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"destTokenRecord",
               "isMut":true,
               "isSigner":false
            },
            {
               "name":"instructions",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"authorizationRulesProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"tokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"associatedTokenProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"systemProgram",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"rent",
               "isMut":false,
               "isSigner":false
            },
            {
               "name":"metadataProgram",
               "isMut":false,
               "isSigner":false
            }
         ],
         "args":[
            {
               "name":"authorizationData",
               "type":{
                  "option":{
                     "defined":"AuthorizationDataLocal"
                  }
               }
            }
         ],
         "returns":null
      }
   ],
   "accounts":[
      {
         "name":"adapterWhitelist",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"whitelistedAdapterProgram",
                  "type":"publicKey"
               },
               {
                  "name":"adapterType",
                  "type":{
                     "defined":"AdapterType"
                  }
               }
            ]
         }
      },
      {
         "name":"authorityAdapter",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"pair",
                  "type":"publicKey"
               },
               {
                  "name":"authorityAdapterProgram",
                  "type":"publicKey"
               },
               {
                  "name":"authorityOwner",
                  "type":"publicKey"
               },
               {
                  "name":"authorityType",
                  "type":{
                     "defined":"AuthorityAdapterType"
                  }
               },
               {
                  "name":"expiringAt",
                  "type":"u64"
               },
               {
                  "name":"authorityState",
                  "type":{
                     "defined":"AuthorityState"
                  }
               }
            ]
         }
      },
      {
         "name":"classicValidationWhitelist",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"hadoMarket",
                  "type":"publicKey"
               },
               {
                  "name":"pair",
                  "type":"publicKey"
               },
               {
                  "name":"whitelistType",
                  "type":{
                     "defined":"NftValidationWhitelistType"
                  }
               },
               {
                  "name":"whitelistedAddress",
                  "type":"publicKey"
               }
            ]
         }
      },
      {
         "name":"hadoMarket",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"marketAuthority",
                  "type":"publicKey"
               },
               {
                  "name":"marketState",
                  "type":{
                     "defined":"MarketState"
                  }
               },
               {
                  "name":"marketTrustType",
                  "type":{
                     "defined":"MarketTrustType"
                  }
               },
               {
                  "name":"pairValidationType",
                  "type":{
                     "defined":"PairValidationType"
                  }
               },
               {
                  "name":"validationAdapterProgram",
                  "type":"publicKey"
               },
               {
                  "name":"pairTokenType",
                  "type":{
                     "defined":"PairTokenType"
                  }
               },
               {
                  "name":"pairTokenMint",
                  "type":"publicKey"
               }
            ]
         }
      },
      {
         "name":"liquidityProvisionOrder",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"nftSwapPair",
                  "type":"publicKey"
               },
               {
                  "name":"lpOrderState",
                  "type":{
                     "defined":"LpOrderState"
                  }
               },
               {
                  "name":"orderACounter",
                  "type":"i64"
               },
               {
                  "name":"orderBCounter",
                  "type":"i64"
               },
               {
                  "name":"accumulatedFee",
                  "type":"u64"
               },
               {
                  "name":"lpTokenMint",
                  "type":"publicKey"
               },
               {
                  "name":"liquidityFeeBump",
                  "type":"u8"
               },
               {
                  "name":"createdAt",
                  "type":"u64"
               }
            ]
         }
      },
      {
         "name":"nftPairBox",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"pair",
                  "type":"publicKey"
               },
               {
                  "name":"nftMint",
                  "type":"publicKey"
               },
               {
                  "name":"nftMetadata",
                  "type":"publicKey"
               },
               {
                  "name":"nftBoxType",
                  "type":{
                     "defined":"NftBoxType"
                  }
               },
               {
                  "name":"vaultTokenAccount",
                  "type":"publicKey"
               },
               {
                  "name":"status",
                  "type":{
                     "defined":"NftBoxState"
                  }
               }
            ]
         }
      },
      {
         "name":"nftSwapPair",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"hadoMarket",
                  "type":"publicKey"
               },
               {
                  "name":"pairType",
                  "type":{
                     "defined":"PairType"
                  }
               },
               {
                  "name":"pairState",
                  "type":{
                     "defined":"PairState"
                  }
               },
               {
                  "name":"pairAuthorityType",
                  "type":{
                     "defined":"PairAuthorityType"
                  }
               },
               {
                  "name":"pairAuthorityAdapterProgram",
                  "type":"publicKey"
               },
               {
                  "name":"lpTokensMint",
                  "type":"publicKey"
               },
               {
                  "name":"lpTokensInCirculation",
                  "type":"u64"
               },
               {
                  "name":"bondingCurve",
                  "type":{
                     "defined":"BondingCurve"
                  }
               },
               {
                  "name":"baseSpotPrice",
                  "type":"u64"
               },
               {
                  "name":"fee",
                  "type":"u64"
               },
               {
                  "name":"mathCounter",
                  "type":"i64"
               },
               {
                  "name":"currentSpotPrice",
                  "type":"u64"
               },
               {
                  "name":"feeTokenAccount",
                  "type":"publicKey"
               },
               {
                  "name":"feeVaultSeed",
                  "type":"u8"
               },
               {
                  "name":"solOrTokenFeeAmount",
                  "type":"u64"
               },
               {
                  "name":"fundsTokenAccount",
                  "type":"publicKey"
               },
               {
                  "name":"fundsSolVaultSeed",
                  "type":"u8"
               },
               {
                  "name":"fundsSolOrTokenBalance",
                  "type":"u64"
               },
               {
                  "name":"initialFundsSolOrTokenBalance",
                  "type":"u64"
               },
               {
                  "name":"buyOrdersQuantity",
                  "type":"u64"
               },
               {
                  "name":"nftsSeed",
                  "type":"u8"
               },
               {
                  "name":"nftsCount",
                  "type":"u64"
               },
               {
                  "name":"lastTransactedAt",
                  "type":"u64"
               },
               {
                  "name":"concentrationIndex",
                  "type":"u64"
               },
               {
                  "name":"assetReceiver",
                  "type":"publicKey"
               }
            ]
         }
      },
      {
         "name":"nftValidationAdapterV2",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"hadoMarket",
                  "type":"publicKey"
               },
               {
                  "name":"scopeType",
                  "type":{
                     "defined":"ScopeType"
                  }
               },
               {
                  "name":"pair",
                  "type":"publicKey"
               },
               {
                  "name":"nftValidationProgram",
                  "type":"publicKey"
               },
               {
                  "name":"nftValidationWhitelistType",
                  "type":{
                     "defined":"NftValidationWhitelistTypeV2"
                  }
               },
               {
                  "name":"whitelistedAddress",
                  "type":"publicKey"
               },
               {
                  "name":"root",
                  "type":{
                     "array":[
                        "u8",
                        32
                     ]
                  }
               },
               {
                  "name":"nftValidationDurationType",
                  "type":{
                     "defined":"NftValidationDurationType"
                  }
               },
               {
                  "name":"validUntil",
                  "type":"u64"
               }
            ]
         }
      },
      {
         "name":"nftValidationAdapter",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"hadoMarket",
                  "type":"publicKey"
               },
               {
                  "name":"scopeType",
                  "type":{
                     "defined":"ScopeType"
                  }
               },
               {
                  "name":"pair",
                  "type":"publicKey"
               },
               {
                  "name":"nftValidationProgram",
                  "type":"publicKey"
               },
               {
                  "name":"nftValidationWhitelistType",
                  "type":{
                     "defined":"NftValidationWhitelistType"
                  }
               },
               {
                  "name":"whitelistedAddress",
                  "type":"publicKey"
               },
               {
                  "name":"nftValidationDurationType",
                  "type":{
                     "defined":"NftValidationDurationType"
                  }
               },
               {
                  "name":"validUntil",
                  "type":"u64"
               }
            ]
         }
      },
      {
         "name":"protocolAdminMultisig",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"protocolSettings",
                  "type":"publicKey"
               },
               {
                  "name":"admin",
                  "type":"publicKey"
               },
               {
                  "name":"weight",
                  "type":"u64"
               }
            ]
         }
      },
      {
         "name":"protocolSettingsV1",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"protocolFee",
                  "type":"u64"
               },
               {
                  "name":"protocolFeeMultiplier",
                  "type":"u64"
               },
               {
                  "name":"maxFee",
                  "type":"u64"
               },
               {
                  "name":"protocolFeeReceiver",
                  "type":"publicKey"
               },
               {
                  "name":"adminThresholdAmountMultisig",
                  "type":"u64"
               }
            ]
         }
      }
   ],
   "types":[
      {
         "name":"PairParams",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"delta",
                  "type":"u64"
               },
               {
                  "name":"spotPrice",
                  "type":"u64"
               },
               {
                  "name":"fee",
                  "type":"u64"
               }
            ]
         }
      },
      {
         "name":"PairBumps",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"fundsSolVaultSeed",
                  "type":"u8"
               },
               {
                  "name":"feeVaultSeed",
                  "type":"u8"
               },
               {
                  "name":"nftsSeed",
                  "type":"u8"
               }
            ]
         }
      },
      {
         "name":"BondingCurve",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"delta",
                  "type":"u64"
               },
               {
                  "name":"bondingType",
                  "type":{
                     "defined":"BondingCurveType"
                  }
               }
            ]
         }
      },
      {
         "name":"AuthorizationDataLocal",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"payload",
                  "type":{
                     "vec":{
                        "defined":"TaggedPayload"
                     }
                  }
               }
            ]
         }
      },
      {
         "name":"TaggedPayload",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"name",
                  "type":"string"
               },
               {
                  "name":"payload",
                  "type":{
                     "defined":"PayloadTypeLocal"
                  }
               }
            ]
         }
      },
      {
         "name":"SeedsVecLocal",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"seeds",
                  "type":{
                     "vec":"bytes"
                  }
               }
            ]
         }
      },
      {
         "name":"ProofInfoLocal",
         "type":{
            "kind":"struct",
            "fields":[
               {
                  "name":"proof",
                  "type":{
                     "vec":{
                        "array":[
                           "u8",
                           32
                        ]
                     }
                  }
               }
            ]
         }
      },
      {
         "name":"AdapterType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Validation"
               },
               {
                  "name":"Authority"
               },
               {
                  "name":"Partial"
               }
            ]
         }
      },
      {
         "name":"AuthorityAdapterType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"OneTime"
               },
               {
                  "name":"Persistent"
               }
            ]
         }
      },
      {
         "name":"AuthorityState",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Active"
               },
               {
                  "name":"Used"
               },
               {
                  "name":"Expired"
               },
               {
                  "name":"Revoked"
               }
            ]
         }
      },
      {
         "name":"MarketTrustType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Unverified"
               },
               {
                  "name":"Verified"
               }
            ]
         }
      },
      {
         "name":"MarketState",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Initializing"
               },
               {
                  "name":"Available"
               }
            ]
         }
      },
      {
         "name":"PairValidationType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"ClassicValidation"
               },
               {
                  "name":"CustomValidation"
               }
            ]
         }
      },
      {
         "name":"PairTokenType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"NativeSol"
               },
               {
                  "name":"Spl"
               }
            ]
         }
      },
      {
         "name":"LpOrderState",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Virtual"
               },
               {
                  "name":"Tokenized"
               },
               {
                  "name":"WithdrawnVirtual"
               },
               {
                  "name":"WithdrawnTokenized"
               }
            ]
         }
      },
      {
         "name":"NftBoxState",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Closed"
               },
               {
                  "name":"Active"
               }
            ]
         }
      },
      {
         "name":"NftBoxType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Escrow"
               },
               {
                  "name":"Escrowless"
               }
            ]
         }
      },
      {
         "name":"PairType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"TokenForNft"
               },
               {
                  "name":"NftForToken"
               },
               {
                  "name":"LiquidityProvision"
               }
            ]
         }
      },
      {
         "name":"PairState",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Initializing"
               },
               {
                  "name":"OnMarketVirtual"
               },
               {
                  "name":"OnMarketTokenized"
               },
               {
                  "name":"Frozen"
               }
            ]
         }
      },
      {
         "name":"PairAuthorityType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"ClassicAuthority"
               },
               {
                  "name":"CustomAuthority"
               }
            ]
         }
      },
      {
         "name":"PartialSettings",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"None"
               },
               {
                  "name":"CustomPartial"
               }
            ]
         }
      },
      {
         "name":"BondingCurveType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Linear"
               },
               {
                  "name":"Exponential"
               },
               {
                  "name":"XYK"
               }
            ]
         }
      },
      {
         "name":"NftValidationWhitelistTypeV2",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Creator"
               },
               {
                  "name":"Nft"
               },
               {
                  "name":"MerkleTree"
               }
            ]
         }
      },
      {
         "name":"ScopeType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Market"
               },
               {
                  "name":"Pair"
               }
            ]
         }
      },
      {
         "name":"NftValidationDurationType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Finite"
               },
               {
                  "name":"Infinite"
               }
            ]
         }
      },
      {
         "name":"NftValidationWhitelistType",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Creator"
               },
               {
                  "name":"Nft"
               }
            ]
         }
      },
      {
         "name":"PayloadTypeLocal",
         "type":{
            "kind":"enum",
            "variants":[
               {
                  "name":"Pubkey",
                  "fields":[
                     "publicKey"
                  ]
               },
               {
                  "name":"Seeds",
                  "fields":[
                     {
                        "defined":"SeedsVecLocal"
                     }
                  ]
               },
               {
                  "name":"MerkleProof",
                  "fields":[
                     {
                        "defined":"ProofInfoLocal"
                     }
                  ]
               },
               {
                  "name":"Number",
                  "fields":[
                     "u64"
                  ]
               }
            ]
         }
      }
   ],
   "errors":[
      {
         "code":6000,
         "name":"MetadataDoesntExist",
         "msg":"MetadataDoesntExist"
      },
      {
         "code":6001,
         "name":"DerivedKeyInvalid",
         "msg":"DerivedKeyInvalid"
      },
      {
         "code":6002,
         "name":"InvalidCollectionDetails",
         "msg":"InvalidCollectionDetails"
      },
      {
         "code":6003,
         "name":"InvalidCollection",
         "msg":"InvalidCollection"
      },
      {
         "code":6004,
         "name":"InvalidCollectionMint",
         "msg":"InvalidCollectionMint"
      },
      {
         "code":6005,
         "name":"NftNotVerified",
         "msg":"NftNotVerified"
      },
      {
         "code":6006,
         "name":"InvalidOwner",
         "msg":"InvalidOwner"
      },
      {
         "code":6007,
         "name":"InvalidDelta",
         "msg":"InvalidDelta"
      },
      {
         "code":6008,
         "name":"InvalidFee",
         "msg":"InvalidFee"
      },
      {
         "code":6009,
         "name":"InvalidPairType",
         "msg":"InvalidPairType"
      },
      {
         "code":6010,
         "name":"NotEnoughInTokenAccount",
         "msg":"NotEnoughInTokenAccount"
      },
      {
         "code":6011,
         "name":"InvalidMint",
         "msg":"InvalidMint"
      },
      {
         "code":6012,
         "name":"InvalidSolVault",
         "msg":"InvalidSolVault"
      },
      {
         "code":6013,
         "name":"InvalidFundingAmount",
         "msg":"InvalidFundingAmount"
      },
      {
         "code":6014,
         "name":"NotEnoughLamports",
         "msg":"NotEnoughLamports"
      },
      {
         "code":6015,
         "name":"InvalidJpegOwner",
         "msg":"InvalidJpegOwner"
      },
      {
         "code":6016,
         "name":"InvalidTokenAccount",
         "msg":"InvalidTokenAccount"
      },
      {
         "code":6017,
         "name":"InvalidPayer",
         "msg":"InvalidPayer"
      },
      {
         "code":6018,
         "name":"ShouldBeActive",
         "msg":"ShouldBeActive"
      },
      {
         "code":6019,
         "name":"CantMakeZeroOrders",
         "msg":"Can't make 0 orders"
      },
      {
         "code":6020,
         "name":"OnlyClassicAuthority",
         "msg":"OnlyClassicAuthority"
      },
      {
         "code":6021,
         "name":"NotValidAuthorityAdapter",
         "msg":"NotValidAuthorityAdapter"
      },
      {
         "code":6022,
         "name":"UserDoesntHaveAuthority",
         "msg":"UserDoesntHaveAuthority"
      },
      {
         "code":6023,
         "name":"WrongSeed",
         "msg":"WrongSeed"
      },
      {
         "code":6024,
         "name":"CanDepositSolOnlyToTokenToNft",
         "msg":"CanDepositSolOnlyToTokenToNft"
      },
      {
         "code":6025,
         "name":"MaxAmountOfOrdersSucceeded",
         "msg":"MaxAmountOfOrdersSucceeded"
      },
      {
         "code":6026,
         "name":"CanDepositNftOnlyToNftToToken",
         "msg":"CanDepositNftOnlyToNftToToken"
      },
      {
         "code":6027,
         "name":"TokenAccountDoesntContainNft",
         "msg":"TokenAccountDoesntContainNft"
      },
      {
         "code":6028,
         "name":"MarketAuthorityIncorrect",
         "msg":"MarketAuthorityIncorrect"
      },
      {
         "code":6029,
         "name":"CanAddWhitelistOnlyToInitializingMarket",
         "msg":"CanAddWhitelistOnlyToInitializingMarket"
      },
      {
         "code":6030,
         "name":"CanPutPairsOnlyToAvailableMarkets",
         "msg":"CanPutPairsOnlyToAvailableMarkets"
      },
      {
         "code":6031,
         "name":"PairAndNftValidationMarketDoesntMatch",
         "msg":"PairAndNftValidationMarketDoesntMatch"
      },
      {
         "code":6032,
         "name":"OnlyMarketScopeSupported",
         "msg":"OnlyMarketScopeSupported"
      },
      {
         "code":6033,
         "name":"NotWhitelistedNftForThisMarket",
         "msg":"NotWhitelistedNftForThisMarket"
      },
      {
         "code":6034,
         "name":"CanDepositOnlyToLiquidityProvision",
         "msg":"CanDepositOnlyToLiquidityProvision"
      },
      {
         "code":6035,
         "name":"NftBoxDoesntMatchPair",
         "msg":"NftBoxDoesntMatchPair"
      },
      {
         "code":6036,
         "name":"NftBoxShouldBeActive",
         "msg":"NftBoxShouldBeActive"
      },
      {
         "code":6037,
         "name":"NftBoxDoesntMatchMint",
         "msg":"NftBoxDoesntMatchMint"
      },
      {
         "code":6038,
         "name":"CantBuyNftFromTokenForNft",
         "msg":"CantBuyNftFromTokenForNft"
      },
      {
         "code":6039,
         "name":"OnlyTokenForNftIsEligibleForThisSell",
         "msg":"OnlyTokenForNftIsEligibleForThisSell"
      },
      {
         "code":6040,
         "name":"NoBuyOrdersOnThisPair",
         "msg":"NoBuyOrdersOnThisPair"
      },
      {
         "code":6041,
         "name":"OnlyLiquidityProvisionIsEligibleForThisSell",
         "msg":"OnlyLiquidityProvisionIsEligibleForThisSell"
      },
      {
         "code":6042,
         "name":"OnlyTokenForNftIsEligibleForThisWithdrawal",
         "msg":"OnlyTokenForNftIsEligibleForThisWithdrawal"
      },
      {
         "code":6043,
         "name":"OnlyNftForTokenIsEligibleForThisWithdrawal",
         "msg":"OnlyNftForTokenIsEligibleForThisWithdrawal"
      },
      {
         "code":6044,
         "name":"OnlyLiquidityProvisionIsEligibleForThisWithdrawal",
         "msg":"OnlyLiquidityProvisionIsEligibleForThisWithdrawal"
      },
      {
         "code":6045,
         "name":"InstructionIsNotSupported",
         "msg":"InstructionIsNotSupported"
      },
      {
         "code":6046,
         "name":"CanTradeOnlyWithPairsOnMarket",
         "msg":"CanTradeOnlyWithPairsOnMarket"
      },
      {
         "code":6047,
         "name":"NoLiquidityFeesToWithdraw",
         "msg":"NoLiquidityFeesToWithdraw"
      },
      {
         "code":6048,
         "name":"MaxAmountToPayExceeded",
         "msg":"MaxAmountToPayExceeded"
      },
      {
         "code":6049,
         "name":"GettingLessThanMinAmountToGet",
         "msg":"GettingLessThanMinAmountToGet"
      },
      {
         "code":6050,
         "name":"UserDoesntHaveHadomarketAuthority",
         "msg":"UserDoesntHaveHadomarketAuthority"
      },
      {
         "code":6051,
         "name":"HadomarketAlreadyFinished",
         "msg":"HadomarketAlreadyFinished"
      },
      {
         "code":6052,
         "name":"CanDepositLiqudityOnlyToVirtualOrInitializingPairs",
         "msg":"CanDepositLiqudityOnlyToVirtualOrInitializingPairs"
      },
      {
         "code":6053,
         "name":"CanModifyOnlyToVirtualOrInitializingPairs",
         "msg":"CanModifyOnlyToVirtualOrInitializingPairs"
      },
      {
         "code":6054,
         "name":"LiquidityProvisionOrderPairDoesntMatch",
         "msg":"LiquidityProvisionOrderPairDoesntMatch"
      },
      {
         "code":6055,
         "name":"OnlyVirtualLpOrdersCanBeWithdrawnByThisFunction",
         "msg":"OnlyVirtualLpOrdersCanBeWithdrawnByThisFunction"
      },
      {
         "code":6056,
         "name":"OnlyVirtualOrTokenizedLpOrdersCanBeReplacedByThisFunction",
         "msg":"OnlyVirtualOrTokenizedLpOrdersCanBeReplacedByThisFunction"
      },
      {
         "code":6057,
         "name":"LiquidityProvisionOrderNotEdge",
         "msg":"LiquidityProvisionOrderNotEdge"
      },
      {
         "code":6058,
         "name":"NftPairBoxNotParsingFromRemaining",
         "msg":"NftPairBoxNotParsingFromRemaining"
      },
      {
         "code":6059,
         "name":"VaultNftTokenAccountNotParsingFromRemaining",
         "msg":"VaultNftTokenAccountNotParsingFromRemaining"
      },
      {
         "code":6060,
         "name":"UserTokenAccountNotParsingFromRemaining",
         "msg":"UserTokenAccountNotParsingFromRemaining"
      },
      {
         "code":6061,
         "name":"WithdrawingOnlyAtLeastOneBuyAndOneSellPairs",
         "msg":"WithdrawingOnlyAtLeastOneBuyAndOneSellPairs"
      },
      {
         "code":6062,
         "name":"VaultDoesntMatchBox",
         "msg":"VaultDoesntMatchBox"
      },
      {
         "code":6063,
         "name":"WithdrawingOnlyBuyOrdersPairs",
         "msg":"WithdrawingOnlyBuyOrdersPairs"
      },
      {
         "code":6064,
         "name":"WithdrawingOnlySellOrdersPairs",
         "msg":"WithdrawingOnlySellOrdersPairs"
      },
      {
         "code":6065,
         "name":"LiquidityProvisionOrderIsWithdrawn",
         "msg":"LiquidityProvisionOrderIsWithdrawn"
      },
      {
         "code":6066,
         "name":"LiquidityProvisionOrderIsNotCorrectOrderForPair",
         "msg":"LiquidityProvisionOrderIsNotCorrectOrderForPair"
      },
      {
         "code":6067,
         "name":"OnlyMarketVirtualPairsCanBeTokenized",
         "msg":"OnlyMarketVirtualPairsCanBeTokenized"
      },
      {
         "code":6068,
         "name":"OnlyLiquidityProvisionPairsCanBeTokenized",
         "msg":"OnlyLiquidityProvisionPairsCanBeTokenized"
      },
      {
         "code":6069,
         "name":"OnlyInitializingPairsCanBePutOnMarket",
         "msg":"OnlyInitializingPairsCanBePutOnMarket"
      },
      {
         "code":6070,
         "name":"CanMakeLpOrderTokenizedOnlyFromTokenizedPair",
         "msg":"CanMakeLpOrderTokenizedOnlyFromTokenizedPair"
      },
      {
         "code":6071,
         "name":"OnlyVirtualLpOrderCanBeTokenized",
         "msg":"OnlyVirtualLpOrderCanBeTokenized"
      },
      {
         "code":6072,
         "name":"OnlyTokenizedLpOrdersCanWithdrawFees",
         "msg":"OnlyTokenizedLpOrdersCanWithdrawFees"
      },
      {
         "code":6073,
         "name":"UserLpTokenAccountDoesntContainNft",
         "msg":"UserLpTokenAccountDoesntContainNft"
      },
      {
         "code":6074,
         "name":"OnlyTokenizedLpOrdersCanBeWithdrawnByThisFunction",
         "msg":"OnlyTokenizedLpOrdersCanBeWithdrawnByThisFunction"
      },
      {
         "code":6075,
         "name":"LpTokenMintDoesntMatchOrder",
         "msg":"LpTokenMintDoesntMatchOrder"
      },
      {
         "code":6076,
         "name":"CanCloseVirtualPoolOnlyIfNoLiquidityLeft",
         "msg":"CanCloseVirtualPoolOnlyIfNoLiquidityLeft"
      },
      {
         "code":6077,
         "name":"NftIsNotMasterEdition",
         "msg":"NftIsNotMasterEdition"
      },
      {
         "code":6078,
         "name":"NftPairBoxNotClosed",
         "msg":"NftPairBoxNotClosed"
      },
      {
         "code":6079,
         "name":"WrongAdmin",
         "msg":"WrongAdmin"
      },
      {
         "code":6080,
         "name":"PairScopeValidationNotSupportedForNow",
         "msg":"PairScopeValidationNotSupportedForNow"
      },
      {
         "code":6081,
         "name":"CustomValidationAdapterProgramDoesntMatchUser",
         "msg":"CustomValidationAdapterProgramDoesntMatchUser"
      },
      {
         "code":6082,
         "name":"ClassicAuthorityWorksIfValidationProgramIsHadeswap",
         "msg":"ClassicAuthorityWorksIfValidationProgramIsHadeswap"
      },
      {
         "code":6083,
         "name":"NftValidationAdapterV2CanWhitelistOnlyMerkleTree",
         "msg":"NftValidationAdapterV2CanWhitelistOnlyMerkleTree"
      },
      {
         "code":6084,
         "name":"BadRuleSet",
         "msg":"BadRuleSet"
      },
      {
         "code":6085,
         "name":"WrongCreatorInRemainingAccounts",
         "msg":"WrongCreatorInRemainingAccounts"
      }
   ]
}'''


def return_anchor_program(program_id: Pubkey, connection: Client) -> Program:
    """Create and return an AnchorPy Program instance for the Hadeswap program."""
    fake_wallet = create_fake_wallet()
    provider = create_anchor_provider(connection, fake_wallet)
    return Program(idl=Idl.from_json(__HADESWAP_IDL), program_id=program_id, provider=provider)
