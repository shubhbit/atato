# Create any script with any language to get the latest block number for Goerli
# Ethereum test network: https://goerli.etherscan.io/

import requests, json



def get_latest_block(api_endpoint):
    print("URL: ", api_endpoint)
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        resp_json = json.loads(response.text)
        return int(resp_json['result'], 16)
    else:
        print("Get request failed with error: ", response.text)

if __name__ == "__main__":
    api_endpoint = "https://api-goerli.etherscan.io/api?module=proxy&action=eth_blockNumber"
    latest_block = get_latest_block(api_endpoint)
    print("latest block number for Goerli Ethereum test network: ",latest_block)