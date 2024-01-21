Hadeswap = {
  'version': '0.1.0',
  'name': 'hadeswap',
  'instructions': [
    {
      'name': 'initializePair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'hadoMarket',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pairAuthorityAdapterProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'partialAdapterProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'partialAssetReceiver',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeTokenAccount',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'fundsTokenAccount',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'assetReceiver',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'assetReceiverTokenAccount',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'bumps',
          'type': {
            'defined': 'PairBumps',
          },
        },
        {
          'name': 'params',
          'type': {
            'defined': 'PairParams',
          },
        },
        {
          'name': 'bondingCurveType',
          'type': {
            'defined': 'BondingCurveType',
          },
        },
        {
          'name': 'pairType',
          'type': {
            'defined': 'PairType',
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'createClassicAuthorityAdapter',
      'accounts': [
        {
          'name': 'authorityAdapter',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'depositSolToPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'amountOfOrders',
          'type': 'u64',
        },
      ],
      'returns': None,
    },
    {
      'name': 'validateNft',
      'accounts': [
        {
          'name': 'nftValidationAdapter',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'validationWhitelist',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'depositNftToPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'initializeHadoMarket',
      'accounts': [
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'validationAdapterProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pairTokenMint',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'finishHadoMarket',
      'accounts': [
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'addClassicWhitelistToMarket',
      'accounts': [
        {
          'name': 'validationWhitelist',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'whitelistedAddress',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'whitelistType',
          'type': {
            'defined': 'NftValidationWhitelistType',
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'depositLiquidityToPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'putPairOnMarket',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'buyNftFromPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'assetReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'protocolFeeReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'maxAmountToPay',
          'type': 'u64',
        },
        {
          'name': 'skipFailed',
          'type': 'bool',
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'sellNftToTokenToNftPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'assetReceiverTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'assetReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'protocolFeeReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'minAmountToGet',
          'type': 'u64',
        },
        {
          'name': 'skipFailed',
          'type': 'bool',
        },
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'sellNftToLiquidityPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'newVaultTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'protocolFeeReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'minAmountToGet',
          'type': 'u64',
        },
        {
          'name': 'skipFailed',
          'type': 'bool',
        },
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawSolFromPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'quantityOfOrders',
          'type': 'u64',
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawNftFromPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityFromBalancedPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'modifyPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'params',
          'type': {
            'defined': 'PairParams',
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityFromBuyOrdersPair',
      'accounts': [
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityFromSellOrdersPair',
      'accounts': [
        {
          'name': 'nftPairBoxFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftMintFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccountFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccountFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftPairBoxSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfoFirst',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfoFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecordFirst',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecordFirst',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'editionInfoSecond',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfoSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecordSecond',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecordSecond',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMintSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccountSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccountSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityOrderVirtualFees',
      'accounts': [
        {
          'name': 'liquidityProvisionOrder',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeVirtualNftSwapPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'withdrawVirtualFees',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeNftPairBox',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeLiquidityProvisionOrder',
      'accounts': [
        {
          'name': 'liquidityProvisionOrder',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'customValidateNft',
      'accounts': [
        {
          'name': 'nftValidationAdapter',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'hadoMarket',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'whitelistedAddress',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'adapterProgramSigner',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'duration',
          'type': 'u64',
        },
        {
          'name': 'nftValidationWhitelistType',
          'type': {
            'defined': 'NftValidationWhitelistType',
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'modifyHadoMarket',
      'accounts': [
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'validationAdapterProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'addMerkleTreeWhitelist',
      'accounts': [
        {
          'name': 'nftValidationAdapter',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'root',
          'type': {
            'array': ['u8', 32],
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'closeNftValidationAdapter',
      'accounts': [
        {
          'name': 'nftValidationAdapter',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeClassicWhitelist',
      'accounts': [
        {
          'name': 'validationWhitelist',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeNftValidationAdapterV2',
      'accounts': [
        {
          'name': 'nftValidationAdapterV2',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'withdrawOutstandingTokensByAdmin',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'depositLiquidityOnlyBuyOrders',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'quantityOfOrders',
          'type': 'u64',
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityOnlyBuyOrders',
      'accounts': [
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'quantityOfOrders',
          'type': 'u64',
        },
      ],
      'returns': None,
    },
    {
      'name': 'depositLiquiditySingleSellToPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawLiquiditySingleSellOrder',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
  ],
  'accounts': [
    {
      'name': 'adapterWhitelist',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'whitelistedAdapterProgram',
            'type': 'publicKey',
          },
          {
            'name': 'adapterType',
            'type': {
              'defined': 'AdapterType',
            },
          },
        ],
      },
    },
    {
      'name': 'authorityAdapter',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'authorityAdapterProgram',
            'type': 'publicKey',
          },
          {
            'name': 'authorityOwner',
            'type': 'publicKey',
          },
          {
            'name': 'authorityType',
            'type': {
              'defined': 'AuthorityAdapterType',
            },
          },
          {
            'name': 'expiringAt',
            'type': 'u64',
          },
          {
            'name': 'authorityState',
            'type': {
              'defined': 'AuthorityState',
            },
          },
        ],
      },
    },
    {
      'name': 'classicValidationWhitelist',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'hadoMarket',
            'type': 'publicKey',
          },
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'whitelistType',
            'type': {
              'defined': 'NftValidationWhitelistType',
            },
          },
          {
            'name': 'whitelistedAddress',
            'type': 'publicKey',
          },
        ],
      },
    },
    {
      'name': 'hadoMarket',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'marketAuthority',
            'type': 'publicKey',
          },
          {
            'name': 'marketState',
            'type': {
              'defined': 'MarketState',
            },
          },
          {
            'name': 'marketTrustType',
            'type': {
              'defined': 'MarketTrustType',
            },
          },
          {
            'name': 'pairValidationType',
            'type': {
              'defined': 'PairValidationType',
            },
          },
          {
            'name': 'validationAdapterProgram',
            'type': 'publicKey',
          },
          {
            'name': 'pairTokenType',
            'type': {
              'defined': 'PairTokenType',
            },
          },
          {
            'name': 'pairTokenMint',
            'type': 'publicKey',
          },
        ],
      },
    },
    {
      'name': 'liquidityProvisionOrder',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'nftSwapPair',
            'type': 'publicKey',
          },
          {
            'name': 'lpOrderState',
            'type': {
              'defined': 'LpOrderState',
            },
          },
          {
            'name': 'orderACounter',
            'type': 'i64',
          },
          {
            'name': 'orderBCounter',
            'type': 'i64',
          },
          {
            'name': 'accumulatedFee',
            'type': 'u64',
          },
          {
            'name': 'lpTokenMint',
            'type': 'publicKey',
          },
          {
            'name': 'liquidityFeeBump',
            'type': 'u8',
          },
          {
            'name': 'createdAt',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'nftPairBox',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'nftMint',
            'type': 'publicKey',
          },
          {
            'name': 'nftMetadata',
            'type': 'publicKey',
          },
          {
            'name': 'nftBoxType',
            'type': {
              'defined': 'NftBoxType',
            },
          },
          {
            'name': 'vaultTokenAccount',
            'type': 'publicKey',
          },
          {
            'name': 'status',
            'type': {
              'defined': 'NftBoxState',
            },
          },
        ],
      },
    },
    {
      'name': 'nftSwapPair',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'hadoMarket',
            'type': 'publicKey',
          },
          {
            'name': 'pairType',
            'type': {
              'defined': 'PairType',
            },
          },
          {
            'name': 'pairState',
            'type': {
              'defined': 'PairState',
            },
          },
          {
            'name': 'pairAuthorityType',
            'type': {
              'defined': 'PairAuthorityType',
            },
          },
          {
            'name': 'pairAuthorityAdapterProgram',
            'type': 'publicKey',
          },
          {
            'name': 'lpTokensMint',
            'type': 'publicKey',
          },
          {
            'name': 'lpTokensInCirculation',
            'type': 'u64',
          },
          {
            'name': 'bondingCurve',
            'type': {
              'defined': 'BondingCurve',
            },
          },
          {
            'name': 'baseSpotPrice',
            'type': 'u64',
          },
          {
            'name': 'fee',
            'type': 'u64',
          },
          {
            'name': 'mathCounter',
            'type': 'i64',
          },
          {
            'name': 'currentSpotPrice',
            'type': 'u64',
          },
          {
            'name': 'feeTokenAccount',
            'type': 'publicKey',
          },
          {
            'name': 'feeVaultSeed',
            'type': 'u8',
          },
          {
            'name': 'solOrTokenFeeAmount',
            'type': 'u64',
          },
          {
            'name': 'fundsTokenAccount',
            'type': 'publicKey',
          },
          {
            'name': 'fundsSolVaultSeed',
            'type': 'u8',
          },
          {
            'name': 'fundsSolOrTokenBalance',
            'type': 'u64',
          },
          {
            'name': 'initialFundsSolOrTokenBalance',
            'type': 'u64',
          },
          {
            'name': 'buyOrdersQuantity',
            'type': 'u64',
          },
          {
            'name': 'nftsSeed',
            'type': 'u8',
          },
          {
            'name': 'nftsCount',
            'type': 'u64',
          },
          {
            'name': 'lastTransactedAt',
            'type': 'u64',
          },
          {
            'name': 'concentrationIndex',
            'type': 'u64',
          },
          {
            'name': 'assetReceiver',
            'type': 'publicKey',
          },
        ],
      },
    },
    {
      'name': 'nftValidationAdapterV2',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'hadoMarket',
            'type': 'publicKey',
          },
          {
            'name': 'scopeType',
            'type': {
              'defined': 'ScopeType',
            },
          },
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationProgram',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationWhitelistType',
            'type': {
              'defined': 'NftValidationWhitelistTypeV2',
            },
          },
          {
            'name': 'whitelistedAddress',
            'type': 'publicKey',
          },
          {
            'name': 'root',
            'type': {
              'array': ['u8', 32],
            },
          },
          {
            'name': 'nftValidationDurationType',
            'type': {
              'defined': 'NftValidationDurationType',
            },
          },
          {
            'name': 'validUntil',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'nftValidationAdapter',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'hadoMarket',
            'type': 'publicKey',
          },
          {
            'name': 'scopeType',
            'type': {
              'defined': 'ScopeType',
            },
          },
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationProgram',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationWhitelistType',
            'type': {
              'defined': 'NftValidationWhitelistType',
            },
          },
          {
            'name': 'whitelistedAddress',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationDurationType',
            'type': {
              'defined': 'NftValidationDurationType',
            },
          },
          {
            'name': 'validUntil',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'protocolAdminMultisig',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'protocolSettings',
            'type': 'publicKey',
          },
          {
            'name': 'admin',
            'type': 'publicKey',
          },
          {
            'name': 'weight',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'protocolSettingsV1',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'protocolFee',
            'type': 'u64',
          },
          {
            'name': 'protocolFeeMultiplier',
            'type': 'u64',
          },
          {
            'name': 'maxFee',
            'type': 'u64',
          },
          {
            'name': 'protocolFeeReceiver',
            'type': 'publicKey',
          },
          {
            'name': 'adminThresholdAmountMultisig',
            'type': 'u64',
          },
        ],
      },
    },
  ],
  'types': [
    {
      'name': 'PairParams',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'delta',
            'type': 'u64',
          },
          {
            'name': 'spotPrice',
            'type': 'u64',
          },
          {
            'name': 'fee',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'PairBumps',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'fundsSolVaultSeed',
            'type': 'u8',
          },
          {
            'name': 'feeVaultSeed',
            'type': 'u8',
          },
          {
            'name': 'nftsSeed',
            'type': 'u8',
          },
        ],
      },
    },
    {
      'name': 'BondingCurve',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'delta',
            'type': 'u64',
          },
          {
            'name': 'bondingType',
            'type': {
              'defined': 'BondingCurveType',
            },
          },
        ],
      },
    },
    {
      'name': 'AuthorizationDataLocal',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'payload',
            'type': {
              'vec': {
                'defined': 'TaggedPayload',
              },
            },
          },
        ],
      },
    },
    {
      'name': 'TaggedPayload',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'name',
            'type': 'string',
          },
          {
            'name': 'payload',
            'type': {
              'defined': 'PayloadTypeLocal',
            },
          },
        ],
      },
    },
    {
      'name': 'SeedsVecLocal',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'seeds',
            'type': {
              'vec': 'bytes',
            },
          },
        ],
      },
    },
    {
      'name': 'ProofInfoLocal',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'proof',
            'type': {
              'vec': {
                'array': ['u8', 32],
              },
            },
          },
        ],
      },
    },
    {
      'name': 'AdapterType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Validation',
          },
          {
            'name': 'Authority',
          },
          {
            'name': 'Partial',
          },
        ],
      },
    },
    {
      'name': 'AuthorityAdapterType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'OneTime',
          },
          {
            'name': 'Persistent',
          },
        ],
      },
    },
    {
      'name': 'AuthorityState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Active',
          },
          {
            'name': 'Used',
          },
          {
            'name': 'Expired',
          },
          {
            'name': 'Revoked',
          },
        ],
      },
    },
    {
      'name': 'MarketTrustType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Unverified',
          },
          {
            'name': 'Verified',
          },
        ],
      },
    },
    {
      'name': 'MarketState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Initializing',
          },
          {
            'name': 'Available',
          },
        ],
      },
    },
    {
      'name': 'PairValidationType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'ClassicValidation',
          },
          {
            'name': 'CustomValidation',
          },
        ],
      },
    },
    {
      'name': 'PairTokenType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'NativeSol',
          },
          {
            'name': 'Spl',
          },
        ],
      },
    },
    {
      'name': 'LpOrderState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Virtual',
          },
          {
            'name': 'Tokenized',
          },
          {
            'name': 'WithdrawnVirtual',
          },
          {
            'name': 'WithdrawnTokenized',
          },
        ],
      },
    },
    {
      'name': 'NftBoxState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Closed',
          },
          {
            'name': 'Active',
          },
        ],
      },
    },
    {
      'name': 'NftBoxType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Escrow',
          },
          {
            'name': 'Escrowless',
          },
        ],
      },
    },
    {
      'name': 'PairType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'TokenForNft',
          },
          {
            'name': 'NftForToken',
          },
          {
            'name': 'LiquidityProvision',
          },
        ],
      },
    },
    {
      'name': 'PairState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Initializing',
          },
          {
            'name': 'OnMarketVirtual',
          },
          {
            'name': 'OnMarketTokenized',
          },
          {
            'name': 'Frozen',
          },
        ],
      },
    },
    {
      'name': 'PairAuthorityType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'ClassicAuthority',
          },
          {
            'name': 'CustomAuthority',
          },
        ],
      },
    },
    {
      'name': 'PartialSettings',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'None',
          },
          {
            'name': 'CustomPartial',
          },
        ],
      },
    },
    {
      'name': 'BondingCurveType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Linear',
          },
          {
            'name': 'Exponential',
          },
          {
            'name': 'XYK',
          },
        ],
      },
    },
    {
      'name': 'NftValidationWhitelistTypeV2',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Creator',
          },
          {
            'name': 'Nft',
          },
          {
            'name': 'MerkleTree',
          },
        ],
      },
    },
    {
      'name': 'ScopeType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Market',
          },
          {
            'name': 'Pair',
          },
        ],
      },
    },
    {
      'name': 'NftValidationDurationType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Finite',
          },
          {
            'name': 'Infinite',
          },
        ],
      },
    },
    {
      'name': 'NftValidationWhitelistType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Creator',
          },
          {
            'name': 'Nft',
          },
        ],
      },
    },
    {
      'name': 'PayloadTypeLocal',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Pubkey',
            'fields': ['publicKey'],
          },
          {
            'name': 'Seeds',
            'fields': [
              {
                'defined': 'SeedsVecLocal',
              },
            ],
          },
          {
            'name': 'MerkleProof',
            'fields': [
              {
                'defined': 'ProofInfoLocal',
              },
            ],
          },
          {
            'name': 'Number',
            'fields': ['u64'],
          },
        ],
      },
    },
  ],
  'errors': [
    {
      'code': 6000,
      'name': 'MetadataDoesntExist',
      'msg': 'MetadataDoesntExist',
    },
    {
      'code': 6001,
      'name': 'DerivedKeyInvalid',
      'msg': 'DerivedKeyInvalid',
    },
    {
      'code': 6002,
      'name': 'InvalidCollectionDetails',
      'msg': 'InvalidCollectionDetails',
    },
    {
      'code': 6003,
      'name': 'InvalidCollection',
      'msg': 'InvalidCollection',
    },
    {
      'code': 6004,
      'name': 'InvalidCollectionMint',
      'msg': 'InvalidCollectionMint',
    },
    {
      'code': 6005,
      'name': 'NftNotVerified',
      'msg': 'NftNotVerified',
    },
    {
      'code': 6006,
      'name': 'InvalidOwner',
      'msg': 'InvalidOwner',
    },
    {
      'code': 6007,
      'name': 'InvalidDelta',
      'msg': 'InvalidDelta',
    },
    {
      'code': 6008,
      'name': 'InvalidFee',
      'msg': 'InvalidFee',
    },
    {
      'code': 6009,
      'name': 'InvalidPairType',
      'msg': 'InvalidPairType',
    },
    {
      'code': 6010,
      'name': 'NotEnoughInTokenAccount',
      'msg': 'NotEnoughInTokenAccount',
    },
    {
      'code': 6011,
      'name': 'InvalidMint',
      'msg': 'InvalidMint',
    },
    {
      'code': 6012,
      'name': 'InvalidSolVault',
      'msg': 'InvalidSolVault',
    },
    {
      'code': 6013,
      'name': 'InvalidFundingAmount',
      'msg': 'InvalidFundingAmount',
    },
    {
      'code': 6014,
      'name': 'NotEnoughLamports',
      'msg': 'NotEnoughLamports',
    },
    {
      'code': 6015,
      'name': 'InvalidJpegOwner',
      'msg': 'InvalidJpegOwner',
    },
    {
      'code': 6016,
      'name': 'InvalidTokenAccount',
      'msg': 'InvalidTokenAccount',
    },
    {
      'code': 6017,
      'name': 'InvalidPayer',
      'msg': 'InvalidPayer',
    },
    {
      'code': 6018,
      'name': 'ShouldBeActive',
      'msg': 'ShouldBeActive',
    },
    {
      'code': 6019,
      'name': 'CantMakeZeroOrders',
      'msg': "Can't make 0 orders",
    },
    {
      'code': 6020,
      'name': 'OnlyClassicAuthority',
      'msg': 'OnlyClassicAuthority',
    },
    {
      'code': 6021,
      'name': 'NotValidAuthorityAdapter',
      'msg': 'NotValidAuthorityAdapter',
    },
    {
      'code': 6022,
      'name': 'UserDoesntHaveAuthority',
      'msg': 'UserDoesntHaveAuthority',
    },
    {
      'code': 6023,
      'name': 'WrongSeed',
      'msg': 'WrongSeed',
    },
    {
      'code': 6024,
      'name': 'CanDepositSolOnlyToTokenToNft',
      'msg': 'CanDepositSolOnlyToTokenToNft',
    },
    {
      'code': 6025,
      'name': 'MaxAmountOfOrdersSucceeded',
      'msg': 'MaxAmountOfOrdersSucceeded',
    },
    {
      'code': 6026,
      'name': 'CanDepositNftOnlyToNftToToken',
      'msg': 'CanDepositNftOnlyToNftToToken',
    },
    {
      'code': 6027,
      'name': 'TokenAccountDoesntContainNft',
      'msg': 'TokenAccountDoesntContainNft',
    },
    {
      'code': 6028,
      'name': 'MarketAuthorityIncorrect',
      'msg': 'MarketAuthorityIncorrect',
    },
    {
      'code': 6029,
      'name': 'CanAddWhitelistOnlyToInitializingMarket',
      'msg': 'CanAddWhitelistOnlyToInitializingMarket',
    },
    {
      'code': 6030,
      'name': 'CanPutPairsOnlyToAvailableMarkets',
      'msg': 'CanPutPairsOnlyToAvailableMarkets',
    },
    {
      'code': 6031,
      'name': 'PairAndNftValidationMarketDoesntMatch',
      'msg': 'PairAndNftValidationMarketDoesntMatch',
    },
    {
      'code': 6032,
      'name': 'OnlyMarketScopeSupported',
      'msg': 'OnlyMarketScopeSupported',
    },
    {
      'code': 6033,
      'name': 'NotWhitelistedNftForThisMarket',
      'msg': 'NotWhitelistedNftForThisMarket',
    },
    {
      'code': 6034,
      'name': 'CanDepositOnlyToLiquidityProvision',
      'msg': 'CanDepositOnlyToLiquidityProvision',
    },
    {
      'code': 6035,
      'name': 'NftBoxDoesntMatchPair',
      'msg': 'NftBoxDoesntMatchPair',
    },
    {
      'code': 6036,
      'name': 'NftBoxShouldBeActive',
      'msg': 'NftBoxShouldBeActive',
    },
    {
      'code': 6037,
      'name': 'NftBoxDoesntMatchMint',
      'msg': 'NftBoxDoesntMatchMint',
    },
    {
      'code': 6038,
      'name': 'CantBuyNftFromTokenForNft',
      'msg': 'CantBuyNftFromTokenForNft',
    },
    {
      'code': 6039,
      'name': 'OnlyTokenForNftIsEligibleForThisSell',
      'msg': 'OnlyTokenForNftIsEligibleForThisSell',
    },
    {
      'code': 6040,
      'name': 'NoBuyOrdersOnThisPair',
      'msg': 'NoBuyOrdersOnThisPair',
    },
    {
      'code': 6041,
      'name': 'OnlyLiquidityProvisionIsEligibleForThisSell',
      'msg': 'OnlyLiquidityProvisionIsEligibleForThisSell',
    },
    {
      'code': 6042,
      'name': 'OnlyTokenForNftIsEligibleForThisWithdrawal',
      'msg': 'OnlyTokenForNftIsEligibleForThisWithdrawal',
    },
    {
      'code': 6043,
      'name': 'OnlyNftForTokenIsEligibleForThisWithdrawal',
      'msg': 'OnlyNftForTokenIsEligibleForThisWithdrawal',
    },
    {
      'code': 6044,
      'name': 'OnlyLiquidityProvisionIsEligibleForThisWithdrawal',
      'msg': 'OnlyLiquidityProvisionIsEligibleForThisWithdrawal',
    },
    {
      'code': 6045,
      'name': 'InstructionIsNotSupported',
      'msg': 'InstructionIsNotSupported',
    },
    {
      'code': 6046,
      'name': 'CanTradeOnlyWithPairsOnMarket',
      'msg': 'CanTradeOnlyWithPairsOnMarket',
    },
    {
      'code': 6047,
      'name': 'NoLiquidityFeesToWithdraw',
      'msg': 'NoLiquidityFeesToWithdraw',
    },
    {
      'code': 6048,
      'name': 'MaxAmountToPayExceeded',
      'msg': 'MaxAmountToPayExceeded',
    },
    {
      'code': 6049,
      'name': 'GettingLessThanMinAmountToGet',
      'msg': 'GettingLessThanMinAmountToGet',
    },
    {
      'code': 6050,
      'name': 'UserDoesntHaveHadomarketAuthority',
      'msg': 'UserDoesntHaveHadomarketAuthority',
    },
    {
      'code': 6051,
      'name': 'HadomarketAlreadyFinished',
      'msg': 'HadomarketAlreadyFinished',
    },
    {
      'code': 6052,
      'name': 'CanDepositLiqudityOnlyToVirtualOrInitializingPairs',
      'msg': 'CanDepositLiqudityOnlyToVirtualOrInitializingPairs',
    },
    {
      'code': 6053,
      'name': 'CanModifyOnlyToVirtualOrInitializingPairs',
      'msg': 'CanModifyOnlyToVirtualOrInitializingPairs',
    },
    {
      'code': 6054,
      'name': 'LiquidityProvisionOrderPairDoesntMatch',
      'msg': 'LiquidityProvisionOrderPairDoesntMatch',
    },
    {
      'code': 6055,
      'name': 'OnlyVirtualLpOrdersCanBeWithdrawnByThisFunction',
      'msg': 'OnlyVirtualLpOrdersCanBeWithdrawnByThisFunction',
    },
    {
      'code': 6056,
      'name': 'OnlyVirtualOrTokenizedLpOrdersCanBeReplacedByThisFunction',
      'msg': 'OnlyVirtualOrTokenizedLpOrdersCanBeReplacedByThisFunction',
    },
    {
      'code': 6057,
      'name': 'LiquidityProvisionOrderNotEdge',
      'msg': 'LiquidityProvisionOrderNotEdge',
    },
    {
      'code': 6058,
      'name': 'NftPairBoxNotParsingFromRemaining',
      'msg': 'NftPairBoxNotParsingFromRemaining',
    },
    {
      'code': 6059,
      'name': 'VaultNftTokenAccountNotParsingFromRemaining',
      'msg': 'VaultNftTokenAccountNotParsingFromRemaining',
    },
    {
      'code': 6060,
      'name': 'UserTokenAccountNotParsingFromRemaining',
      'msg': 'UserTokenAccountNotParsingFromRemaining',
    },
    {
      'code': 6061,
      'name': 'WithdrawingOnlyAtLeastOneBuyAndOneSellPairs',
      'msg': 'WithdrawingOnlyAtLeastOneBuyAndOneSellPairs',
    },
    {
      'code': 6062,
      'name': 'VaultDoesntMatchBox',
      'msg': 'VaultDoesntMatchBox',
    },
    {
      'code': 6063,
      'name': 'WithdrawingOnlyBuyOrdersPairs',
      'msg': 'WithdrawingOnlyBuyOrdersPairs',
    },
    {
      'code': 6064,
      'name': 'WithdrawingOnlySellOrdersPairs',
      'msg': 'WithdrawingOnlySellOrdersPairs',
    },
    {
      'code': 6065,
      'name': 'LiquidityProvisionOrderIsWithdrawn',
      'msg': 'LiquidityProvisionOrderIsWithdrawn',
    },
    {
      'code': 6066,
      'name': 'LiquidityProvisionOrderIsNotCorrectOrderForPair',
      'msg': 'LiquidityProvisionOrderIsNotCorrectOrderForPair',
    },
    {
      'code': 6067,
      'name': 'OnlyMarketVirtualPairsCanBeTokenized',
      'msg': 'OnlyMarketVirtualPairsCanBeTokenized',
    },
    {
      'code': 6068,
      'name': 'OnlyLiquidityProvisionPairsCanBeTokenized',
      'msg': 'OnlyLiquidityProvisionPairsCanBeTokenized',
    },
    {
      'code': 6069,
      'name': 'OnlyInitializingPairsCanBePutOnMarket',
      'msg': 'OnlyInitializingPairsCanBePutOnMarket',
    },
    {
      'code': 6070,
      'name': 'CanMakeLpOrderTokenizedOnlyFromTokenizedPair',
      'msg': 'CanMakeLpOrderTokenizedOnlyFromTokenizedPair',
    },
    {
      'code': 6071,
      'name': 'OnlyVirtualLpOrderCanBeTokenized',
      'msg': 'OnlyVirtualLpOrderCanBeTokenized',
    },
    {
      'code': 6072,
      'name': 'OnlyTokenizedLpOrdersCanWithdrawFees',
      'msg': 'OnlyTokenizedLpOrdersCanWithdrawFees',
    },
    {
      'code': 6073,
      'name': 'UserLpTokenAccountDoesntContainNft',
      'msg': 'UserLpTokenAccountDoesntContainNft',
    },
    {
      'code': 6074,
      'name': 'OnlyTokenizedLpOrdersCanBeWithdrawnByThisFunction',
      'msg': 'OnlyTokenizedLpOrdersCanBeWithdrawnByThisFunction',
    },
    {
      'code': 6075,
      'name': 'LpTokenMintDoesntMatchOrder',
      'msg': 'LpTokenMintDoesntMatchOrder',
    },
    {
      'code': 6076,
      'name': 'CanCloseVirtualPoolOnlyIfNoLiquidityLeft',
      'msg': 'CanCloseVirtualPoolOnlyIfNoLiquidityLeft',
    },
    {
      'code': 6077,
      'name': 'NftIsNotMasterEdition',
      'msg': 'NftIsNotMasterEdition',
    },
    {
      'code': 6078,
      'name': 'NftPairBoxNotClosed',
      'msg': 'NftPairBoxNotClosed',
    },
    {
      'code': 6079,
      'name': 'WrongAdmin',
      'msg': 'WrongAdmin',
    },
    {
      'code': 6080,
      'name': 'PairScopeValidationNotSupportedForNow',
      'msg': 'PairScopeValidationNotSupportedForNow',
    },
    {
      'code': 6081,
      'name': 'CustomValidationAdapterProgramDoesntMatchUser',
      'msg': 'CustomValidationAdapterProgramDoesntMatchUser',
    },
    {
      'code': 6082,
      'name': 'ClassicAuthorityWorksIfValidationProgramIsHadeswap',
      'msg': 'ClassicAuthorityWorksIfValidationProgramIsHadeswap',
    },
    {
      'code': 6083,
      'name': 'NftValidationAdapterV2CanWhitelistOnlyMerkleTree',
      'msg': 'NftValidationAdapterV2CanWhitelistOnlyMerkleTree',
    },
    {
      'code': 6084,
      'name': 'BadRuleSet',
      'msg': 'BadRuleSet',
    },
    {
      'code': 6085,
      'name': 'WrongCreatorInRemainingAccounts',
      'msg': 'WrongCreatorInRemainingAccounts',
    },
  ],
}

