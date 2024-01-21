### Documentation for `hadeswap.market.admin`

The `hadeswap.market.admin` module contains functions used for administrative purposes within the Hadeswap ecosystem. These functions are crucial for managing various aspects of the platform's operation. Below is a comprehensive description of each function:

1. **close_classic_whitelist**
   - **Purpose**: Closes a classic whitelist on the Hadeswap platform.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `validation_whitelist`: The public key of the validation whitelist to be closed.
     - `admin`: The public key of the admin account.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Used by administrators to close a classic whitelist, thereby removing it from active use in the market.

2. **close_liquidity_provision_order**
   - **Purpose**: Closes a liquidity provision order.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `liquidity_provision_order`: The public key of the liquidity provision order to be closed.
     - `admin`: The public key of the admin account.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Enables administrators to close liquidity provision orders, thereby finalizing and settling them.

3. **close_nft_pair_box**
   - **Purpose**: Closes an NFT pair box.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `nft_pair_box`: The public key of the NFT pair box to be closed.
     - `admin`: The public key of the admin account.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Allows administrators to close an NFT pair box, which is part of the process for managing NFT pairs on the platform.

4. **close_nft_validation_adapter**
   - **Purpose**: Closes an NFT validation adapter.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `nft_validation_adapter`: The public key of the NFT validation adapter to be closed.
     - `admin`: The public key of the admin account.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Admins use this function to close NFT validation adapters, which are instrumental in validating NFTs on the marketplace.

5. **close_nft_validation_adapter_v2**
   - **Purpose**: Closes the second version of an NFT validation adapter.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `nft_validation_adapter_v2`: The public key of the NFT validation adapter V2 to be closed.
     - `admin`: The public key of the admin account.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Similar to the previous function, but specifically targets version 2 of the NFT validation adapters.

6. **withdraw_outstanding_tokens_by_admin**
   - **Purpose**: Withdraws outstanding tokens from a pair by an admin.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `pair`: The public key of the pair from which tokens are to be withdrawn.
     - `admin`: The public key of the admin account.
     - `token_mint`: The public key of the token mint.
     - `payer_rule_set`: The public key of the payer rule set.
     - `name_for_rule_set`: The name of the rule set.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Admins can use this function to withdraw tokens that are outstanding in a pair, often as part of management or settlement processes.
