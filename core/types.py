

class BondingCurveType:
    """Enum for Bonding Curve Types."""
    Linear = 'linear'
    Exponential = 'exponential'
    XYK = 'xyk'


class PairType:
    """Enum for Pair Types."""
    TokenForNFT = 'tokenForNft'
    NftForToken = 'nftForToken'
    LiquidityProvision = 'liquidityProvision'


class NftValidationWhitelistType:
    """Enum for NFT Validation Whitelist Types."""
    Creator = 'creator'
    Nft = 'nft'


class OrderType:
    """Enum for Order Types."""
    Buy = 'buy'
    Sell = 'sell'
