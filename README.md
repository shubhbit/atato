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
- task3/test/test_booking.py. => this is actual test file which contains a test class and test functions inside which verifies creation of booking, getting booking, deletion of booking, deleted booking can not be fetched etc. tests are written using "pytest" framework.
- to run the tests, execute below command from current folder:
  > python3 -m pytest

- Output: 
plugins: dependency-0.5.1, web3-5.31.3, anyio-3.6.2
collected 3 items                                                                                                                      

task3/test/test_booking.py ...                                                                                                   [100%]

========================================================== 3 passed in 10.30s ==========================================================

# Task-4
- test cases for task-4(serch service ui) can be found in a file "task4.pdf" in the current folder.


# Task-5
- I have written a javascript code to fetch the oldest mined block of "goerli testnet chain" using "web3.js" library
- making a connection to Web3 using url : ""https://goerli.infura.io/v3/<project-id>"", where project ID can be fetched from infura projects
- once we get the connection handle, we are recursively trying to get blocks starting from block_num 1, using web3.eth.getBlock(block_num) function
- and checking transactions lenght for eatch block, if we get a block where length of transaction is greater than zero, exit the infinite loop and that's the oldest block which is mined(having transaction.)
- this code is put inside folder task5 present in the current folder.
- to execute the code, goto flder task5
  > cd task5
- install dependencies,
  > npm install
- once dependencies are installed, execute below command to run:
  > npde index.js
