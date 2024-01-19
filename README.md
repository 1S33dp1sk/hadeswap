# Hadeswap Solana Python SDK

## Overview

This SDK allows you to interact with the Hadeswap protocol on the Solana blockchain using Python. The examples below demonstrate how to create a pool (bid) and deposit funds into the pool to activate the bid. This Python implementation focuses on generating the data payload for transaction instructions.
Installation

Ensure you have Python installed and then add the Hadeswap Solana Python SDK to your project.
Example Usage
Initialize a Pair

```python

import solana
import hadeswap

# Load your user keypair
user_keypair = solana.keypair.load_keypair_from_file('path/to/admin.json')
user_pubkey = user_keypair.public_key

# Specify the program ID and HadoMarket address
program_id = solana.publickey.PublicKey('DFsZgwKM3SvkvMwVRPQhhEnkYZCS1hZ2g2u6ehmAWjyc')
hado_market = solana.publickey.PublicKey('Hd2Rx5cEvFojpBFTHeHXfk1tMNrbSKt1dhNK78LCXPqH')

# Initialize a pair
init_pair_data = hadeswap.functions.market_factory.pair.virtual.mutations.initialize_pair(
    program_id=program_id,
    args={
        'spot_price': 1e9,
        'delta': 0.2e9,
        'bonding_curve_type': hadeswap.types.BondingCurveType.Linear,
        'fee': 0,
        'pair_type': hadeswap.types.PairType.TokenForNFT,
    },
    accounts={
        'hado_market': hado_market,
        'user_pubkey': user_pubkey,
    }
)
```
Deposit SOL to the Pair

```python

# Continue from previous example

# Deposit SOL to the pair
all_accounts = hadeswap.get_all_program_accounts(program_id)
pair = solana.publickey.PublicKey('FsE3egxUv3eiLDNLT6m4bu6s72dMTjGfYc4Xhk7Yd9rq')
authority_adapter = find_authority_adapter(all_accounts, user_pubkey, pair)

deposit_data = hadeswap.functions.market_factory.pair.virtual.deposits.deposit_sol_to_pair(
    program_id=program_id,
    args={'amount_of_orders': 6},
    accounts={
        'pair': pair,
        'authority_adapter': authority_adapter,
        'user_pubkey': user_pubkey,
    }
)
```

## Note: The signing and transmitting of the transaction are not covered in this SDK.

Notes

    The SDK focuses on generating the data payload for transaction instructions.
    The signing and transmitting of the transaction are outside the scope of this SDK.
