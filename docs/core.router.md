### Documentation for `hadeswap.core.router`

The `hadeswap.core.router` module provides essential functions for interacting with different pair types within the Hadeswap ecosystem. These functions facilitate the buying and selling of NFTs through various liquidity and token pairs. Here's a detailed overview of each function:

1. **buy_nft_from_pair**
   - **Purpose**: Executes a transaction to buy an NFT from a pair.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `args`: A dictionary containing transaction arguments.
     - `accounts`: A dictionary containing account public keys relevant to the transaction.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Facilitates the purchase of NFTs from a specific pair on the Hadeswap platform.

2. **sell_nft_to_liquidity_pair**
   - **Purpose**: Executes a transaction to sell an NFT to a liquidity pair.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `args`: A dictionary containing transaction arguments, including details about the NFT and sale conditions.
     - `accounts`: A dictionary containing account public keys relevant to the transaction.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Enables users to sell their NFTs to liquidity pairs, providing liquidity and earning rewards.

3. **sell_nft_to_token_to_nft_pair**
   - **Purpose**: Executes a transaction to sell an NFT to a token-to-NFT pair.
   - **Parameters**:
     - `program_id`: The public key of the program.
     - `connection`: The connection to the Solana blockchain.
     - `args`: A dictionary containing transaction arguments, including details about the NFT and sale conditions.
     - `accounts`: A dictionary containing account public keys relevant to the transaction.
     - `send_txn`: A function to send the transaction.
   - **Returns**: None.
   - **Usage**: Allows users to trade their NFTs for tokens through a specific token-to-NFT pair, facilitating asset exchange on the platform.