IDL  = {
  'version': '0.1.0',
  'name': 'hadeswap',
  'instructions': [
    {
      'name': 'initializePair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'hadoMarket',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pairAuthorityAdapterProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'partialAdapterProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'partialAssetReceiver',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeTokenAccount',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'fundsTokenAccount',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'assetReceiver',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'assetReceiverTokenAccount',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'bumps',
          'type': {
            'defined': 'PairBumps',
          },
        },
        {
          'name': 'params',
          'type': {
            'defined': 'PairParams',
          },
        },
        {
          'name': 'bondingCurveType',
          'type': {
            'defined': 'BondingCurveType',
          },
        },
        {
          'name': 'pairType',
          'type': {
            'defined': 'PairType',
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'createClassicAuthorityAdapter',
      'accounts': [
        {
          'name': 'authorityAdapter',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'depositSolToPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'amountOfOrders',
          'type': 'u64',
        },
      ],
      'returns': None,
    },
    {
      'name': 'validateNft',
      'accounts': [
        {
          'name': 'nftValidationAdapter',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'validationWhitelist',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'depositNftToPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'initializeHadoMarket',
      'accounts': [
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'validationAdapterProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pairTokenMint',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'finishHadoMarket',
      'accounts': [
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'addClassicWhitelistToMarket',
      'accounts': [
        {
          'name': 'validationWhitelist',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'whitelistedAddress',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'whitelistType',
          'type': {
            'defined': 'NftValidationWhitelistType',
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'depositLiquidityToPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'putPairOnMarket',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'buyNftFromPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'assetReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'protocolFeeReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'maxAmountToPay',
          'type': 'u64',
        },
        {
          'name': 'skipFailed',
          'type': 'bool',
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'sellNftToTokenToNftPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'assetReceiverTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'assetReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'protocolFeeReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'minAmountToGet',
          'type': 'u64',
        },
        {
          'name': 'skipFailed',
          'type': 'bool',
        },
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'sellNftToLiquidityPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'newVaultTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'protocolFeeReceiver',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'minAmountToGet',
          'type': 'u64',
        },
        {
          'name': 'skipFailed',
          'type': 'bool',
        },
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawSolFromPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'quantityOfOrders',
          'type': 'u64',
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawNftFromPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityFromBalancedPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'modifyPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'params',
          'type': {
            'defined': 'PairParams',
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityFromBuyOrdersPair',
      'accounts': [
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityFromSellOrdersPair',
      'accounts': [
        {
          'name': 'nftPairBoxFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftMintFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccountFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccountFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftPairBoxSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfoFirst',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfoFirst',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecordFirst',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecordFirst',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'editionInfoSecond',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfoSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecordSecond',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecordSecond',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMintSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccountSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccountSecond',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityOrderVirtualFees',
      'accounts': [
        {
          'name': 'liquidityProvisionOrder',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeVirtualNftSwapPair',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'withdrawVirtualFees',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeNftPairBox',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeLiquidityProvisionOrder',
      'accounts': [
        {
          'name': 'liquidityProvisionOrder',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'customValidateNft',
      'accounts': [
        {
          'name': 'nftValidationAdapter',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'hadoMarket',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'whitelistedAddress',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'adapterProgramSigner',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'duration',
          'type': 'u64',
        },
        {
          'name': 'nftValidationWhitelistType',
          'type': {
            'defined': 'NftValidationWhitelistType',
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'modifyHadoMarket',
      'accounts': [
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'validationAdapterProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'addMerkleTreeWhitelist',
      'accounts': [
        {
          'name': 'nftValidationAdapter',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'hadoMarket',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'root',
          'type': {
            'array': ['u8', 32],
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'closeNftValidationAdapter',
      'accounts': [
        {
          'name': 'nftValidationAdapter',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeClassicWhitelist',
      'accounts': [
        {
          'name': 'validationWhitelist',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'closeNftValidationAdapterV2',
      'accounts': [
        {
          'name': 'nftValidationAdapterV2',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'admin',
          'isMut': True,
          'isSigner': True,
        },
      ],
      'args': [],
      'returns': None,
    },
    {
      'name': 'withdrawOutstandingTokensByAdmin',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'depositLiquidityOnlyBuyOrders',
      'accounts': [
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'quantityOfOrders',
          'type': 'u64',
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawLiquidityOnlyBuyOrders',
      'accounts': [
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'quantityOfOrders',
          'type': 'u64',
        },
      ],
      'returns': None,
    },
    {
      'name': 'depositLiquiditySingleSellToPair',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftValidationAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'proof',
          'type': {
            'vec': {
              'array': ['u8', 32],
            },
          },
        },
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
    {
      'name': 'withdrawLiquiditySingleSellOrder',
      'accounts': [
        {
          'name': 'nftPairBox',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftMint',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'vaultNftTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'nftUserTokenAccount',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'authorityAdapter',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'pair',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'user',
          'isMut': True,
          'isSigner': True,
        },
        {
          'name': 'nftsOwner',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'feeSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'fundsSolVault',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'editionInfo',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataInfo',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'ownerTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'destTokenRecord',
          'isMut': True,
          'isSigner': False,
        },
        {
          'name': 'instructions',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'authorizationRulesProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'tokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'associatedTokenProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'systemProgram',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'rent',
          'isMut': False,
          'isSigner': False,
        },
        {
          'name': 'metadataProgram',
          'isMut': False,
          'isSigner': False,
        },
      ],
      'args': [
        {
          'name': 'authorizationData',
          'type': {
            'option': {
              'defined': 'AuthorizationDataLocal',
            },
          },
        },
      ],
      'returns': None,
    },
  ],
  'accounts': [
    {
      'name': 'adapterWhitelist',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'whitelistedAdapterProgram',
            'type': 'publicKey',
          },
          {
            'name': 'adapterType',
            'type': {
              'defined': 'AdapterType',
            },
          },
        ],
      },
    },
    {
      'name': 'authorityAdapter',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'authorityAdapterProgram',
            'type': 'publicKey',
          },
          {
            'name': 'authorityOwner',
            'type': 'publicKey',
          },
          {
            'name': 'authorityType',
            'type': {
              'defined': 'AuthorityAdapterType',
            },
          },
          {
            'name': 'expiringAt',
            'type': 'u64',
          },
          {
            'name': 'authorityState',
            'type': {
              'defined': 'AuthorityState',
            },
          },
        ],
      },
    },
    {
      'name': 'classicValidationWhitelist',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'hadoMarket',
            'type': 'publicKey',
          },
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'whitelistType',
            'type': {
              'defined': 'NftValidationWhitelistType',
            },
          },
          {
            'name': 'whitelistedAddress',
            'type': 'publicKey',
          },
        ],
      },
    },
    {
      'name': 'hadoMarket',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'marketAuthority',
            'type': 'publicKey',
          },
          {
            'name': 'marketState',
            'type': {
              'defined': 'MarketState',
            },
          },
          {
            'name': 'marketTrustType',
            'type': {
              'defined': 'MarketTrustType',
            },
          },
          {
            'name': 'pairValidationType',
            'type': {
              'defined': 'PairValidationType',
            },
          },
          {
            'name': 'validationAdapterProgram',
            'type': 'publicKey',
          },
          {
            'name': 'pairTokenType',
            'type': {
              'defined': 'PairTokenType',
            },
          },
          {
            'name': 'pairTokenMint',
            'type': 'publicKey',
          },
        ],
      },
    },
    {
      'name': 'liquidityProvisionOrder',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'nftSwapPair',
            'type': 'publicKey',
          },
          {
            'name': 'lpOrderState',
            'type': {
              'defined': 'LpOrderState',
            },
          },
          {
            'name': 'orderACounter',
            'type': 'i64',
          },
          {
            'name': 'orderBCounter',
            'type': 'i64',
          },
          {
            'name': 'accumulatedFee',
            'type': 'u64',
          },
          {
            'name': 'lpTokenMint',
            'type': 'publicKey',
          },
          {
            'name': 'liquidityFeeBump',
            'type': 'u8',
          },
          {
            'name': 'createdAt',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'nftPairBox',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'nftMint',
            'type': 'publicKey',
          },
          {
            'name': 'nftMetadata',
            'type': 'publicKey',
          },
          {
            'name': 'nftBoxType',
            'type': {
              'defined': 'NftBoxType',
            },
          },
          {
            'name': 'vaultTokenAccount',
            'type': 'publicKey',
          },
          {
            'name': 'status',
            'type': {
              'defined': 'NftBoxState',
            },
          },
        ],
      },
    },
    {
      'name': 'nftSwapPair',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'hadoMarket',
            'type': 'publicKey',
          },
          {
            'name': 'pairType',
            'type': {
              'defined': 'PairType',
            },
          },
          {
            'name': 'pairState',
            'type': {
              'defined': 'PairState',
            },
          },
          {
            'name': 'pairAuthorityType',
            'type': {
              'defined': 'PairAuthorityType',
            },
          },
          {
            'name': 'pairAuthorityAdapterProgram',
            'type': 'publicKey',
          },
          {
            'name': 'lpTokensMint',
            'type': 'publicKey',
          },
          {
            'name': 'lpTokensInCirculation',
            'type': 'u64',
          },
          {
            'name': 'bondingCurve',
            'type': {
              'defined': 'BondingCurve',
            },
          },
          {
            'name': 'baseSpotPrice',
            'type': 'u64',
          },
          {
            'name': 'fee',
            'type': 'u64',
          },
          {
            'name': 'mathCounter',
            'type': 'i64',
          },
          {
            'name': 'currentSpotPrice',
            'type': 'u64',
          },
          {
            'name': 'feeTokenAccount',
            'type': 'publicKey',
          },
          {
            'name': 'feeVaultSeed',
            'type': 'u8',
          },
          {
            'name': 'solOrTokenFeeAmount',
            'type': 'u64',
          },
          {
            'name': 'fundsTokenAccount',
            'type': 'publicKey',
          },
          {
            'name': 'fundsSolVaultSeed',
            'type': 'u8',
          },
          {
            'name': 'fundsSolOrTokenBalance',
            'type': 'u64',
          },
          {
            'name': 'initialFundsSolOrTokenBalance',
            'type': 'u64',
          },
          {
            'name': 'buyOrdersQuantity',
            'type': 'u64',
          },
          {
            'name': 'nftsSeed',
            'type': 'u8',
          },
          {
            'name': 'nftsCount',
            'type': 'u64',
          },
          {
            'name': 'lastTransactedAt',
            'type': 'u64',
          },
          {
            'name': 'concentrationIndex',
            'type': 'u64',
          },
          {
            'name': 'assetReceiver',
            'type': 'publicKey',
          },
        ],
      },
    },
    {
      'name': 'nftValidationAdapterV2',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'hadoMarket',
            'type': 'publicKey',
          },
          {
            'name': 'scopeType',
            'type': {
              'defined': 'ScopeType',
            },
          },
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationProgram',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationWhitelistType',
            'type': {
              'defined': 'NftValidationWhitelistTypeV2',
            },
          },
          {
            'name': 'whitelistedAddress',
            'type': 'publicKey',
          },
          {
            'name': 'root',
            'type': {
              'array': ['u8', 32],
            },
          },
          {
            'name': 'nftValidationDurationType',
            'type': {
              'defined': 'NftValidationDurationType',
            },
          },
          {
            'name': 'validUntil',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'nftValidationAdapter',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'hadoMarket',
            'type': 'publicKey',
          },
          {
            'name': 'scopeType',
            'type': {
              'defined': 'ScopeType',
            },
          },
          {
            'name': 'pair',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationProgram',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationWhitelistType',
            'type': {
              'defined': 'NftValidationWhitelistType',
            },
          },
          {
            'name': 'whitelistedAddress',
            'type': 'publicKey',
          },
          {
            'name': 'nftValidationDurationType',
            'type': {
              'defined': 'NftValidationDurationType',
            },
          },
          {
            'name': 'validUntil',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'protocolAdminMultisig',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'protocolSettings',
            'type': 'publicKey',
          },
          {
            'name': 'admin',
            'type': 'publicKey',
          },
          {
            'name': 'weight',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'protocolSettingsV1',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'protocolFee',
            'type': 'u64',
          },
          {
            'name': 'protocolFeeMultiplier',
            'type': 'u64',
          },
          {
            'name': 'maxFee',
            'type': 'u64',
          },
          {
            'name': 'protocolFeeReceiver',
            'type': 'publicKey',
          },
          {
            'name': 'adminThresholdAmountMultisig',
            'type': 'u64',
          },
        ],
      },
    },
  ],
  'types': [
    {
      'name': 'PairParams',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'delta',
            'type': 'u64',
          },
          {
            'name': 'spotPrice',
            'type': 'u64',
          },
          {
            'name': 'fee',
            'type': 'u64',
          },
        ],
      },
    },
    {
      'name': 'PairBumps',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'fundsSolVaultSeed',
            'type': 'u8',
          },
          {
            'name': 'feeVaultSeed',
            'type': 'u8',
          },
          {
            'name': 'nftsSeed',
            'type': 'u8',
          },
        ],
      },
    },
    {
      'name': 'BondingCurve',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'delta',
            'type': 'u64',
          },
          {
            'name': 'bondingType',
            'type': {
              'defined': 'BondingCurveType',
            },
          },
        ],
      },
    },
    {
      'name': 'AuthorizationDataLocal',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'payload',
            'type': {
              'vec': {
                'defined': 'TaggedPayload',
              },
            },
          },
        ],
      },
    },
    {
      'name': 'TaggedPayload',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'name',
            'type': 'string',
          },
          {
            'name': 'payload',
            'type': {
              'defined': 'PayloadTypeLocal',
            },
          },
        ],
      },
    },
    {
      'name': 'SeedsVecLocal',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'seeds',
            'type': {
              'vec': 'bytes',
            },
          },
        ],
      },
    },
    {
      'name': 'ProofInfoLocal',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'proof',
            'type': {
              'vec': {
                'array': ['u8', 32],
              },
            },
          },
        ],
      },
    },
    {
      'name': 'AdapterType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Validation',
          },
          {
            'name': 'Authority',
          },
          {
            'name': 'Partial',
          },
        ],
      },
    },
    {
      'name': 'AuthorityAdapterType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'OneTime',
          },
          {
            'name': 'Persistent',
          },
        ],
      },
    },
    {
      'name': 'AuthorityState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Active',
          },
          {
            'name': 'Used',
          },
          {
            'name': 'Expired',
          },
          {
            'name': 'Revoked',
          },
        ],
      },
    },
    {
      'name': 'MarketTrustType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Unverified',
          },
          {
            'name': 'Verified',
          },
        ],
      },
    },
    {
      'name': 'MarketState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Initializing',
          },
          {
            'name': 'Available',
          },
        ],
      },
    },
    {
      'name': 'PairValidationType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'ClassicValidation',
          },
          {
            'name': 'CustomValidation',
          },
        ],
      },
    },
    {
      'name': 'PairTokenType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'NativeSol',
          },
          {
            'name': 'Spl',
          },
        ],
      },
    },
    {
      'name': 'LpOrderState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Virtual',
          },
          {
            'name': 'Tokenized',
          },
          {
            'name': 'WithdrawnVirtual',
          },
          {
            'name': 'WithdrawnTokenized',
          },
        ],
      },
    },
    {
      'name': 'NftBoxState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Closed',
          },
          {
            'name': 'Active',
          },
        ],
      },
    },
    {
      'name': 'NftBoxType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Escrow',
          },
          {
            'name': 'Escrowless',
          },
        ],
      },
    },
    {
      'name': 'PairType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'TokenForNft',
          },
          {
            'name': 'NftForToken',
          },
          {
            'name': 'LiquidityProvision',
          },
        ],
      },
    },
    {
      'name': 'PairState',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Initializing',
          },
          {
            'name': 'OnMarketVirtual',
          },
          {
            'name': 'OnMarketTokenized',
          },
          {
            'name': 'Frozen',
          },
        ],
      },
    },
    {
      'name': 'PairAuthorityType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'ClassicAuthority',
          },
          {
            'name': 'CustomAuthority',
          },
        ],
      },
    },
    {
      'name': 'PartialSettings',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'None',
          },
          {
            'name': 'CustomPartial',
          },
        ],
      },
    },
    {
      'name': 'BondingCurveType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Linear',
          },
          {
            'name': 'Exponential',
          },
          {
            'name': 'XYK',
          },
        ],
      },
    },
    {
      'name': 'NftValidationWhitelistTypeV2',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Creator',
          },
          {
            'name': 'Nft',
          },
          {
            'name': 'MerkleTree',
          },
        ],
      },
    },
    {
      'name': 'ScopeType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Market',
          },
          {
            'name': 'Pair',
          },
        ],
      },
    },
    {
      'name': 'NftValidationDurationType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Finite',
          },
          {
            'name': 'Infinite',
          },
        ],
      },
    },
    {
      'name': 'NftValidationWhitelistType',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Creator',
          },
          {
            'name': 'Nft',
          },
        ],
      },
    },
    {
      'name': 'PayloadTypeLocal',
      'type': {
        'kind': 'enum',
        'variants': [
          {
            'name': 'Pubkey',
            'fields': ['publicKey'],
          },
          {
            'name': 'Seeds',
            'fields': [
              {
                'defined': 'SeedsVecLocal',
              },
            ],
          },
          {
            'name': 'MerkleProof',
            'fields': [
              {
                'defined': 'ProofInfoLocal',
              },
            ],
          },
          {
            'name': 'Number',
            'fields': ['u64'],
          },
        ],
      },
    },
  ],
  'errors': [
    {
      'code': 6000,
      'name': 'MetadataDoesntExist',
      'msg': 'MetadataDoesntExist',
    },
    {
      'code': 6001,
      'name': 'DerivedKeyInvalid',
      'msg': 'DerivedKeyInvalid',
    },
    {
      'code': 6002,
      'name': 'InvalidCollectionDetails',
      'msg': 'InvalidCollectionDetails',
    },
    {
      'code': 6003,
      'name': 'InvalidCollection',
      'msg': 'InvalidCollection',
    },
    {
      'code': 6004,
      'name': 'InvalidCollectionMint',
      'msg': 'InvalidCollectionMint',
    },
    {
      'code': 6005,
      'name': 'NftNotVerified',
      'msg': 'NftNotVerified',
    },
    {
      'code': 6006,
      'name': 'InvalidOwner',
      'msg': 'InvalidOwner',
    },
    {
      'code': 6007,
      'name': 'InvalidDelta',
      'msg': 'InvalidDelta',
    },
    {
      'code': 6008,
      'name': 'InvalidFee',
      'msg': 'InvalidFee',
    },
    {
      'code': 6009,
      'name': 'InvalidPairType',
      'msg': 'InvalidPairType',
    },
    {
      'code': 6010,
      'name': 'NotEnoughInTokenAccount',
      'msg': 'NotEnoughInTokenAccount',
    },
    {
      'code': 6011,
      'name': 'InvalidMint',
      'msg': 'InvalidMint',
    },
    {
      'code': 6012,
      'name': 'InvalidSolVault',
      'msg': 'InvalidSolVault',
    },
    {
      'code': 6013,
      'name': 'InvalidFundingAmount',
      'msg': 'InvalidFundingAmount',
    },
    {
      'code': 6014,
      'name': 'NotEnoughLamports',
      'msg': 'NotEnoughLamports',
    },
    {
      'code': 6015,
      'name': 'InvalidJpegOwner',
      'msg': 'InvalidJpegOwner',
    },
    {
      'code': 6016,
      'name': 'InvalidTokenAccount',
      'msg': 'InvalidTokenAccount',
    },
    {
      'code': 6017,
      'name': 'InvalidPayer',
      'msg': 'InvalidPayer',
    },
    {
      'code': 6018,
      'name': 'ShouldBeActive',
      'msg': 'ShouldBeActive',
    },
    {
      'code': 6019,
      'name': 'CantMakeZeroOrders',
      'msg': "Can't make 0 orders",
    },
    {
      'code': 6020,
      'name': 'OnlyClassicAuthority',
      'msg': 'OnlyClassicAuthority',
    },
    {
      'code': 6021,
      'name': 'NotValidAuthorityAdapter',
      'msg': 'NotValidAuthorityAdapter',
    },
    {
      'code': 6022,
      'name': 'UserDoesntHaveAuthority',
      'msg': 'UserDoesntHaveAuthority',
    },
    {
      'code': 6023,
      'name': 'WrongSeed',
      'msg': 'WrongSeed',
    },
    {
      'code': 6024,
      'name': 'CanDepositSolOnlyToTokenToNft',
      'msg': 'CanDepositSolOnlyToTokenToNft',
    },
    {
      'code': 6025,
      'name': 'MaxAmountOfOrdersSucceeded',
      'msg': 'MaxAmountOfOrdersSucceeded',
    },
    {
      'code': 6026,
      'name': 'CanDepositNftOnlyToNftToToken',
      'msg': 'CanDepositNftOnlyToNftToToken',
    },
    {
      'code': 6027,
      'name': 'TokenAccountDoesntContainNft',
      'msg': 'TokenAccountDoesntContainNft',
    },
    {
      'code': 6028,
      'name': 'MarketAuthorityIncorrect',
      'msg': 'MarketAuthorityIncorrect',
    },
    {
      'code': 6029,
      'name': 'CanAddWhitelistOnlyToInitializingMarket',
      'msg': 'CanAddWhitelistOnlyToInitializingMarket',
    },
    {
      'code': 6030,
      'name': 'CanPutPairsOnlyToAvailableMarkets',
      'msg': 'CanPutPairsOnlyToAvailableMarkets',
    },
    {
      'code': 6031,
      'name': 'PairAndNftValidationMarketDoesntMatch',
      'msg': 'PairAndNftValidationMarketDoesntMatch',
    },
    {
      'code': 6032,
      'name': 'OnlyMarketScopeSupported',
      'msg': 'OnlyMarketScopeSupported',
    },
    {
      'code': 6033,
      'name': 'NotWhitelistedNftForThisMarket',
      'msg': 'NotWhitelistedNftForThisMarket',
    },
    {
      'code': 6034,
      'name': 'CanDepositOnlyToLiquidityProvision',
      'msg': 'CanDepositOnlyToLiquidityProvision',
    },
    {
      'code': 6035,
      'name': 'NftBoxDoesntMatchPair',
      'msg': 'NftBoxDoesntMatchPair',
    },
    {
      'code': 6036,
      'name': 'NftBoxShouldBeActive',
      'msg': 'NftBoxShouldBeActive',
    },
    {
      'code': 6037,
      'name': 'NftBoxDoesntMatchMint',
      'msg': 'NftBoxDoesntMatchMint',
    },
    {
      'code': 6038,
      'name': 'CantBuyNftFromTokenForNft',
      'msg': 'CantBuyNftFromTokenForNft',
    },
    {
      'code': 6039,
      'name': 'OnlyTokenForNftIsEligibleForThisSell',
      'msg': 'OnlyTokenForNftIsEligibleForThisSell',
    },
    {
      'code': 6040,
      'name': 'NoBuyOrdersOnThisPair',
      'msg': 'NoBuyOrdersOnThisPair',
    },
    {
      'code': 6041,
      'name': 'OnlyLiquidityProvisionIsEligibleForThisSell',
      'msg': 'OnlyLiquidityProvisionIsEligibleForThisSell',
    },
    {
      'code': 6042,
      'name': 'OnlyTokenForNftIsEligibleForThisWithdrawal',
      'msg': 'OnlyTokenForNftIsEligibleForThisWithdrawal',
    },
    {
      'code': 6043,
      'name': 'OnlyNftForTokenIsEligibleForThisWithdrawal',
      'msg': 'OnlyNftForTokenIsEligibleForThisWithdrawal',
    },
    {
      'code': 6044,
      'name': 'OnlyLiquidityProvisionIsEligibleForThisWithdrawal',
      'msg': 'OnlyLiquidityProvisionIsEligibleForThisWithdrawal',
    },
    {
      'code': 6045,
      'name': 'InstructionIsNotSupported',
      'msg': 'InstructionIsNotSupported',
    },
    {
      'code': 6046,
      'name': 'CanTradeOnlyWithPairsOnMarket',
      'msg': 'CanTradeOnlyWithPairsOnMarket',
    },
    {
      'code': 6047,
      'name': 'NoLiquidityFeesToWithdraw',
      'msg': 'NoLiquidityFeesToWithdraw',
    },
    {
      'code': 6048,
      'name': 'MaxAmountToPayExceeded',
      'msg': 'MaxAmountToPayExceeded',
    },
    {
      'code': 6049,
      'name': 'GettingLessThanMinAmountToGet',
      'msg': 'GettingLessThanMinAmountToGet',
    },
    {
      'code': 6050,
      'name': 'UserDoesntHaveHadomarketAuthority',
      'msg': 'UserDoesntHaveHadomarketAuthority',
    },
    {
      'code': 6051,
      'name': 'HadomarketAlreadyFinished',
      'msg': 'HadomarketAlreadyFinished',
    },
    {
      'code': 6052,
      'name': 'CanDepositLiqudityOnlyToVirtualOrInitializingPairs',
      'msg': 'CanDepositLiqudityOnlyToVirtualOrInitializingPairs',
    },
    {
      'code': 6053,
      'name': 'CanModifyOnlyToVirtualOrInitializingPairs',
      'msg': 'CanModifyOnlyToVirtualOrInitializingPairs',
    },
    {
      'code': 6054,
      'name': 'LiquidityProvisionOrderPairDoesntMatch',
      'msg': 'LiquidityProvisionOrderPairDoesntMatch',
    },
    {
      'code': 6055,
      'name': 'OnlyVirtualLpOrdersCanBeWithdrawnByThisFunction',
      'msg': 'OnlyVirtualLpOrdersCanBeWithdrawnByThisFunction',
    },
    {
      'code': 6056,
      'name': 'OnlyVirtualOrTokenizedLpOrdersCanBeReplacedByThisFunction',
      'msg': 'OnlyVirtualOrTokenizedLpOrdersCanBeReplacedByThisFunction',
    },
    {
      'code': 6057,
      'name': 'LiquidityProvisionOrderNotEdge',
      'msg': 'LiquidityProvisionOrderNotEdge',
    },
    {
      'code': 6058,
      'name': 'NftPairBoxNotParsingFromRemaining',
      'msg': 'NftPairBoxNotParsingFromRemaining',
    },
    {
      'code': 6059,
      'name': 'VaultNftTokenAccountNotParsingFromRemaining',
      'msg': 'VaultNftTokenAccountNotParsingFromRemaining',
    },
    {
      'code': 6060,
      'name': 'UserTokenAccountNotParsingFromRemaining',
      'msg': 'UserTokenAccountNotParsingFromRemaining',
    },
    {
      'code': 6061,
      'name': 'WithdrawingOnlyAtLeastOneBuyAndOneSellPairs',
      'msg': 'WithdrawingOnlyAtLeastOneBuyAndOneSellPairs',
    },
    {
      'code': 6062,
      'name': 'VaultDoesntMatchBox',
      'msg': 'VaultDoesntMatchBox',
    },
    {
      'code': 6063,
      'name': 'WithdrawingOnlyBuyOrdersPairs',
      'msg': 'WithdrawingOnlyBuyOrdersPairs',
    },
    {
      'code': 6064,
      'name': 'WithdrawingOnlySellOrdersPairs',
      'msg': 'WithdrawingOnlySellOrdersPairs',
    },
    {
      'code': 6065,
      'name': 'LiquidityProvisionOrderIsWithdrawn',
      'msg': 'LiquidityProvisionOrderIsWithdrawn',
    },
    {
      'code': 6066,
      'name': 'LiquidityProvisionOrderIsNotCorrectOrderForPair',
      'msg': 'LiquidityProvisionOrderIsNotCorrectOrderForPair',
    },
    {
      'code': 6067,
      'name': 'OnlyMarketVirtualPairsCanBeTokenized',
      'msg': 'OnlyMarketVirtualPairsCanBeTokenized',
    },
    {
      'code': 6068,
      'name': 'OnlyLiquidityProvisionPairsCanBeTokenized',
      'msg': 'OnlyLiquidityProvisionPairsCanBeTokenized',
    },
    {
      'code': 6069,
      'name': 'OnlyInitializingPairsCanBePutOnMarket',
      'msg': 'OnlyInitializingPairsCanBePutOnMarket',
    },
    {
      'code': 6070,
      'name': 'CanMakeLpOrderTokenizedOnlyFromTokenizedPair',
      'msg': 'CanMakeLpOrderTokenizedOnlyFromTokenizedPair',
    },
    {
      'code': 6071,
      'name': 'OnlyVirtualLpOrderCanBeTokenized',
      'msg': 'OnlyVirtualLpOrderCanBeTokenized',
    },
    {
      'code': 6072,
      'name': 'OnlyTokenizedLpOrdersCanWithdrawFees',
      'msg': 'OnlyTokenizedLpOrdersCanWithdrawFees',
    },
    {
      'code': 6073,
      'name': 'UserLpTokenAccountDoesntContainNft',
      'msg': 'UserLpTokenAccountDoesntContainNft',
    },
    {
      'code': 6074,
      'name': 'OnlyTokenizedLpOrdersCanBeWithdrawnByThisFunction',
      'msg': 'OnlyTokenizedLpOrdersCanBeWithdrawnByThisFunction',
    },
    {
      'code': 6075,
      'name': 'LpTokenMintDoesntMatchOrder',
      'msg': 'LpTokenMintDoesntMatchOrder',
    },
    {
      'code': 6076,
      'name': 'CanCloseVirtualPoolOnlyIfNoLiquidityLeft',
      'msg': 'CanCloseVirtualPoolOnlyIfNoLiquidityLeft',
    },
    {
      'code': 6077,
      'name': 'NftIsNotMasterEdition',
      'msg': 'NftIsNotMasterEdition',
    },
    {
      'code': 6078,
      'name': 'NftPairBoxNotClosed',
      'msg': 'NftPairBoxNotClosed',
    },
    {
      'code': 6079,
      'name': 'WrongAdmin',
      'msg': 'WrongAdmin',
    },
    {
      'code': 6080,
      'name': 'PairScopeValidationNotSupportedForNow',
      'msg': 'PairScopeValidationNotSupportedForNow',
    },
    {
      'code': 6081,
      'name': 'CustomValidationAdapterProgramDoesntMatchUser',
      'msg': 'CustomValidationAdapterProgramDoesntMatchUser',
    },
    {
      'code': 6082,
      'name': 'ClassicAuthorityWorksIfValidationProgramIsHadeswap',
      'msg': 'ClassicAuthorityWorksIfValidationProgramIsHadeswap',
    },
    {
      'code': 6083,
      'name': 'NftValidationAdapterV2CanWhitelistOnlyMerkleTree',
      'msg': 'NftValidationAdapterV2CanWhitelistOnlyMerkleTree',
    },
    {
      'code': 6084,
      'name': 'BadRuleSet',
      'msg': 'BadRuleSet',
    },
    {
      'code': 6085,
      'name': 'WrongCreatorInRemainingAccounts',
      'msg': 'WrongCreatorInRemainingAccounts',
    },
  ],
}