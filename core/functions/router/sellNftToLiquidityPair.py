# Solana-py imports for Solana blockchain interaction
from solana.publickey import PublicKey
from solana.transaction import AccountMeta
from solana.rpc.api import Client
from solana.system_program import SYS_PROGRAM_ID
from solana.sysvar import SYSVAR_RENT_PUBKEY, SYSVAR_INSTRUCTIONS_PUBKEY

# Importing constants from the constants module
from hadeswap.constants import (
    EMPTY_PUBKEY, ENCODER, NFTS_OWNER_PREFIX, METADATA_PROGRAM_PUBKEY,
    SOL_FUNDS_PREFIX, FEE_PREFIX, AUTHORIZATION_RULES_PROGRAM
)

# Importing helper functions from the helpers module
from hadeswap.helpers import (
    anchor_raw_BNs_and_pubkeys_to_nums_and_strings, find_rule_set_pda,
    find_token_record_pda, get_metaplex_edition_pda,
    get_metaplex_metadata_pda, return_anchor_program
)

# Imports for associated and token program IDs, assuming they are defined in your Python project
from hadeswap.utils import ASSOCIATED_PROGRAM_ID, TOKEN_PROGRAM_ID

# Importing the find_associated_token_address function
from hadeswap.common import find_associated_token_address

# For Metaplex's Metadata, assuming a Python equivalent is implemented in your project
from hadeswap.mpl_token_metadata import Metadata


from typing import Callable, Optional, List, Tuple, Dict
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction, TransactionInstruction
from solana.keypair import Keypair

async def sell_nft_to_liquidity_pair(
    program_id: PublicKey,
    connection: Client,
    args: Dict[str, any],
    accounts: Dict[str, PublicKey],
    send_txn: Callable[[Transaction, List[Keypair]], None]
) -> Tuple[PublicKey, List[TransactionInstruction], List[Keypair]]:
    """
    Implement the logic for selling an NFT to a liquidity pair on the Solana blockchain.

    :param program_id: Program public key (PublicKey)
    :param connection: Solana RPC connection (Client)
    :param args: Arguments for the transaction (dict)
    :param accounts: Accounts involved in the transaction (dict)
    :param send_txn: Callable to send the transaction (function)
    :return: Tuple containing account public key, list of transaction instructions, and list of signers (Keypair)
    """
    # Placeholder for the core logic of the function
    # You will need to implement the specific logic based on the TypeScript version

    # Example structure (replace with actual logic):
    account = PublicKey('<replace_with_actual_account>')
    instructions = []  # List of TransactionInstruction
    signers = []       # List of Keypair

    # Implement the logic to populate 'instructions' and 'signers' based on 'args' and 'accounts'

    # Example of sending a transaction (replace with actual transaction logic)
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)
    await send_txn(transaction, signers)

    return account, instructions, signers



async def sell_nft_to_liquidity_pair(
    program_id: PublicKey,
    connection: Client,
    args: dict,
    accounts: dict,
    send_txn
):
    program = return_anchor_program(program_id, connection)
    nft_pair_box = Keypair.generate()

    user_nft_token_account = await find_associated_token_address(accounts['userPubkey'], accounts['nftMint'])

    nfts_owner, _ = await PublicKey.find_program_address(
        [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair']], program_id
    )
    fee_sol_vault, _ = await PublicKey.find_program_address(
        [ENCODER.encode(FEE_PREFIX), accounts['pair']], program_id
    )
    sol_funds_vault, _ = await PublicKey.find_program_address(
        [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair']], program_id
    )

    new_vault_token_account = await find_associated_token_address(nfts_owner, accounts['nftMint'])
    owner_token_record = find_token_record_pda(accounts['nftMint'], user_nft_token_account)
    dest_token_record = find_token_record_pda(accounts['nftMint'], new_vault_token_account)
    edition_info = get_metaplex_edition_pda(accounts['nftMint'])
    metadata_info = get_metaplex_metadata_pda(accounts['nftMint'])
    metadata_account = await Metadata.from_account_address(connection, metadata_info)

    rule_set = METADATA_PROGRAM_PUBKEY
    if args.get('pnft'):
        if args['pnft'].get('payerRuleSet') and args['pnft'].get('nameForRuleSet'):
            rule_set = await find_rule_set_pda(args['pnft']['payerRuleSet'], args['pnft']['nameForRuleSet'])
        elif metadata_account.programmable_config:
            rule_set = metadata_account.programmable_config.rule_set

    creators = metadata_account.data.creators if metadata_account.data else None
    creator_account_metas = [
        AccountMeta(pubkey=creator.address, is_signer=False, is_writable=True)
        for creator in creators if creator.share > 0
    ] if creators else []

    modify_compute_units = AccountMeta(pubkey=PublicKey('ComputeBudget111111111111111111111111111111'), is_signer=False, is_writable=False)

    # Construct the sellNftToLiquidityPair instruction
    sell_nft_instruction = await program.sell_nft_to_liquidity_pair(
        args['minAmountToGet'], args['skipFailed'], args.get('proof', []), None
    ).accounts_strict({
        'nftPairBox': nft_pair_box.public_key,
        'nftValidationAdapter': accounts['nftValidationAdapter'],
        'pair': accounts['pair'],
        'user': accounts['userPubkey'],
        'nftMint': accounts['nftMint'],
        'nftUserTokenAccount': user_nft_token_account,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'nftsOwner': nfts_owner,
        'feeSolVault': fee_sol_vault,
        'newVaultTokenAccount': new_vault_token_account,
        'protocolFeeReceiver': accounts['protocolFeeReceiver'],
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'fundsSolVault': sol_funds_vault,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_info,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
    }).remaining_accounts(
        [{'pubkey': accounts.get('nftValidationAdapterV2', rule_set), 'isSigner': False, 'isWritable': False}] + creator_account_metas
    ).instruction()

    # Create and populate the transaction
    transaction = Transaction()
    transaction.add(modify_compute_units)
    transaction.add(sell_nft_instruction)

    # Define the signers
    signers = [nft_pair_box]

    # Send the transaction
    await send_txn(transaction, signers)

    # Return the result
    return {'account': nft_pair_box.public_key, 'instructions': transaction.instructions, 'signers': signers}


    