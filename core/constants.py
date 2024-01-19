# Import necessary modules from solana-py
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID

# METADATA_PROGRAM_PUBKEY: PublicKey instance for the metadata program
METADATA_PROGRAM_PUBKEY = PublicKey('metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s')

# AUTHORIZATION_RULES_PROGRAM: PublicKey instance for the authorization rules program
AUTHORIZATION_RULES_PROGRAM = PublicKey("auth9SigNpDKz4sJJ1DfCTuZrZNSAgh9sFD3rboVmgg")

# METADATA_PREFIX: Prefix for metadata
METADATA_PREFIX = 'metadata'

# EDITION_PREFIX: Prefix for edition
EDITION_PREFIX = 'edition'

# FEE_PREFIX: Prefix for the fee vault
FEE_PREFIX = 'fee_vault'

# TOKEN_RECORD: String representing the token record
TOKEN_RECORD = 'token_record'

# SOL_FUNDS_PREFIX: Prefix for the SOL funds vault
SOL_FUNDS_PREFIX = 'sol_funds_vault'

# NFTS_OWNER_PREFIX: Prefix for NFTs owner
NFTS_OWNER_PREFIX = 'nfts_owner'

# EMPTY_PUBKEY: PublicKey instance representing an empty public key
EMPTY_PUBKEY = PublicKey('11111111111111111111111111111111')

# ENCODER: TextEncoder instance for encoding text
ENCODER = 'utf-8'  # In Python, specify the encoding directly

# BASE_POINTS: Integer representing the base points
BASE_POINTS = 10000
