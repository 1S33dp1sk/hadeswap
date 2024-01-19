# hadeswap
Hadeswap solana python3 


main testing 

Here's an example of how the current SDK is being used to create a pool (bid) and then deposit funds to the pool in order to activate the bid.

```js
  const userKeypair = await createKeypairFromFile(__dirname + '/keys/admin.json');
  const sendTxnUserDevnet = async (txn, signers) =>
    void (await devnetConnection.sendTransaction(txn, [userKeypair, ...signers]).catch((err) => console.log(err)));
  const programId = NEW_DEVNET_PROGRAM;
  // new anchor.web3.PublicKey('DFsZgwKM3SvkvMwVRPQhhEnkYZCS1hZ2g2u6ehmAWjyc');
  // console.log('userKeypair: ', userKeypair.publicKey.toBase58());
  const hadoMarket = new anchor.web3.PublicKey('Hd2Rx5cEvFojpBFTHeHXfk1tMNrbSKt1dhNK78LCXPqH');

  await hadeswap.functions.marketFactory.pair.virtual.mutations.initializePair({
    programId,
    connection: devnetConnection,
    args: {
      spotPrice: 1 * 1e9,
      delta: 0.2 * 1e9,
      bondingCurveType: hadeswap.types.BondingCurveType.Linear,
      fee: 0,
      pairType: hadeswap.types.PairType.TokenForNFT,
    },
    accounts: {
      hadoMarket: hadoMarket,
      userPubkey: userKeypair.publicKey,
    },
    sendTxn: sendTxnUserDevnet,
  });
```

```js
  const userKeypair = await createKeypairFromFile(__dirname + '/keys/admin.json');
  const sendTxnUserDevnet = async (txn, signers) =>
    void (await devnetConnection.sendTransaction(txn, [userKeypair, ...signers]).catch((err) => console.log(err)));
  const programId = new anchor.web3.PublicKey('DFsZgwKM3SvkvMwVRPQhhEnkYZCS1hZ2g2u6ehmAWjyc');
  // console.log('userKeypair: ', userKeypair.publicKey.toBase58());
  const allAccounts = await getAllProgramAccounts(programId, devnetConnection);

  const pair = new anchor.web3.PublicKey('FsE3egxUv3eiLDNLT6m4bu6s72dMTjGfYc4Xhk7Yd9rq');
  const authorityAdapter = allAccounts.authorityAdapters.find(
    (authority) => authority.authorityOwner === userKeypair.publicKey.toBase58() && authority.pair === pair.toBase58(),
  ).publicKey;
  await hadeswap.functions.marketFactory.pair.virtual.deposits.depositSolToPair({
    programId,
    connection: devnetConnection,
    args: {
      amountOfOrders: 6,
    },
    accounts: {
      pair: pair,
      authorityAdapter,
      userPubkey: userKeypair.publicKey,
    },
    sendTxn: sendTxnUserDevnet,
  });
```

In reality, we'll want to modify this slightly. We want to simplify it, by only isolating the instruction generating aspect, meaning, we'll want the data payload that the SDK generates and then handle the signing and transmitting separately on our own (meaning, it'd fall outside of this project to be done). Basically, when we call the deposits.depositSOLToPair, we supply the arguments to receive a bytes array. That's all we need, everything else related to keypairs, connections, and transmitting falls outside of the scope of this project and is something that you should omit.