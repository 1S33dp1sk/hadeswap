### Documentation for `hadeswap.core.hado`

The `hadeswap.core.hado` module provides a set of functions to manage and interact with Hado markets within the Hadeswap ecosystem. Here's a detailed overview of each function:

1. **validate_nft**
   - **Purpose**: Validates an NFT within the Hado market.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `user_pubkey`: The public key of the user.
     - `classic_validation_whitelist`: The public key of the classic validation whitelist.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.

2. **modify_hado_market**
   - **Purpose**: Modifies the parameters of an existing Hado market.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `user_pubkey`: The public key of the user.
     - `hado_market`: The public key of the Hado market to modify.
     - `validation_adapter_authority`: The public key of the validation adapter authority.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.

3. **initialize_hado_market**
   - **Purpose**: Initializes a new Hado market.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `user_pubkey`: The public key of the user.
     - `validation_adapter_program`: The public key of the validation adapter program.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.

4. **finish_hado_market**
   - **Purpose**: Finalizes the setup of a Hado market.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `user_pubkey`: The public key of the user.
     - `hado_market`: The public key of the Hado market to finalize.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.

5. **create_merkle_tree_whitelist**
   - **Purpose**: Creates a Merkle tree whitelist for a Hado market.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `user_pubkey`: The public key of the user.
     - `hado_market`: The public key of the Hado market.
     - `root`: The root of the Merkle tree.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.

6. **add_classic_whitelist_to_market**
   - **Purpose**: Adds a classic whitelist to a Hado market.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `user_pubkey`: The public key of the user.
     - `hado_market`: The public key of the Hado market.
     - `whitelisted_address`: The public key of the address to be whitelisted.
     - `whitelist_type`: The type of NFT validation whitelist.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
