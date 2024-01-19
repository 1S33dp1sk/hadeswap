
import asyncio
from solana.rpc.api import Client
from solana.publickey import PublicKey


class TradeActivity:
    """
    Represents a trade activity.

    Attributes:
        timestamp (int): Timestamp of the trade activity.
        signature (str): Signature of the transaction.
        pair (str): Identifier of the trading pair.
        order_type (OrderType): Type of the order (Buy/Sell).
        pair_type (PairType): Type of the trading pair.
        nft_mint (str): Mint address of the NFT.
        sol_amount (float): Amount of SOL involved in the trade.
        user_maker (str): Address of the maker user (optional).
        user_taker (str): Address of the taker user.
    """
    def __init__(self, timestamp, signature, pair, order_type, pair_type, nft_mint, sol_amount, user_maker, user_taker):
        self.timestamp = timestamp
        self.signature = signature
        self.pair = pair
        self.order_type = order_type
        self.pair_type = pair_type
        self.nft_mint = nft_mint
        self.sol_amount = sol_amount
        self.user_maker = user_maker
        self.user_taker = user_taker


class TradeInstruction:
    """
    Enum for trade instructions.

    Attributes:
        BuyNftFromPair (str): Instruction log for buying an NFT from a pair.
        SellNftToTokenToNftPair (str): Instruction log for selling an NFT to a token-to-NFT pair.
        SellNftToLiquidityPair (str): Instruction log for selling an NFT to a liquidity pair.
    """
    BuyNftFromPair = 'Program log: Instruction: BuyNftFromPair'
    SellNftToTokenToNftPair = 'Program log: Instruction: SellNftToTokenToNftPair'
    SellNftToLiquidityPair = 'Program log: Instruction: SellNftToLiquidityPair'


class InnerProgramTypes:
    """Enum for inner program types."""
    System = 'system'
    SplToken = 'spl-token'

class InnerInstructionTypes:
    """Enum for inner instruction types."""
    Transfer = 'transfer'



def get_transfer_amount_from_inner_instructions(inner_instruction):
    """
    Get the total transfer amount from inner instructions.

    :param inner_instruction: Parsed inner instruction (dict)
    :return: Total transfer amount in lamports (int)
    """
    transfer_amount = 0
    for instruction in inner_instruction.get('instructions', []):
        if instruction.get('program') == InnerProgramTypes.System and \
           instruction.get('parsed', {}).get('type') == InnerInstructionTypes.Transfer:
            transfer_amount += instruction['parsed']['info']['lamports']

    return transfer_amount


async def get_trade_activities(program_id, from_this_signature=None, until_this_signature=None, limit=None, connection: Client = None):
    """
    Fetch and process trade activities from a Solana program.

    :param program_id: Program public key (PublicKey)
    :param from_this_signature: Start fetching from this signature (optional, str)
    :param until_this_signature: Fetch until this signature (optional, str)
    :param limit: Limit the number of results (optional, int)
    :param connection: Solana RPC connection (Client)
    :return: List of all trade activities (list)
    """
    LIMIT = 100
    all_signatures_infos = []
    current_last_signature_info = (await connection.get_confirmed_signatures_for_address2(
        program_id, {'limit': 1}, 'confirmed'))[0]
    current_last_signature = current_last_signature_info['signature']

    new_signature_infos_latest_to_past = await connection.get_confirmed_signatures_for_address2(
        program_id,
        {'limit': LIMIT, 'before': from_this_signature or current_last_signature, 'until': until_this_signature},
        'confirmed')

    if new_signature_infos_latest_to_past:
        current_last_signature = new_signature_infos_latest_to_past[-1]['signature']

    all_signatures_infos.extend(new_signature_infos_latest_to_past)
    all_signatures_infos.append(current_last_signature_info)
    all_signatures_infos = [info for info in all_signatures_infos if not info['err']]

    while len(new_signature_infos_latest_to_past) == LIMIT:
        new_signature_infos_latest_to_past = await connection.get_confirmed_signatures_for_address2(
            program_id,
            {'limit': LIMIT, 'before': current_last_signature, 'until': until_this_signature},
            'confirmed')

        if new_signature_infos_latest_to_past:
            current_last_signature = new_signature_infos_latest_to_past[-1]['signature']

        all_signatures_infos.extend(new_signature_infos_latest_to_past)
        all_signatures_infos = [info for info in all_signatures_infos if not info['err']]

        if limit is not None and len(all_signatures_infos) >= limit:
            break

    trade_transactions = await get_trade_transactions_from_signatures(
        signatures=[info['signature'] for info in all_signatures_infos if info],
        connection=connection)

    all_trade_activities = []
    for trade_txn in trade_transactions:
        trade_activities = await parse_transaction_info_to_trade_activities(trade_txn, connection, program_id)
        all_trade_activities.extend(trade_activities)

    return all_trade_activities


