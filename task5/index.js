// oldest mined block can be found using following two ways:
// 1. open https://goerli.etherscan.io/ on browser and keep in scrolling down page to find a block which is oldest and mined(with transaction)
//     this way is not feasible as there would be very large amount of blocks available to explore them manually.

// 2. second way is to do it programmatically , using web3 library of Javascript
//    create a project on infura to get project id for goerli testnet ChannelSplitterNode
//    and write a javascript code to make a connection.
//    start iterating from block#1 and keep iterating until you find a block with transaction lenght > 0.
//    this will be the first block is mined(having transactions).
//    implementing a js code for the same

const Web3 = require("web3");

// url to connect to goerli testnet

// put your project-id in below url

url = "https://goerli.infura.io/v3/<project-id>";

const web3 = new Web3(url);

let blockNumber = 1;
let oldestBlock = null;

async function getOldestMinedBlock() {
  while (true) {
    let block = await web3.eth.getBlock(blockNumber);
    if (block.transactions.length > 0) {
        oldestBlock = block
        break
    }
    blockNumber++;
  }
  console.log(`oldest minded bock is : ${oldestBlock}`)
}
getOldestMinedBlock();
