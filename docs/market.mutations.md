### Documentation for `hadeswap.market.mutations`

The `hadeswap.market.mutations` module contains functions for performing various mutations on pairs within the Hadeswap platform. These functions allow for creating, modifying, and closing pairs. Here is a detailed overview of each function:

1. **close_virtual_pair**
   - **Purpose**: Closes a virtual pair on the Hadeswap platform.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `pair`: The public key of the pair to be closed.
     - `authority_adapter`: The public key of the authority adapter.
     - `user_pubkey`: The public key of the user performing the action.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Used to close a virtual pair, typically when it is no longer needed or desired by the user.

2. **create_classic_authority_adapter**
   - **Purpose**: Creates a classic authority adapter for a pair.
   - **Parameters**:
     - Similar to `close_virtual_pair`, with the addition of `authority_adapter_kp`, representing the keypair of the authority adapter.
   - **Returns**: None.
   - **Usage**: Essential for setting up a classic authority adapter, which is a key component in managing pairs on the platform.

3. **initialize_pair**
   - **Purpose**: Initializes a new pair on the Hadeswap platform.
   - **Parameters**:
     - `delta`, `spot_price`, `fee`: Numerical values representing the pair's delta, spot price, and fee, respectively.
     - `bonding_curve_type`, `pair_type`: Enums representing the bonding curve and pair type.
     - `hado_market`, `user_pubkey`: Public keys for the Hado market and the user.
     - `pair_kp`: An optional keypair for the pair.
   - **Returns**: None.
   - **Usage**: Used to create a new pair on the platform, setting the initial parameters for trading and liquidity.

4. **modify_pair**
   - **Purpose**: Modifies an existing pair's parameters.
   - **Parameters**:
     - Similar to `initialize_pair`, excluding `pair_kp`.
   - **Returns**: None.
   - **Usage**: Allows users to update the parameters of an existing pair, such as delta, spot price, and fee, to adapt to market changes or strategic decisions.

5. **put_pair_on_market**
   - **Purpose**: Puts an existing pair on the market.
   - **Parameters**:
     - Similar to `close_virtual_pair`.
   - **Returns**: None.
   - **Usage**: Enables users to make their pair available for trading on the Hadeswap platform, an essential step for starting liquidity provision and trading activities.
