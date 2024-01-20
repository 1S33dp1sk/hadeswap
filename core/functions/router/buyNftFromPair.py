# Solana-py imports for Solana blockchain interaction
from solana.publickey import PublicKey
from solana.transaction import AccountMeta
from solana.rpc.api import Client

# Importing constants from the constants module
from hadeswap.constants import (
    AUTHORIZATION_RULES_PROGRAM, EMPTY_PUBKEY, ENCODER, FEE_PREFIX,
    METADATA_PROGRAM_PUBKEY, NFTS_OWNER_PREFIX, SOL_FUNDS_PREFIX
)

# Importing helper functions from the helpers module
from hadeswap.helpers import (
    anchor_raw_BNs_and_pubkeys_to_nums_and_strings, find_rule_set_pda,
    find_token_record_pda, get_metaplex_edition_pda, get_metaplex_metadata,
    return_anchor_program
)

# Imports for associated and token program IDs, assuming they are defined in your Python project
from hadeswap.utils import ASSOCIATED_PROGRAM_ID, TOKEN_PROGRAM_ID

# Imports for Metaplex's Metadata, assuming a Python equivalent is implemented in your project
from mpl_token_metadata import Metadata



async def buy_nft_from_pair(
    program_id: PublicKey,
    connection: Client,
    args: dict,
    accounts: dict,
    send_txn
):
    program = return_anchor_program(program_id, connection)
    instructions = []

    # Finding program addresses
    sol_funds_vault, _ = await PublicKey.find_program_address(
        [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair']], program_id
    )
    nfts_owner, _ = await PublicKey.find_program_address(
        [ENCODER.encode(NFTS_OWNER_PREFIX), accounts['pair']], program_id
    )
    fee_sol_vault, _ = await PublicKey.find_program_address(
        [ENCODER.encode(FEE_PREFIX), accounts['pair']], program_id
    )

    # Finding associated token addresses and PDAs
    user_nft_token_account = await find_associated_token_address(accounts['userPubkey'], accounts['nftMint'])
    owner_token_record = find_token_record_pda(accounts['nftMint'], accounts['vaultNftTokenAccount'])
    dest_token_record = find_token_record_pda(accounts['nftMint'], user_nft_token_account)
    edition_info = get_metaplex_edition_pda(accounts['nftMint'])
    metadata_info = get_metaplex_metadata(accounts['nftMint'])
    metadata_account = await Metadata.from_account_address(connection, metadata_info)

    # Determining the rule set
    rule_set = METADATA_PROGRAM_PUBKEY
    if args.get('pnft'):
        if args['pnft'].get('payerRuleSet') and args['pnft'].get('nameForRuleSet'):
            rule_set = await find_rule_set_pda(args['pnft']['payerRuleSet'], args['pnft']['nameForRuleSet'])
        elif metadata_account.programmable_config:
            rule_set = metadata_account.programmable_config.rule_set

    # Handling creators
    creators = metadata_account.data.creators if metadata_account.data else None
    creator_account_metas = [
        AccountMeta(pubkey=creator.address, is_signer=False, is_writable=True)
        for creator in creators if creator.share > 0
    ] if creators else []

    # Modify compute units instruction (adjust units as needed)
    modify_compute_units = AccountMeta(pubkey=PublicKey('ComputeBudget111111111111111111111111111111'), is_signer=False, is_writable=False)
    instructions.append(modify_compute_units)

    # Construct the buyNftFromPair instruction
    buy_nft_instruction = await program.buy_nft_from_pair(
        args['maxAmountToPay'], args['skipFailed'], None
    ).accounts_strict({
        'nftPairBox': accounts['nftPairBox'],
        'pair': accounts['pair'],
        'user': accounts['userPubkey'],
        'fundsSolVault': sol_funds_vault,
        'nftsOwner': nfts_owner,
        'feeSolVault': fee_sol_vault,
        'nftMint': accounts['nftMint'],
        'vaultNftTokenAccount': accounts['vaultNftTokenAccount'],
        'nftUserTokenAccount': user_nft_token_account,
        'assetReceiver': accounts['assetReceiver'],
        'protocolFeeReceiver': accounts['protocolFeeReceiver'],
        'tokenProgram': TOKEN_PROGRAM_ID,
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_info,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
    }).remaining_accounts([
        {'pubkey': rule_set or METADATA_PROGRAM_PUBKEY, 'isSigner': False, 'isWritable': False}
    ] + creator_account_metas).instruction()

    # Add the instruction to the instructions list
    instructions.append(buy_nft_instruction)

    # Create and populate the transaction
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    # Define the signers (if any)
    signers = []

    # Send the transaction
    await send_txn(transaction, signers)

    # Return the result
    return {'account': None, 'instructions': transaction.instructions, 'signers': signers}