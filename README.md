
# Hadeswap Python API

The Hadeswap Python API provides a comprehensive set of tools for interacting with the Hadeswap platform on the Solana blockchain. This API allows developers to integrate Hadeswap's functionality into Python applications, enabling operations such as liquidity provision, NFT swaps, and more.

## Core Functionality

The core of the Hadeswap Python API is divided into two main modules: `hadeswap.core` and `hadeswap.market`. Each module contains several sub-modules that provide specific functionalities.

### hadeswap.core

The `hadeswap.core` module contains essential functions for interacting with the Hadeswap platform:

- **accounts.py**: Provides functions to fetch specific accounts, monitor account changes, and parse transaction data for various Hadeswap operations.
- **hado.py**: Contains functions related to Hado market operations, including initializing and modifying Hado markets, as well as validating NFTs.
- **router.py**: Offers routing functionalities, enabling actions such as buying NFTs from pairs, and selling NFTs to liquidity or token-to-NFT pairs.
- **trades.py**: Handles trade-related operations, facilitating the process of executing trades on the Hadeswap platform.

### hadeswap.market

The `hadeswap.market` module includes functions that are specifically designed for managing and interacting with market pairs:

- **admin.py**: Provides administrative functions, such as closing various types of accounts and withdrawing outstanding tokens by an admin.
- **deposits.py**: Facilitates depositing liquidity, NFTs, and SOL to pairs, as well as handling single sell order deposits.
- **mutations.py**: Contains functions for creating and modifying market pairs, including initializing pairs, putting pairs on the market, and closing virtual pairs.
- **withdrawals.py**: Enables withdrawing liquidity, NFTs, SOL, and virtual fees from pairs, covering various withdrawal scenarios including balanced, buy orders only, and sell orders only pairs.


## overview

```sh
hadeswap/
├── _hadeswap_idl.py        # Hadeswap's Interface Description Language (IDL) definitions
├── common.py               # Common utilities and helper functions
├── core/                   # Core functionalities and modules
│   ├── accounts.py         # Functions related to account management
│   ├── hado.py             # Functions related to Hado operations
│   ├── router.py           # Router functions for various operations
│   └── trades.py           # Functions for trade-related operations
├── market/                 # Market-related functionalities and modules
│   ├── admin.py            # Administrative functions for market management
│   ├── deposits.py         # Functions for handling deposits in the market
│   ├── mutations.py        # Mutation functions for market state changes
│   └── withdrawals.py      # Functions for handling withdrawals from the market
├── __init__.py             # Initialization script for the Hadeswap module
└── pyproject.toml          # Project configuration file (TOML format)
```


## Usage

To use the Hadeswap Python API, import the required modules and functions from the hadeswap package. You can then interact with the Hadeswap platform by calling the provided functions with the appropriate parameters.

For more detailed examples and usage instructions, refer to the documentation provided within each module and function.

```python

import asyncio
from hadeswap.market.mutations import initialize_pair
from hadeswap.market.deposits import deposit_sol_to_pair
from hadeswap.core.accounts import get_all_program_accounts
from hadeswap.common import (
    NEW_DEVNET_PROGRAM,  
    load_keypair_from_file, 
    create_fake_wallet,
    BondingCurveType,
    PairType
)

async def main():
    # Load user Keypair
    user_keypair = load_keypair_from_file('keys/admin.json')
    # Create fake wallet for sending transactions
    send_txn = create_fake_wallet()
    # Define connection and program ID
    connection = hadeswap.create_connection('https://api.devnet.solana.com')
    program_id = NEW_DEVNET_PROGRAM
    # Define Hado Market
    hado_market = "Hd2Rx5cEvFojpBFTHeHXfk1tMNrbSKt1dhNK78LCXPqH"
    # Initialize Pair
    await initialize_pair(
        program_id,
        connection,
        {
            "spot_price": 1 * 1e9,
            "delta": 0.2 * 1e9,
            "bonding_curve_type": BondingCurveType.Linear,
            "fee": 0,
            "pair_type": PairType.TokenForNFT
        },
        {
            "hado_market": hado_market,
            "user_pubkey": user_keypair.public_key
        },
        send_txn
    )
    # Get all program accounts to find the authority adapter
    all_accounts = await get_all_program_accounts(program_id, connection)
    pair = "FsE3egxUv3eiLDNLT6m4bu6s72dMTjGfYc4Xhk7Yd9rq"
    authority_adapter = next(account.authority_adapter for account in all_accounts.authority_adapters if account.pair == pair and account.authority_owner == user_keypair.public_key.to_base58())
    # Deposit SOL to Pair
    await deposit_sol_to_pair(
        program_id,
        connection,
        {
            "amount_of_orders": 6
        },
        {
            "pair": pair,
            "authority_adapter": authority_adapter,
            "user_pubkey": user_keypair.public_key
        },
        send_txn
    )

if __name__ == "__main__":
    asyncio.run(main())

```