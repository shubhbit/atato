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
- install dependencies using below command:
  > python3 -m pip install -r requirements.txt
- script is present in current folder with name: "task2_get_latest_block.py"
- script could be run as below:
  > python3 task2_get_latest_block.py

# Task-3
- code for task#3 is contained inside folder : "task3" available in current folder
- folder structure is as below:
- task3/app/booking.py. => this is a python file which contains a class called Booking which represents Booking object, it has methods such as create_booking, get_booking, delete_booking. It makes use of "requests" library of python to call http requests.
- task3/test/conftest.py. => this is conftest file which contsins setup before test and teardown after test.
- task3/test/test_booking.py. => 
