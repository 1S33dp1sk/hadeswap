import asyncio
from solana.rpc.api import Client
from solana.publickey import PublicKey

from .helpers import return_anchor_program, anchor_raw_BNs_and_pubkeys_to_nums_and_strings

async def initialize_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def validate_nft_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    nft_validation_adapter_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    nft_validation_adapter_account = await program.account.nftValidationAdapter.fetch(nft_validation_adapter_pubkey)
    nft_validation_adapter = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': nft_validation_adapter_account, 'publicKey': nft_validation_adapter_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [nft_validation_adapter],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def create_classic_authority_adapter_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    authority_adapter_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    authority_adapter_account = await program.account.authorityAdapter.fetch(authority_adapter_pubkey)
    authority_adapter = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': authority_adapter_account, 'publicKey': authority_adapter_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [authority_adapter],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def deposit_sol_to_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [],
        'nftPairBoxes': [pair],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def deposit_nft_to_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    nft_pair_box_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    nft_pair_box_account = await program.account.nftPairBox.fetch(nft_pair_box_pubkey)
    nft_pair_box = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': nft_pair_box_account, 'publicKey': nft_pair_box_pubkey})

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][1])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [nft_pair_box],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def initialize_hado_market_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    hado_market_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    hado_market_account = await program.account.hadoMarket.fetch(hado_market_pubkey)
    hado_market = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': hado_market_account, 'publicKey': hado_market_pubkey})

    return {
        'hadoMarkets': [hado_market],
        'nftSwapPairs': [],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def finish_hado_market_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    hado_market_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    hado_market_account = await program.account.hadoMarket.fetch(hado_market_pubkey)
    hado_market = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': hado_market_account, 'publicKey': hado_market_pubkey})

    return {
        'hadoMarkets': [hado_market],
        'nftSwapPairs': [],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def add_classic_whitelist_to_market_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    classic_validation_whitelist_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    classic_validation_whitelist_account = await program.account.classicValidationWhitelist.fetch(classic_validation_whitelist_pubkey)
    classic_validation_whitelist = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': classic_validation_whitelist_account, 'publicKey': classic_validation_whitelist_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [classic_validation_whitelist],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def deposit_liquidity_to_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    liquidity_provision_order_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    liquidity_provision_order_account = await program.account.liquidityProvisionOrder.fetch(liquidity_provision_order_pubkey)
    liquidity_provision_order = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': liquidity_provision_order_account, 'publicKey': liquidity_provision_order_pubkey})

    nft_pair_box_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][1])
    nft_pair_box_account = await program.account.nftPairBox.fetch(nft_pair_box_pubkey)
    nft_pair_box = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': nft_pair_box_account, 'publicKey': nft_pair_box_pubkey})

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][2])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [nft_pair_box],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [liquidity_provision_order],
    }

async def put_pair_on_market_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def buy_nft_from_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    nft_pair_box_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    nft_pair_box_account = await program.account.nftPairBox.fetch(nft_pair_box_pubkey)
    nft_pair_box = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': nft_pair_box_account, 'publicKey': nft_pair_box_pubkey})

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][1])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [nft_pair_box],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def sell_nft_to_token_to_nft_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def sell_nft_to_liquidity_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    nft_pair_box_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    nft_pair_box_account = await program.account.nftPairBox.fetch(nft_pair_box_pubkey)
    nft_pair_box = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': nft_pair_box_account, 'publicKey': nft_pair_box_pubkey})

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][1])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [nft_pair_box],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def withdraw_sol_from_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def withdraw_nft_from_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    nft_pair_box_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    nft_pair_box_account = await program.account.nftPairBox.fetch(nft_pair_box_pubkey)
    nft_pair_box = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': nft_pair_box_account, 'publicKey': nft_pair_box_pubkey})

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][2])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [nft_pair_box],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def withdraw_liquidity_from_balanced_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][4])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    liquidity_provision_order_pubkey_first = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    liquidity_provision_order_first_account = await program.account.liquidityProvisionOrder.fetch(liquidity_provision_order_pubkey_first)
    liquidity_provision_order_first = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': liquidity_provision_order_first_account, 'publicKey': liquidity_provision_order_pubkey_first})

    liquidity_provision_order_pubkey_second = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][1])
    liquidity_provision_order_second_account = await program.account.liquidityProvisionOrder.fetch(liquidity_provision_order_pubkey_second)
    liquidity_provision_order_second = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': liquidity_provision_order_second_account, 'publicKey': liquidity_provision_order_pubkey_second})

    nft_pair_box_pubkey_first = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][2])

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [{'publicKey': str(nft_pair_box_pubkey_first)}],  # Convert PublicKey to string
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [liquidity_provision_order_first, liquidity_provision_order_second],
    }

async def modify_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def withdraw_liquidity_from_buy_orders_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][3])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    liquidity_provision_order_pubkey_first = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    liquidity_provision_order_first_account = await program.account.liquidityProvisionOrder.fetch(liquidity_provision_order_pubkey_first)
    liquidity_provision_order_first = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': liquidity_provision_order_first_account, 'publicKey': liquidity_provision_order_pubkey_first})

    liquidity_provision_order_pubkey_second = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][1])
    liquidity_provision_order_second_account = await program.account.liquidityProvisionOrder.fetch(liquidity_provision_order_pubkey_second)
    liquidity_provision_order_second = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': liquidity_provision_order_second_account, 'publicKey': liquidity_provision_order_pubkey_second})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [liquidity_provision_order_first, liquidity_provision_order_second],
    }

