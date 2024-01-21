### Documentation for `hadeswap.market.deposits`

The `hadeswap.market.deposits` module provides functions essential for depositing liquidity and assets into pairs on the Hadeswap platform. Here's a detailed description of each function in the module:

1. **deposit_liquidity_only_buy_orders_to_pair**
   - **Purpose**: Deposits liquidity specifically for buy orders into a pair.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `pair`: The public key of the pair for deposit.
     - `authority_adapter`: The public key of the authority adapter.
     - `user_pubkey`: The public key of the user making the deposit.
     - `amount_of_orders`: The amount of liquidity/orders to deposit.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: This function is used when a user wants to deposit liquidity that will only be used for buy orders on the platform.

2. **deposit_liquidity_single_sell_order**
   - **Purpose**: Deposits liquidity for a single sell order into a pair.
   - **Parameters**:
     - Similar to `deposit_liquidity_only_buy_orders_to_pair`, with the addition of `nft_mint` and `nft_validation_adapter` parameters.
     - `proof`: A list of proofs for the deposit.
   - **Returns**: None.
   - **Usage**: Ideal for users looking to deposit liquidity specifically for a single sell order in a pair.

3. **deposit_liquidity_to_pair**
   - **Purpose**: Deposits liquidity into a pair.
   - **Parameters**:
     - Similar to `deposit_liquidity_single_sell_order`.
   - **Returns**: None.
   - **Usage**: More general than the specific buy or sell order functions, this function allows users to deposit liquidity into a pair without specifying the order type.

4. **deposit_nft_to_pair**
   - **Purpose**: Deposits an NFT into a pair.
   - **Parameters**:
     - `args`: A dictionary containing specific arguments for the deposit.
     - `accounts`: A dictionary containing account information required for the deposit.
   - **Returns**: None.
   - **Usage**: Used for depositing NFTs into a pair, crucial for NFT-related transactions on the platform.

5. **deposit_sol_to_pair**
   - **Purpose**: Deposits SOL (the native cryptocurrency of Solana) into a pair.
   - **Parameters**:
     - Similar to `deposit_liquidity_only_buy_orders_to_pair`, without the `nft_mint` and `nft_validation_adapter` parameters.
   - **Returns**: None.
   - **Usage**: Allows users to deposit SOL into a pair, increasing liquidity and enabling further trading activities.
