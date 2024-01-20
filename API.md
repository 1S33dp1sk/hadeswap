# Hadeswap Solana Python3 API Documentation

The Hadeswap Solana Python3 API provides a comprehensive set of functionalities for interacting with the Hadeswap protocol on the Solana blockchain. The API is organized into modules and functions, mirroring the structure of the project.


## Core Functions

* Getters

*Functions for retrieving information from the blockchain.*

    get_all_program_accounts: Fetches all program accounts.
    get_specific_accounts: Retrieves specific accounts based on provided criteria.
    on_accounts_change: Subscribes to changes in accounts and triggers callbacks.

* Router

*Functions for routing transactions.*

    buy_nft_from_pair: Buys an NFT from a pair.
    sell_nft_to_token_to_nft_pair: Sells an NFT to a token-to-NFT pair.
    sell_nft_to_liquidity_pair: Sells an NFT to a liquidity pair.

## Market Factory

* HadoMarket

*Functions related to the HadoMarket.*

    validate_nft: Validates an NFT.
    initialize_hado_market: Initializes a HadoMarket.
    finish_hado_market: Finishes a HadoMarket.
    add_classic_whitelist_to_market: Adds a classic whitelist to a market.
    modify_hado_market: Modifies a HadoMarket.
    create_merkle_tree_whitelist: Creates a Merkle Tree whitelist.

* Pair

*Functions related to pairs in the HadoMarket.*

* Virtual

1. Deposits

*Functions for depositing into virtual pairs.*

    deposit_liquidity_to_pair: Deposits liquidity into a pair.
    deposit_liquidity_only_buy_orders_to_pair: Deposits liquidity for only buy orders to a pair.
    deposit_nft_to_pair: Deposits an NFT into a pair.
    deposit_sol_to_pair: Deposits SOL into a pair.
    deposit_liquidity_single_sell_order: Deposits liquidity for a single sell order.

2. Withdrawals

*Functions for withdrawing from virtual pairs.*

    withdraw_liquidity_from_balanced_pair: Withdraws liquidity from a balanced pair.
    withdraw_liquidity_from_buy_orders_pair: Withdraws liquidity from a buy orders pair.
    withdraw_liquidity_from_sell_orders_pair: Withdraws liquidity from a sell orders pair.
    withdraw_liquidity_order_virtual_fees: Withdraws virtual fees from a liquidity order.
    withdraw_nft_from_pair: Withdraws an NFT from a pair.
    withdraw_sol_from_pair: Withdraws SOL from a pair.
    withdraw_virtual_fees: Withdraws virtual fees.
    withdraw_liquidity_only_buy_orders: Withdraws liquidity only from buy orders.
    withdraw_liquidity_single_sell_order: Withdraws liquidity from a single sell order.

3. Mutations

*Functions for mutating virtual pairs.*

    create_classic_authority_adapter: Creates a classic authority adapter.
    initialize_pair: Initializes a pair.
    modify_pair: Modifies a pair.
    put_pair_on_market: Puts a pair on the market.
    close_virtual_pair: Closes a virtual pair.

4. Admin

*Administrative functions for virtual pairs.*

    close_nft_pair_box: Closes an NFT pair box.
    close_liquidity_provision_order: Closes a liquidity provision order.
    close_nft_validation_adapter: Closes an NFT validation adapter.
    close_classic_whitelist: Closes a classic whitelist.
    close_nft_validation_adapter_v2: Closes an NFT validation adapter V2.
    withdraw_outstanding_tokens_by_admin: Withdraws outstanding tokens by an admin.