async def get_trade_activities_by_signatures(signatures, connection, program_id):
    """
    Fetch and process trade activities by signatures.

    :param signatures: List of transaction signatures (list of str)
    :param connection: Solana RPC connection (Client)
    :param program_id: Program public key (PublicKey)
    :return: List of all trade activities (list)
    """
    trade_transactions = await get_trade_transactions_from_signatures(signatures, connection)

    all_trade_activities = []
    for trade_txn in trade_transactions:
        trade_activities = await parse_transaction_info_to_trade_activities(trade_txn, connection, program_id)
        all_trade_activities.extend(trade_activities)

    return all_trade_activities



async def get_trade_transactions_from_signatures(signatures, connection):
    """
    Fetch trade transactions from signatures.

    :param signatures: List of transaction signatures (list of str)
    :param connection: Solana RPC connection (Client)
    :return: List of parsed transactions with metadata (list)
    """
    trade_transactions = []

    for signature in signatures:
        try:
            current_transaction_info = await connection.get_parsed_transaction(signature, 'confirmed')

            if (not current_transaction_info or
                not current_transaction_info['meta'] or
                current_transaction_info['meta'].get('err') is not None or
                not is_trade_transaction_info(current_transaction_info)):
                continue

            trade_transactions.append(current_transaction_info)

        except Exception as err:
            print(err)

    return trade_transactions



def is_trade_transaction_info(current_transaction_info):
    """
    Determine if the transaction info is related to a trade.

    :param current_transaction_info: Parsed transaction with metadata (dict)
    :return: True if it's a trade transaction, False otherwise (bool)
    """
    log_messages = current_transaction_info['meta'].get('logMessages', [])
    return any(is_trade_instruction_log(log) for log in log_messages)


def is_trade_instruction_log(log_message):
    """
    Determine if the log message indicates a trade instruction.

    :param log_message: Log message (str)
    :return: True if it's a trade instruction log, False otherwise (bool)
    """
    # Implement the logic to identify trade instruction logs
    # This depends on the specific log format and criteria for trade transactions
    return 'trade instruction' in log_message  # Placeholder, replace with actual criteria


async def parse_transaction_info_to_trade_activities(trade_txn, connection, program_id):
    """
    Parse transaction info to trade activities.

    :param trade_txn: Parsed transaction with metadata (dict)
    :param connection: Solana RPC connection (Client)
    :param program_id: Program public key (PublicKey)
    :return: List of trade activities (list)
    """
    trade_logs = [log for log in trade_txn['meta'].get('logMessages', []) if is_trade_instruction_log(log)]

    inner_instructions = trade_txn['meta'].get('innerInstructions', [])
    program_instructions = [ix for ix in trade_txn['transaction']['message']['instructions']
                            if (ix['programId'] != 'ComputeBudget111111111111111111111111111111' and
                                ix['programId'] == program_id.to_base58())]

    trade_activities = []

    for i in range(len(inner_instructions)):
        current_inner_instruction = inner_instructions[i]
        current_program_instruction = program_instructions[i]
        current_log = trade_logs[i]

        current_signature = trade_txn['transaction']['signatures'][0]
        block_time = trade_txn.get('blockTime')

        if current_log not in TRADE_TRANSACTION_PARSERS:
            continue
        parsed_trade_activity = await TRADE_TRANSACTION_PARSERS[current_log](
            inner_instruction=current_inner_instruction,
            program_instruction=current_program_instruction,
            signature=current_signature,
            block_time=block_time,
            connection=connection
        )

        if parsed_trade_activity:
            trade_activities.append(parsed_trade_activity)

    return trade_activities


