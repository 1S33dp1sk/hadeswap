from solana.rpc.api import Client
from solana.publickey import PublicKey

from .helpers import return_anchor_program, anchor_raw_BNs_and_pubkeys_to_nums_and_strings

async def get_all_program_accounts(program_id: PublicKey, connection: Client):
    program = await return_anchor_program(program_id, connection)

    # Retrieve and process all program accounts
    hado_markets_raw = await program.account.hadoMarket.all()
    hado_markets = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in hado_markets_raw]

    nft_swap_pairs_raw = await program.account.nftSwapPair.all()
    nft_swap_pairs = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in nft_swap_pairs_raw]

    classic_validation_whitelists_raw = await program.account.classicValidationWhitelist.all()
    classic_validation_whitelists = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in classic_validation_whitelists_raw]

    nft_validation_adapters_raw = await program.account.nftValidationAdapter.all()
    nft_validation_adapters = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in nft_validation_adapters_raw]

    nft_validation_adapters_v2_raw = await program.account.nftValidationAdapterV2.all()
    nft_validation_adapters_v2 = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in nft_validation_adapters_v2_raw]

    authority_adapters_raw = await program.account.authorityAdapter.all()
    authority_adapters = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in authority_adapters_raw]

    nft_pair_boxes_raw = await program.account.nftPairBox.all()
    nft_pair_boxes = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in nft_pair_boxes_raw]

    adapter_whitelists_raw = await program.account.adapterWhitelist.all()
    adapter_whitelists = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in adapter_whitelists_raw]

    protocol_settings_v1_raw = await program.account.protocolSettingsV1.all()
    protocol_settings_v1 = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in protocol_settings_v1_raw]

    protocol_admin_multisigs_raw = await program.account.protocolAdminMultisig.all()
    protocol_admin_multisigs = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in protocol_admin_multisigs_raw]

    liquidity_provision_orders_raw = await program.account.liquidityProvisionOrder.all()
    liquidity_provision_orders = [anchor_raw_BNs_and_pubkeys_to_nums_and_strings(acc) for acc in liquidity_provision_orders_raw]

    return {
        'hadoMarkets': hado_markets,
        'nftSwapPairs': nft_swap_pairs,
        'nftPairBoxes': nft_pair_boxes,
        'classicValidationWhitelists': classic_validation_whitelists,
        'nftValidationAdapters': nft_validation_adapters,
        'nftValidationAdaptersV2': nft_validation_adapters_v2,
        'authorityAdapters': authority_adapters,
        'adapterWhitelists': adapter_whitelists,
        'protocolSettingsV1': protocol_settings_v1,
        'protocolAdminMultisigs': protocol_admin_multisigs,
        'liquidityProvisionOrders': liquidity_provision_orders
    }
