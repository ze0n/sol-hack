import solana

// Step 1 - Define Review Inputs
const RESTAURANT = "Eats";
const AMOUNT = new anchor.BN(1);
//const AMOUNT = 5;
const REVIEW = "Always super fast!";

// Step 2 - Fetch the PDA of our Review account
const [GOAL_PDA] = await anchor.web3.PublicKey.findProgramAddress(
  [Buffer.from(RESTAURANT), pg.wallet.publicKey.toBuffer()],
  pg.program.programId
);

const [TEMP_FUND] = await anchor.web3.PublicKey.findProgramAddress(
  [Buffer.from("TEMP"), pg.wallet.publicKey.toBuffer()],
  pg.program.programId
);

const [LOSE_FUND] = await anchor.web3.PublicKey.findProgramAddress(
  [Buffer.from("LOSE"), pg.wallet.publicKey.toBuffer()],
  pg.program.programId
);

console.log(`Reviewer: ${pg.wallet.publicKey.toString()}`);
console.log(`TEMP: ${TEMP_FUND.toString()}`);
console.log(`LOSE_FUND: ${LOSE_FUND.toString()}`);
console.log(`Review: ${GOAL_PDA.toString()}`);

// Step 3 - Fetch Latest Blockhash
let latestBlockhash = await pg.connection.getLatestBlockhash("finalized");
console.log(`BBB ${latestBlockhash}`);

// Step 4 - Send and Confirm the Transaction
const tx = await pg.program.methods
  .setGoal(RESTAURANT, AMOUNT)
  .accounts({ goal: GOAL_PDA, tempFund: TEMP_FUND, loseFund: LOSE_FUND })
  .rpc();

console.log(`CCC`);

console.log(`https://explorer.solana.com/tx/${tx}?cluster=devnet`);

await pg.connection.confirmTransaction({
  signature: tx,
  blockhash: latestBlockhash.blockhash,
  lastValidBlockHeight: latestBlockhash.lastValidBlockHeight,
});

console.log(`https://explorer.solana.com/tx/${tx}?cluster=devnet`);

// Step 5 - Fetch the data account and log results
const data = await pg.program.account.goal.fetch(GOAL_PDA);
console.log(`Amount: `, data.amount.toString());
console.log(`Winner: `, data.winner);
console.log(`Loser: `, data.loser);


# from solathon.core.instructions import transfer
# from solathon import Client, Transaction, PublicKey, Keypair

# client = Client("https://api.devnet.solana.com")

# public_key = PublicKey("CgNcBAHD6tn2ynKDAsnnXAbHTWyuksY5LLh3dPebfrUm")

# balance = client.get_balance(public_key)
# print(balance)


# sender = Keypair.from_private_key("your_private_key")
# receiver = PublicKey("receiver_public_key")
# amount = 100  

# instruction = transfer(
#         from_public_key=sender.public_key,
#         to_public_key=receiver, 
#         lamports=100
#     )

# transaction = Transaction(instructions=[instruction], signers=[sender])

# result = client.send_transaction(transaction)
# print("Transaction response: ", result)


# import solana
# from solathon.core.instructions import transfer
# from solathon import Client, Transaction, PublicKey, Keypair

# from solana.rpc.api import Client

# sender = Keypair.from_private_key("you_private_key_here")
# receiver = PublicKey("receiver_public_key")
# amount = 100 

# instruction = transfer(
#         from_public_key=sender.public_key,
#         to_public_key=receiver, 
#         lamports=100
#     )

# transaction = Transaction(instructions=[instruction], signers=[sender])

# result = client.send_transaction(transaction)
# print("Transaction result: ", result)

# client = Client("https://api.devnet.solana.com")

# params = {
#     "address": "CgNcBAHD6tn2ynKDAsnnXAbHTWyuksY5LLh3dPebfrUm",
#     "network": body["network"]
#     }
# result = sol_api.account.balance(
#     api_key= moralis_api_key,
#     params = params
# )


# acc = client.get_account_info("CgNcBAHD6tn2ynKDAsnnXAbHTWyuksY5LLh3dPebfrUm")
# print(acc)