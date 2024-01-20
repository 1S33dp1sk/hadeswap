# Importing necessary Python libraries
import base64
import time
import requests
from solana.rpc.api import Client
from solana.publickey import PublicKey

# Importing the hadeswap package and its components
from hadeswap import utils, helpers
from hadeswap.core import get_all_program_accounts, calculate_prices_array
from hadeswap.types import BondingCurveType, OrderType, PairType
import hadeswap
import anchor

# Importing additional dependencies
from hadeswap.common import find_associated_token_address
# Metaplex import if needed (Python equivalent if available)

# Setting the test timeout duration
# Note: Python's testing framework uses a different mechanism to set timeouts

# Define connection to Solana networks
mainnet_url = 'https://polished-fragrant-dawn.solana-mainnet.quiknode.pro/8005e8943672dd7c0a751fe88526a6cca7954072/'
devnet_url = 'https://api.devnet.solana.com'
mainnet_connection = Client(mainnet_url)
devnet_connection = Client(devnet_url)

# Define program public keys
NEW_DEVNET_PROGRAM = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')
MAINNET_PROGRAM = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')



# Importing the test functions
# from test_module import test_initialize_market_and_add_to_whitelist_and_close
# from test_module import get_specific_accounts_script
# from test_module import get_all_program_accounts_script
# from test_module import create_classic_authority_adapter_script
# from test_module import finalize_hado_market_script
# from test_module import add_to_whitelist_to_market_script
# from test_module import create_token_to_nft_pair_script
# from test_module import add_sol_deposit_to_token_to_nft_pair_script
# from test_module import create_nft_to_token_pair_script
# from test_module import put_pair_on_market_script
# from test_module import create_nft_validation_adapter
# from test_module import deposit_nft_to_pair_script
# from test_module import deposit_liquidity_script
# from test_module import test_buy_orders_series_sum
# from test_module import test_next_spot_price
# from test_module import test_viktors_next_spot_price
# from test_module import create_liquidity_pair_script
# from test_module import get_market_data
# from test_module import test_cart_manager_cross_pair_rebalancing
# from test_module import test_cart_manager_sell_orders
# from test_module import test_cart_manager_buy_and_sell_orders
# from test_module import initialize_hado_market_script
# from test_module import modify_pair_script
# from test_module import test_calculate_prices_array
# from test_module import get_starting_spot_price_by_current_and_delta
# from test_module import get_activity_script
# from test_module import get_trade_activities_by_signatures_script
# from test_module import test_whitelist_script
# from test_module import is_nft_frozen

async def run_tests():
    # await test_initialize_market_and_add_to_whitelist_and_close()
    # await get_specific_accounts_script()
    # await get_all_program_accounts_script()
    # await create_classic_authority_adapter_script()
    # await finalize_hado_market_script()
    # await add_to_whitelist_to_market_script()
    # await create_token_to_nft_pair_script()
    # await add_sol_deposit_to_token_to_nft_pair_script()
    # await create_nft_to_token_pair_script()
    # await put_pair_on_market_script()
    # await create_nft_validation_adapter()
    # await deposit_nft_to_pair_script()
    # await deposit_liquidity_script()
    # test_buy_orders_series_sum()
    # test_next_spot_price()
    # test_viktors_next_spot_price()
    # await create_liquidity_pair_script()
    # await get_market_data()
    # await test_cart_manager_cross_pair_rebalancing()
    # await test_cart_manager_sell_orders()
    # await test_cart_manager_buy_and_sell_orders()
    # await initialize_hado_market_script()
    # await modify_pair_script()
    # test_calculate_prices_array()
    # get_starting_spot_price_by_current_and_delta()
    # await get_activity_script()
    # await get_trade_activities_by_signatures_script()
    await test_whitelist_script()
    # await is_nft_frozen()