def is_trade_instruction_log(log):
    """
    Determine if the log message is a trade instruction log.

    :param log: Log message (str)
    :return: True if it's a trade instruction log, False otherwise (bool)
    """
    # Replace with actual trade instruction log checks
    return log in [TradeInstruction.BuyNftFromPair, TradeInstruction.SellNftToTokenToNftPair, TradeInstruction.SellNftToLiquidityPair]


TRADE_TRANSACTION_PARSERS = {
    TradeInstruction.BuyNftFromPair: parse_buy_nft_from_pair,
    TradeInstruction.SellNftToTokenToNftPair: parse_sell_nft_to_token_to_nft_pair,
    TradeInstruction.SellNftToLiquidityPair: parse_sell_nft_to_liquidity_pair
}

async def parse_buy_nft_from_pair(inner_instruction, program_instruction, signature, block_time, connection):
    sol_amount = get_transfer_amount_from_inner_instructions(inner_instruction)
    order_type = OrderType.Buy
    pair = program_instruction['accounts'][1]
    user_taker = program_instruction['accounts'][2]
    user_maker = program_instruction['accounts'][9]
    nft_mint = program_instruction['accounts'][6]

    return TradeActivity(
        timestamp=block_time,
        signature=signature,
        pair=pair.to_base58() if pair else '',
        order_type=order_type,
        pair_type=None,
        nft_mint=nft_mint.to_base58() if nft_mint else '',
        sol_amount=sol_amount,
        user_maker=user_maker.to_base58() if user_maker else '',
        user_taker=user_taker.to_base58() if user_taker else ''
    )

async def parse_sell_nft_to_token_to_nft_pair(inner_instruction, program_instruction, signature, block_time, connection):
    sol_amount = get_transfer_amount_from_inner_instructions(inner_instruction)
    order_type = OrderType.Sell
    pair = program_instruction['accounts'][0]
    user_taker = program_instruction['accounts'][2]
    user_maker = program_instruction['accounts'][7]
    nft_mint = program_instruction['accounts'][3]

    return TradeActivity(
        timestamp=block_time,
        signature=signature,
        pair=pair.to_base58() if pair else '',
        order_type=order_type,
        pair_type=PairType.TokenForNFT,
        nft_mint=nft_mint.to_base58() if nft_mint else '',
        sol_amount=sol_amount,
        user_maker=user_maker.to_base58() if user_maker else '',
        user_taker=user_taker.to_base58() if user_taker else ''
    )

async def parse_sell_nft_to_liquidity_pair(inner_instruction, program_instruction, signature, block_time, connection):
    sol_amount = get_transfer_amount_from_inner_instructions(inner_instruction)
    order_type = OrderType.Sell
    pair = program_instruction['accounts'][1]
    user_taker = program_instruction['accounts'][3]
    nft_mint = program_instruction['accounts'][4]

    return TradeActivity(
        timestamp=block_time,
        signature=signature,
        pair=pair.to_base58() if pair else '',
        order_type=order_type,
        pair_type=PairType.LiquidityProvision,
        nft_mint=nft_mint.to_base58() if nft_mint else '',
        sol_amount=sol_amount,
        user_maker=None,
        user_taker=user_taker.to_base58() if user_taker else ''
    )
