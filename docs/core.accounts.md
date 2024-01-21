* get_specific_accounts(account_id: str, program_id: Pubkey, connection: Client)
        Retrieves specific accounts based on the given account identifier within a program.

* get_all_program_accounts(program_id: Pubkey, connection: Client)
        Fetches all accounts associated with a given program ID.

* on_accounts_change(program_id: Pubkey, timeout_of_calls: int, from_this_signature: str, connection: Client, on_accounts_change_callback)
        Subscribes to account changes for a specific program, triggering a callback function on changes.

* initialize_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to initializing a trading pair in Hadeswap.

* validate_nft_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to validating an NFT within the Hadeswap platform.

* create_classic_authority_adapter_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to creating a classic authority adapter in Hadeswap.

* deposit_sol_to_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to depositing SOL to a trading pair.

* deposit_nft_to_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to depositing an NFT to a trading pair.

* initialize_hado_market_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to initializing a Hado market.

* finish_hado_market_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to finishing a Hado market operation.

* add_classic_whitelist_to_market_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to adding a classic whitelist to the market.

* deposit_liquidity_to_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to depositing liquidity to a trading pair.

* put_pair_on_market_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to putting a trading pair on the market.

* buy_nft_from_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to buying an NFT from a trading pair.

* sell_nft_to_token_to_nft_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to selling an NFT to a Token-to-NFT trading pair.

* sell_nft_to_liquidity_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to selling an NFT to a liquidity pair.

* withdraw_sol_from_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to withdrawing SOL from a trading pair.

* withdraw_nft_from_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to withdrawing an NFT from a trading pair.

* withdraw_liquidity_from_balanced_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to withdrawing liquidity from a balanced trading pair.

* modify_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to modifying a trading pair's parameters.

* withdraw_liquidity_from_buy_orders_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to withdrawing liquidity from a pair with only buy orders.

* withdraw_liquidity_from_sell_orders_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to withdrawing liquidity from a pair with only sell orders.

* withdraw_liquidity_order_virtual_fees_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to withdrawing virtual fees from a liquidity provision order.

* close_virtual_nft_swap_pair_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to closing a virtual NFT swap pair.

* withdraw_virtual_fees_parser(transaction, program_id: Pubkey, connection: Client)
        Parses a transaction related to withdrawing virtual fees.