from dataclasses import dataclass
from typing import Optional, List
from decimal import Decimal


@dataclass
class TokenExtensions:
    website: Optional[str] = None
    bridge_contract: Optional[str] = None
    asset_contract: Optional[str] = None
    address: Optional[str] = None
    explorer: Optional[str] = None
    twitter: Optional[str] = None
    github: Optional[str] = None
    medium: Optional[str] = None
    tgann: Optional[str] = None
    tggroup: Optional[str] = None
    discord: Optional[str] = None
    serum_v3_usdt: Optional[str] = None
    serum_v3_usdc: Optional[str] = None
    coingecko_id: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None


@dataclass
class TokenInfo:
    chain_id: int
    address: str
    name: str
    decimals: int
    symbol: str
    logo_uri: Optional[str] = None
    tags: Optional[List[str]] = None
    extensions: Optional[TokenExtensions] = None


@dataclass
class TokenView:
    token_account_pubkey: str
    mint: str
    owner: str
    amount: int
    amount_bn: Decimal
    delegate_option: bool
    delegate: str
    state: int
    is_native_option: bool
    is_native: int
    delegated_amount: int
    close_authority_option: bool
    close_authority: str
