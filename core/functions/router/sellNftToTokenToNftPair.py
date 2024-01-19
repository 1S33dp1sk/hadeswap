from solana.rpc.api import Client, Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.system_program import SYS_PROGRAM_ID
from solana.sysvar import SYSVAR_RENT_PUBKEY, SYSVAR_INSTRUCTIONS_PUBKEY
from solana.transaction import AccountMeta

from .helpers import (
    return_anchor_program, find_associated_token_address, find_token_record_pda,
    get_metaplex_edition_pda, get_metaplex_metadata_pda, find_rule_set_pda
)
from .constants import ENCODER, SOL_FUNDS_PREFIX, METADATA_PROGRAM_PUBKEY, TOKEN_PROGRAM_ID, ASSOCIATED_PROGRAM_ID
from .mpl_token_metadata import Metadata  # Assuming a Python equivalent for Metaplex's Metadata

async def sell_nft_to_token_to_nft_pair(
    program_id: PublicKey,
    connection: Client,
    args: dict,
    accounts: dict,
    send_txn
):
    program = return_anchor_program(program_id, connection)
    instructions = []

    user_nft_token_account = await find_associated_token_address(accounts['userPubkey'], accounts['nftMint'])
    asset_receiver_token_account = await find_associated_token_address(accounts['assetReceiver'], accounts['nftMint'])

    sol_funds_vault, _ = await PublicKey.find_program_address(
        [ENCODER.encode(SOL_FUNDS_PREFIX), accounts['pair']], program_id
    )

    owner_token_record = find_token_record_pda(accounts['nftMint'], user_nft_token_account)
    dest_token_record = find_token_record_pda(accounts['nftMint'], asset_receiver_token_account)
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
    instructions.append(modify_compute_units)

    # Construct the sellNftToTokenToNftPair instruction
    sell_nft_instruction = await program.sell_nft_to_token_to_nft_pair(
        args['minAmountToGet'], args['skipFailed'], args.get('proof', []), None
    ).accounts_strict({
        'nftValidationAdapter': accounts['nftValidationAdapter'],
        'pair': accounts['pair'],
        'user': accounts['userPubkey'],
        'nftMint': accounts['nftMint'],
        'nftUserTokenAccount': user_nft_token_account,
        'tokenProgram': TOKEN_PROGRAM_ID,
        'assetReceiver': accounts['assetReceiver'],
        'protocolFeeReceiver': accounts['protocolFeeReceiver'],
        'assetReceiverTokenAccount': asset_receiver_token_account,
        'associatedTokenProgram': ASSOCIATED_PROGRAM_ID,
        'fundsSolVault': sol_funds_vault,
        'instructions': SYSVAR_INSTRUCTIONS_PUBKEY,
        'metadataInfo': metadata_info,
        'ownerTokenRecord': owner_token_record,
        'destTokenRecord': dest_token_record,
        'editionInfo': edition_info,
        'authorizationRulesProgram': AUTHORIZATION_RULES_PROGRAM,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
        'metadataProgram': METADATA_PROGRAM_PUBKEY,
    }).remaining_accounts(
        [{'pubkey': accounts.get('nftValidationAdapterV2', rule_set), 'isSigner': False, 'isWritable': False}] + creator_account_metas
    ).instruction()

    # Add the instruction to the instructions list
    instructions.append(sell_nft_instruction)

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
