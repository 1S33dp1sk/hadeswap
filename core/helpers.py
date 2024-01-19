from solana.rpc.api import Client  # Equivalent to web3.Connection in TypeScript
from solana.publickey import PublicKey  # Equivalent to web3.PublicKey and @solana/web3.js PublicKey
from solana.system_program import SYS_PROGRAM_ID  # Equivalent to some utilities in web3
from solana.transaction import Transaction
from solana.rpc.types import TxOpts  # Transaction options
import base58  # For base58 encoding/decoding

# Import your custom modules (assuming they are translated to Python)
from .idl.hadeswap import Hadeswap, IDL  # Replace with actual Python module path
from .constants import (
    BASE_POINTS, EDITION_PREFIX, METADATA_PREFIX, METADATA_PROGRAM_PUBKEY, TOKEN_RECORD
)
from .types import BondingCurveType, OrderType
from .utils import create_fake_wallet  # Assuming createFakeWallet is converted to create_fake_wallet

# Define the AUTHORIZATION_RULES_PROGRAM constant
AUTHORIZATION_RULES_PROGRAM = PublicKey('auth9SigNpDKz4sJJ1DfCTuZrZNSAgh9sFD3rboVmgg')

# Define the ReturnAnchorProgram type
# In Python, this could be represented as a function signature using type hints
from typing import Callable
from solana.program import Program  # Assuming a similar Program class exists in solana-py or your custom implementation

ReturnAnchorProgram = Callable[[PublicKey, Client], Program[Hadeswap]]  # Replace with actual type if Hadeswap is a custom type

GetMetaplexEditionPda = Callable[[PublicKey], PublicKey]


def return_anchor_program(program_id: PublicKey, connection: Client) -> Program[Hadeswap]:
    # Create and return a new Program instance
    # Note: The actual implementation will depend on your translation of the Program class and AnchorProvider
    anchor_provider = AnchorProvider(connection, create_fake_wallet(), ANCHOR_PROVIDER_DEFAULT_OPTIONS)
    return Program[Hadeswap](IDL, program_id, anchor_provider)



def get_metaplex_edition_pda(mint_pubkey: PublicKey) -> PublicKey:
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


def enum_to_anchor_enum(any_enum: Any) -> dict:
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





async def find_rule_set_pda(payer: PublicKey, name: str) -> PublicKey:
    """
    Asynchronously find the rule set PDA for a given payer public key and name.

    :param payer: Payer public key (PublicKey)
    :param name: Name (str)
    :return: Rule set PDA (PublicKey)
    """
    seeds = [bytes('rule_set', 'utf-8'), payer.__bytes__(), bytes(name, 'utf-8')]
    rule_set_pda, _ = await find_program_address(seeds, AUTHORIZATION_RULES_PROGRAM)
    return rule_set_pda



def find_token_record_pda(mint: PublicKey, token: PublicKey) -> PublicKey:
    """
    Find the token record PDA for a given mint and token public keys.

    :param mint: Mint public key (PublicKey)
    :param token: Token public key (PublicKey)
    :return: Token record PDA (PublicKey)
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


def get_metaplex_metadata(mint_pubkey: PublicKey) -> PublicKey:
    """
    Get the metadata PDA for a given mint public key.

    :param mint_pubkey: Mint public key (PublicKey)
    :return: Metadata PDA (PublicKey)
    """
    seeds = [
        bytes(METADATA_PREFIX, 'utf-8'),
        METADATA_PROGRAM_PUBKEY.__bytes__(),
        mint_pubkey.__bytes__()
    ]
    metadata, _ = find_program_address_sync(seeds, METADATA_PROGRAM_PUBKEY)
    return metadata
