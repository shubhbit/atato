# atato

# Task-1

- to identify the wallet address with given seed phrase, we could use any of the wallets such as "myetherWallet" or "metamask"
- I used "myetherWallet" and with the help of seed phrase I could find the wallet address in account info section,
- I aslo sent test eths to this address using one of the faucets
- wallet address is written in file called "task1.pdf" in the current folder.

# Task-2
- goerli.etherscan.io exposes APIs to fetch block details.
- I made use of requests library available in python to make http get request to api to fetch latest block
- api_endpoint used is : "https://api-goerli.etherscan.io/api?module=proxy&action=eth_blockNumber" (with appropriate query params to fetch latest block)
- 