async def test_whitelist_script():
    # Define the constants
    MAINNET_PROGRAM = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')
    devnet_connection = ...  # Initialize the connection to the devnet (replace with actual connection initialization)

    # Load the frakt whitelists from a JSON file
    file_path = os.path.join(os.path.dirname(__file__), 'whitelist.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        frakt_whitelists = json.load(file)

    all_accounts = await hadeswap.get_all_program_accounts(MAINNET_PROGRAM, devnet_connection)
    validation_whitelists = all_accounts['classic_validation_whitelists']

    metaplex = MetaplexAPI(devnet_connection)

    count = 0
    not_valid_markets = []
    frakt_name = 'Taiyo Infants/Incubators'
    hado_market = '941QWBMH3WS23T8zYxqE88ZNVAQSisdh4G2DCG34LCQ2'
    validation_entry = next((v for v in validation_whitelists if v['hado_market'] == hado_market), None)

    if not validation_entry:
        return

    print('Validation entry:', validation_entry)

    frakt_entry = next((f for f in frakt_whitelists if f['name'] == frakt_name), None)
    if not frakt_entry:
        return

    nfts_by_creator = []
    position = 1
    while position < 3:
        print(f'Fetching nftsByCreator {position} ...')
        nfts_by_creator += await metaplex.nfts().find_all_by_creator(validation_entry['whitelisted_address'], position)
        position += 1

    nfts_by_creator = [nft for nft in nfts_by_creator if any(
        creator['address'] == validation_entry['whitelisted_address'] and creator['verified']
        for creator in nft['creators']
    )]

    print('NFTs by creator:', len(nfts_by_creator))

    not_whitelisted = [nft for nft in nfts_by_creator if nft['mint_address'] not in frakt_entry['whitelisted_mints']]
    if not_whitelisted:
        not_valid_markets.append(validation_entry)
        # Write to file (not_valid_markets.json)
        file_path = os.path.join(os.path.dirname(__file__), 'not_valid_markets.json')
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(not_valid_markets, file)
        print('This market is not whitelisted properly:', validation_entry)


async def deposit_liquidity_script():
    # Load user keypair from file
    user_keypair = load_keypair_from_file(os.path.join(os.path.dirname(__file__), 'keys/admin.json'))

    # Define the function to send transactions
    async def send_txn_user_devnet(txn, signers):
        try:
            await devnet_connection.send_transaction(txn, [user_keypair] + signers)
        except Exception as err:
            print(err)

    program_id = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')  # NEW_DEVNET_PROGRAM

    # Initialize the Solana RPC client
    devnet_connection = Client('https://api.devnet.solana.com')

    # Get all program accounts
    all_accounts = await hadeswap.get_all_program_accounts(program_id, devnet_connection)

    # Find the pair and authority adapter
    pair = PublicKey('NxoovcU7NEdVWJuYi8NnuLxJobrEtFYxMUxkU9Vw4Wy')
    pair_account = next(acc for acc in all_accounts['nft_swap_pairs'] if acc['public_key'] == pair)
    hado_market = PublicKey(pair_account['hado_market'])
    authority_adapter = next(
        (acc for acc in all_accounts['authority_adapters']
         if acc['authority_owner'] == user_keypair.public_key and acc['pair'] == pair),
        None
    )['public_key']

    # Find the NFT validation adapter
    nft_validation_adapter = next(
        (acc for acc in all_accounts['nft_validation_adapters'] if acc['hado_market'] == hado_market),
        None
    )['public_key']
    
    nft_mint = PublicKey('jRCcvxuoM1B6U94j5p5e93sjmcP8roKvjPfNC4C4YLf')

    # Deposit liquidity to pair
    await hadeswap.functions.market_factory.pair.virtual.deposits.deposit_liquidity_to_pair(
        program_id,
        devnet_connection,
        {
            'nft_validation_adapter': nft_validation_adapter,
            'nft_mint': nft_mint,
            'pair': pair,
            'authority_adapter': authority_adapter,
            'user_pubkey': user_keypair.public_key,
        },
        send_txn_user_devnet
    )

async def put_pair_on_market_script():
    # Load user keypair from file
    user_keypair = load_keypair_from_file(os.path.join(os.path.dirname(__file__), 'keys/admin.json'))

    # Define the function to send transactions
    async def send_txn_user_devnet(txn, signers):
        try:
            await mainnet_connection.send_transaction(txn, [user_keypair] + signers)
        except Exception as err:
            print(err)

    program_id = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')  # MAINNET_PROGRAM

    # Initialize the Solana RPC client
    mainnet_connection = Client('https://api.mainnet-beta.solana.com')

    # Get all program accounts
    all_accounts = await hadeswap.get_all_program_accounts(program_id, mainnet_connection)

    # Find the pair and authority adapter
    pair = PublicKey('NxoovcU7NEdVWJuYi8NnuLxJobrEtFYxMUxkU9Vw4Wy')
    authority_adapter = next(
        (acc for acc in all_accounts['authority_adapters']
         if acc['authority_owner'] == user_keypair.public_key and acc['pair'] == pair),
        None
    )['public_key']

    # Put the pair on the market
    await hadeswap.functions.market_factory.pair.virtual.mutations.put_pair_on_market(
        program_id,
        mainnet_connection,
        {
            'pair': pair,
            'authority_adapter': authority_adapter,
            'user_pubkey': user_keypair.public_key,
        },
        send_txn_user_devnet
    )




async def create_liquidity_pair_script():
    # Load user keypair from file
    user_keypair = load_keypair_from_file(os.path.join(os.path.dirname(__file__), 'keys/admin.json'))

    # Define the function to send transactions
    async def send_txn_user_devnet(txn, signers):
        try:
            await devnet_connection.send_transaction(txn, [user_keypair] + signers)
        except Exception as err:
            print(err)

    program_id = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')  # NEW_DEVNET_PROGRAM

    # Initialize the Solana RPC client
    devnet_connection = Client('https://api.devnet.solana.com')

    # Define hadoMarket
    hado_market = PublicKey('Hd2Rx5cEvFojpBFTHeHXfk1tMNrbSKt1dhNK78LCXPqH')

    # Initialize pair
    await hadeswap.functions.market_factory.pair.virtual.mutations.initialize_pair(
        program_id,
        devnet_connection,
        {
            'spot_price': int(1 * 1e9),
            'delta': int(0.2 * 1e9),
            'bonding_curve_type': hadeswap.types.BondingCurveType.LINEAR,
            'fee': 0,
            'pair_type': hadeswap.types.PairType.LIQUIDITY_PROVISION,
        },
        {
            'hado_market': hado_market,
            'user_pubkey': user_keypair.public_key,
        },
        send_txn_user_devnet
    )





async def initialize_hado_market_script():
    # Load user keypair from file
    user_keypair = load_keypair_from_file(os.path.join(os.path.dirname(__file__), 'keys/production_admin.json'))

    # Define the function to send transactions
    async def send_txn_user_devnet(txn, signers):
        try:
            await devnet_connection.send_transaction(txn, [user_keypair] + signers)
        except Exception as err:
            print(err)

    program_id = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')  # MAINNET_PROGRAM

    # Initialize the Solana RPC client
    devnet_connection = Client('https://api.devnet.solana.com')

    # Initialize Hado Market
    hado_market = await hadeswap.functions.market_factory.hado_market.initialize_hado_market(
        program_id,
        devnet_connection,
        {
            'user_pubkey': user_keypair.public_key,
        },
        send_txn_user_devnet,
    )

    print('hadoMarket: ', hado_market['account'].to_base58())

async def get_specific_accounts_script():
    program_id = PublicKey('DFsZgwKM3SvkvMwVRPQhhEnkYZCS1hZ2g2u6ehmAWjyc')

    # Initialize the Solana RPC client
    devnet_connection = Client('https://api.devnet.solana.com')

    # Get specific accounts
    all_accounts = await hadeswap.functions.getters.get_specific_accounts(
        'nftSwapPair',
        program_id,
        devnet_connection
    )
    print('allAccounts: ', all_accounts)

async def create_nft_validation_adapter():
    # Load user keypair from file
    user_keypair = load_keypair_from_file(os.path.join(os.path.dirname(__file__), 'keys/production_admin.json'))

    # Define the function to send transactions
    async def send_txn_user_devnet(txn, signers):
        try:
            await devnet_connection.send_transaction(txn, [user_keypair] + signers)
        except Exception as err:
            print(err)

    program_id = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')  # MAINNET_PROGRAM
    classic_validation_whitelist = PublicKey('3YeRHNoxSvYkVrcghbybkG2CtqysnrVhDxSNVcyTEUPs')

    # Initialize the Solana RPC client
    devnet_connection = Client('https://api.devnet.solana.com')

    # Validate NFT
    await hadeswap.functions.market_factory.hado_market.validate_nft(
        program_id,
        devnet_connection,
        {
            'classic_validation_whitelist': classic_validation_whitelist,
            'user_pubkey': user_keypair.public_key,
        },
        send_txn_user_devnet,
    )

async def add_sol_deposit_to_token_to_nft_pair_script():
    # Load user keypair from file
    user_keypair = load_keypair_from_file(os.path.join(os.path.dirname(__file__), 'keys/admin.json'))

    # Define the function to send transactions
    async def send_txn_user_devnet(txn, signers):
        try:
            await devnet_connection.send_transaction(txn, [user_keypair] + signers)
        except Exception as err:
            print(err)

    program_id = PublicKey('DFsZgwKM3SvkvMwVRPQhhEnkYZCS1hZ2g2u6ehmAWjyc')

    # Initialize the Solana RPC client
    devnet_connection = Client('https://api.devnet.solana.com')

    pair = PublicKey('FsE3egxUv3eiLDNLT6m4bu6s72dMTjGfYc4Xhk7Yd9rq')
    # Retrieve authority adapters here (mocked as 'authority_adapter' for demonstration)
    # authority_adapter = ...

    # Deposit SOL to Pair
    await hadeswap.functions.market_factory.pair.virtual.deposits.deposit_sol_to_pair(
        program_id,
        devnet_connection,
        {
            'amount_of_orders': 6,
        },
        {
            'pair': pair,
            'authority_adapter': authority_adapter,
            'user_pubkey': user_keypair.public_key,
        },
        send_txn_user_devnet,
    )


async def create_nft_to_token_pair_script():
    # Load user keypair from file
    user_keypair = load_keypair_from_file(os.path.join(os.path.dirname(__file__), 'keys/admin.json'))

    # Define the function to send transactions
    async def send_txn_user_devnet(txn, signers):
        try:
            await devnet_connection.send_transaction(txn, [user_keypair] + signers)
        except Exception as err:
            print(err)

    program_id = PublicKey('DFsZgwKM3SvkvMwVRPQhhEnkYZCS1hZ2g2u6ehmAWjyc')
    hado_market = PublicKey('4iJDy7TMzev2qtgrrdZtL3DmEivoY3MPVdebEw3zfkDA')

    # Initialize the Solana RPC client
    devnet_connection = Client('https://api.devnet.solana.com')

    # Initialize NFT to Token Pair
    await hadeswap.functions.market_factory.pair.virtual.mutations.initialize_pair(
        program_id,
        devnet_connection,
        {
            'spot_price': 2.2 * 1e9,
            'delta': 0.2 * 1e9,
            'bonding_curve_type': hadeswap.types.BondingCurveType.Linear,
            'fee': 0,
            'pair_type': hadeswap.types.PairType.NftForToken,
        },
        {
            'hado_market': hado_market,
            'user_pubkey': user_keypair.public_key,
        },
        send_txn_user_devnet,
    )



async def create_classic_authority_adapter_script():
    # Load user keypair from file
    user_keypair = load_keypair_from_file(os.path.join(os.path.dirname(__file__), 'keys/admin.json'))

    # Define the function to send transactions
    async def send_txn_user_devnet(txn, signers):
        try:
            await devnet_connection.send_transaction(txn, [user_keypair] + signers)
        except Exception as err:
            print(err)

    program_id = PublicKey('hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu')  # NEW_DEVNET_PROGRAM
    pair = PublicKey('NxoovcU7NEdVWJuYi8NnuLxJobrEtFYxMUxkU9Vw4Wy')

    # Initialize the Solana RPC client
    devnet_connection = Client('https://api.devnet.solana.com')

    # Create Classic Authority Adapter
    await hadeswap.functions.market_factory.pair.virtual.mutations.create_classic_authority_adapter(
        program_id,
        devnet_connection,
        {
            'pair': pair,
            'user_pubkey': user_keypair.public_key,
        },
        send_txn_user_devnet,
    )



























































































































































