### Documentation for `hadeswap.market.withdrawals`

The `hadeswap.market.withdrawals` module provides functions for executing various types of withdrawal operations on the Hadeswap platform. These functions allow users to withdraw liquidity, NFTs, SOL, and virtual fees from pairs. Below is an overview of each function:

1. **withdraw_liquidity_from_balanced_pair**
   - **Purpose**: Withdraws liquidity from a balanced pair.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `args`: Additional arguments specific to the withdrawal operation.
     - `accounts`: Dictionary of account public keys involved in the transaction.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Enables users to withdraw their liquidity from a pair that has both buy and sell orders, returning the assets to their wallets.

2. **withdraw_liquidity_from_buy_orders_pair**
   - **Purpose**: Withdraws liquidity from a pair with only buy orders.
   - **Parameters**:
     - Similar to `withdraw_liquidity_from_balanced_pair`, excluding `args`.
   - **Returns**: None.
   - **Usage**: Used when a user wants to withdraw liquidity from a pair that only has buy orders active.

3. **withdraw_liquidity_from_sell_orders_pair**
   - **Purpose**: Withdraws liquidity from a pair with only sell orders.
   - **Parameters**:
     - Similar to `withdraw_liquidity_from_buy_orders_pair`.
   - **Returns**: None.
   - **Usage**: Useful for users who wish to retrieve their assets from a pair that only has sell orders active.

4. **withdraw_liquidity_only_buy_orders**
   - **Purpose**: Withdraws liquidity from a pair with only buy orders based on the specified amount.
   - **Parameters**:
     - Similar to `withdraw_liquidity_from_balanced_pair`.
   - **Returns**: None.
   - **Usage**: Allows precise withdrawal of liquidity based on the number of buy orders, providing more control to the user.

5. **withdraw_liquidity_order_virtual_fees**
   - **Purpose**: Withdraws virtual fees associated with a liquidity provision order.
   - **Parameters**:
     - Similar to `withdraw_liquidity_from_buy_orders_pair`.
   - **Returns**: None.
   - **Usage**: Enables users to claim the virtual fees they have earned from providing liquidity in the form of orders.

6. **withdraw_liquidity_single_sell_order**
   - **Purpose**: Withdraws liquidity from a single sell order.
   - **Parameters**:
     - Similar to `withdraw_liquidity_from_balanced_pair`.
   - **Returns**: None.
   - **Usage**: Allows users to withdraw assets from a specific sell order, providing flexibility in managing their liquidity positions.

7. **withdraw_nft_from_pair**
   - **Purpose**: Withdraws an NFT from a pair.
   - **Parameters**:
     - Similar to `withdraw_liquidity_from_balanced_pair`.
   - **Returns**: None.
   - **Usage**: Facilitates the retrieval of NFTs from a pair, returning them to the user's wallet.

8. **withdraw_sol_from_pair**
   - **Purpose**: Withdraws SOL from a pair.
   - **Parameters**:
     - Similar to `withdraw_liquidity_from_balanced_pair`.
   - **Returns**: None.
   - **Usage**: Enables users to withdraw SOL from a pair, providing access to their funds in SOL.

9. **withdraw_virtual_fees**
   - **Purpose**: Withdraws virtual fees from a pair.
   - **Parameters**:
     - Similar to `withdraw_liquidity_from_buy_orders_pair`.
   - **Returns**: None.
   - **Usage**: Allows users to claim the virtual fees they have earned from their participation in the pair, in terms of trading and liquidity provision.
