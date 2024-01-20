import base64
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import AccountMeta, TransactionInstruction, Transaction
from construct import Struct, Int8ul, Int64ul, Padding, PaddedString, Byte, IfThenElse

# Define the structure for a creator entry
Creator = Struct(
    "address" / PaddedString(32, "utf8"),
    "verified" / Int8ul,
    "share" / Int8ul,
)

# Define the structure for the metadata account data
MetadataStruct = Struct(
    Padding(1), # Discard the first byte (discriminator)
    "key" / Byte,
    "update_authority" / PaddedString(32, "utf8"),
    "mint" / PaddedString(32, "utf8"),
    "name_length" / Int8ul,
    "name" / IfThenElse(lambda ctx: ctx.name_length > 0, PaddedString(lambda ctx: ctx.name_length, "utf8"), Padding(0)),
    "symbol_length" / Int8ul,
    "symbol" / IfThenElse(lambda ctx: ctx.symbol_length > 0, PaddedString(lambda ctx: ctx.symbol_length, "utf8"), Padding(0)),
    "uri_length" / Int8ul,
    "uri" / IfThenElse(lambda ctx: ctx.uri_length > 0, PaddedString(lambda ctx: ctx.uri_length, "utf8"), Padding(0)),
    "seller_fee_basis_points" / Int64ul,
    "creator_array_length" / Int8ul,
    "creators" / Creator[this.creator_array_length],
)

class Metadata:
    def __init__(self, key, update_authority, mint, name, symbol, uri, seller_fee_basis_points, creators):
        self.key = key
        self.update_authority = PublicKey(update_authority)
        self.mint = PublicKey(mint)
        self.name = name
        self.symbol = symbol
        self.uri = uri
        self.seller_fee_basis_points = seller_fee_basis_points
        self.creators = [
            {
                "address": PublicKey(creator.address),
                "verified": bool(creator.verified),
                "share": creator.share,
            }
            for creator in creators
        ]

    @staticmethod
    def parse(account_data):
        decoded_data = base64.b64decode(account_data)
        parsed_data = MetadataStruct.parse(decoded_data)

        return Metadata(
            key=parsed_data.key,
            update_authority=parsed_data.update_authority,
            mint=parsed_data.mint,
            name=parsed_data.name,
            symbol=parsed_data.symbol,
            uri=parsed_data.uri,
            seller_fee_basis_points=parsed_data.seller_fee_basis_points,
            creators=parsed_data.creators,
        )

    @staticmethod
    async def from_account_address(connection, account_address):
        """Fetches and parses metadata information of a token from a given account address."""
        program_id = PublicKey("metaqbxxUerdDd1a7Qo8Luv6tqKx1dSC2Vm")  # Metaplex Metadata program ID
        account_pubkey = PublicKey(account_address)

        # Fetch metadata account data
        account_info = await connection.get_account_info(account_pubkey)
        metadata_account = Metadata.parse(account_info['result']['value']['data'][0])

        return metadata_account
