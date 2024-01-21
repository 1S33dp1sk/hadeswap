from ..common import *


async def validate_nft(program_id: Pubkey, connection: Client, user_pubkey: Pubkey, classic_validation_whitelist: Pubkey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    nft_validation_adapter = Keypair()

    # Assuming the `validateNft` method is implemented in the Python version of the anchor program
    validate_nft_instruction = program.validateNft().accounts_strict({
        'nftValidationAdapter': nft_validation_adapter.public_key,
        'validationWhitelist': classic_validation_whitelist,
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(validate_nft_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [nft_validation_adapter]
    await send_txn(transaction, signers)
    return {'account': nft_validation_adapter.public_key, 'instructions': instructions, 'signers': signers}

async def modify_hado_market(program_id: Pubkey, connection: Client, user_pubkey: Pubkey, hado_market: Pubkey, validation_adapter_authority: Pubkey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    # Assuming the `modifyHadoMarket` method is implemented in the Python version of the anchor program
    modify_hado_market_instruction = program.modifyHadoMarket().accounts_strict({
        'hadoMarket': hado_market,
        'user': user_pubkey,
        'validationAdapterProgram': validation_adapter_authority,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(modify_hado_market_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}

async def initialize_hado_market(program_id: Pubkey, connection: Client, user_pubkey: Pubkey, validation_adapter_program: Pubkey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    hado_market = Keypair()

    # Assuming the `initializeHadoMarket` method is implemented in the Python version of the anchor program
    initialize_hado_market_instruction = program.initializeHadoMarket().accounts_strict({
        'hadoMarket': hado_market.public_key,
        'user': user_pubkey,
        'validationAdapterProgram': validation_adapter_program,
        'pairTokenMint': EMPTY_PUBKEY,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(initialize_hado_market_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [hado_market]
    await send_txn(transaction, signers)
    return {'account': hado_market.public_key, 'instructions': instructions, 'signers': signers}

async def finish_hado_market(program_id: Pubkey, connection: Client, user_pubkey: Pubkey, hado_market: Pubkey, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []

    # Assuming the `finishHadoMarket` method is implemented in the Python version of the anchor program
    finish_hado_market_instruction = program.finishHadoMarket().accounts_strict({
        'hadoMarket': hado_market,
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(finish_hado_market_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = []
    await send_txn(transaction, signers)
    return {'account': None, 'instructions': instructions, 'signers': signers}

async def create_merkle_tree_whitelist(program_id: Pubkey, connection: Client, user_pubkey: Pubkey, hado_market: Pubkey, root: bytes, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    nft_validation_adapter_v2 = Keypair()

    # Assuming the `addMerkleTreeWhitelist` method is implemented in the Python version of the anchor program
    add_merkle_tree_whitelist_instruction = program.addMerkleTreeWhitelist(list(root)).accounts_strict({
        'nftValidationAdapter': nft_validation_adapter_v2.public_key,
        'hadoMarket': hado_market,
        'user': user_pubkey,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(add_merkle_tree_whitelist_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [nft_validation_adapter_v2]
    await send_txn(transaction, signers)
    return {'account': nft_validation_adapter_v2.public_key, 'instructions': instructions, 'signers': signers}

async def add_classic_whitelist_to_market(program_id: Pubkey, connection: Client, user_pubkey: Pubkey, hado_market: Pubkey, whitelisted_address: Pubkey, whitelist_type: NftValidationWhitelistType, send_txn):
    program = await return_anchor_program(program_id, connection)
    instructions = []
    validation_whitelist = Keypair()

    # Convert Python enum to a format suitable for the Anchor program
    anchor_enum_whitelist_type = enum_to_anchor_enum(whitelist_type)

    # Assuming the `addClassicWhitelistToMarket` method is implemented in the Python version of the anchor program
    add_classic_whitelist_to_market_instruction = program.addClassicWhitelistToMarket(anchor_enum_whitelist_type).accounts_strict({
        'validationWhitelist': validation_whitelist.public_key,
        'hadoMarket': hado_market,
        'user': user_pubkey,
        'whitelistedAddress': whitelisted_address,
        'systemProgram': SYS_PROGRAM_ID,
        'rent': SYSVAR_RENT_PUBKEY,
    }).instruction()

    instructions.append(add_classic_whitelist_to_market_instruction)
    
    transaction = Transaction()
    for instruction in instructions:
        transaction.add(instruction)

    signers = [validation_whitelist]
    await send_txn(transaction, signers)
    return {'account': validation_whitelist.public_key, 'instructions': instructions, 'signers': signers}