async def withdraw_liquidity_from_sell_orders_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][11])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    liquidity_provision_order_pubkey_first = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    liquidity_provision_order_first_account = await program.account.liquidityProvisionOrder.fetch(liquidity_provision_order_pubkey_first)
    liquidity_provision_order_first = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': liquidity_provision_order_first_account, 'publicKey': liquidity_provision_order_pubkey_first})

    liquidity_provision_order_pubkey_second = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][1])
    liquidity_provision_order_second_account = await program.account.liquidityProvisionOrder.fetch(liquidity_provision_order_pubkey_second)
    liquidity_provision_order_second = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': liquidity_provision_order_second_account, 'publicKey': liquidity_provision_order_pubkey_second})

    nft_pair_box_pubkey_first = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][2])
    nft_pair_box_first_account = await program.account.nftPairBox.fetch(nft_pair_box_pubkey_first)
    nft_pair_box_first = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': nft_pair_box_first_account, 'publicKey': nft_pair_box_pubkey_first})

    nft_pair_box_pubkey_second = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][3])
    nft_pair_box_second_account = await program.account.nftPairBox.fetch(nft_pair_box_pubkey_second)
    nft_pair_box_second = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': nft_pair_box_second_account, 'publicKey': nft_pair_box_pubkey_second})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [nft_pair_box_first, nft_pair_box_second],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [liquidity_provision_order_first, liquidity_provision_order_second],
    }

async def withdraw_liquidity_order_virtual_fees_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    liquidity_provision_order_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    liquidity_provision_order_account = await program.account.liquidityProvisionOrder.fetch(liquidity_provision_order_pubkey)
    liquidity_provision_order = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': liquidity_provision_order_account, 'publicKey': liquidity_provision_order_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [liquidity_provision_order],
    }

async def close_virtual_nft_swap_pair_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    # No need to fetch data from the program as the transaction is closing the pair

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [],
        'nftPairBoxes': [{'publicKey': str(pair_pubkey)}],  # Convert PublicKey to string
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

async def withdraw_virtual_fees_parser(transaction, program_id: PublicKey, connection: Client):
    await asyncio.sleep(0.15)
    program = await return_anchor_program(program_id, connection)

    pair_pubkey = PublicKey(transaction['transaction']['message']['instructions'][0]['accounts'][0])
    pair_account = await program.account.nftSwapPair.fetch(pair_pubkey)
    pair = anchor_raw_BNs_and_pubkeys_to_nums_and_strings({'account': pair_account, 'publicKey': pair_pubkey})

    return {
        'hadoMarkets': [],
        'nftSwapPairs': [pair],
        'nftPairBoxes': [],
        'classicValidationWhitelists': [],
        'nftValidationAdapters': [],
        'authorityAdapters': [],
        'adapterWhitelists': [],
        'protocolSettingsV1': [],
        'protocolAdminMultisigs': [],
        'liquidityProvisionOrders': [],
    }

# Define other parsers following the same pattern

TRANSACTION_ACCOUNT_PARSERS = {
    'Program log: Instruction: InitializePair': initialize_pair_parser,
    'Program log: Instruction: ValidateNft': validate_nft_parser,
    'Program log: Instruction: CreateClassicAuthorityAdapter': create_classic_authority_adapter_parser,
    'Program log: Instruction: DepositSolToPair': deposit_sol_to_pair_parser,
    'Program log: Instruction: DepositNftToPair': deposit_nft_to_pair_parser,
    'Program log: Instruction: InitializeHadoMarket': initialize_hado_market_parser,
    'Program log: Instruction: FinishHadoMarket': finish_hado_market_parser,
    'Program log: Instruction: AddClassicWhitelistToMarket': add_classic_whitelist_to_market_parser,
    'Program log: Instruction: DepositLiquidityToPair': deposit_liquidity_to_pair_parser,
    'Program log: Instruction: PutPairOnMarket': put_pair_on_market_parser,
    'Program log: Instruction: BuyNftFromPair': buy_nft_from_pair_parser,
    'Program log: Instruction: SellNftToTokenToNftPair': sell_nft_to_token_to_nft_pair_parser,
    'Program log: Instruction: SellNftToLiquidityPair': sell_nft_to_liquidity_pair_parser,
    'Program log: Instruction: WithdrawSolFromPair': withdraw_sol_from_pair_parser,
    'Program log: Instruction: WithdrawNftFromPair': withdraw_nft_from_pair_parser,
    'Program log: Instruction: WithdrawLiquidityFromBalancedPair': withdraw_liquidity_from_balanced_pair_parser,
    'Program log: Instruction: ModifyPair': modify_pair_parser,
    'Program log: Instruction: WithdrawLiquidityFromBuyOrdersPair': withdraw_liquidity_from_buy_orders_pair_parser,
    'Program log: Instruction: WithdrawLiquidityFromSellOrdersPair': withdraw_liquidity_from_sell_orders_pair_parser,
    'Program log: Instruction: WithdrawLiquidityOrderVirtualFees': withdraw_liquidity_order_virtual_fees_parser,
    'Program log: Instruction: CloseVirtualNftSwapPair': close_virtual_nft_swap_pair_parser,
    'Program log: Instruction: WithdrawVirtualFees': withdraw_virtual_fees_parser,
    # Add other parsers here
}
