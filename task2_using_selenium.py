from selenium import webdriver
from selenium.webdriver.common.by import By


def find_latest_block(driver):
    """
    this function tries to fetch first block on first page of goerli etherscan
    block on first page
    """
    block_table = driver.find_element(By.XPATH, '//table')
    for row in block_table.find_elements(By.CSS_SELECTOR, 'tr'):
        if len(row.find_elements(By.TAG_NAME, "td")) > 0:
            print("latest block number for Goerli Ethereum test network: ",
                  row.find_elements(By.TAG_NAME, "td")[0].text)
            break


if __name__ == "__main__":
    try:
        driver = webdriver.Firefox()
        driver.get("https://goerli.etherscan.io/blocks")
        find_latest_block(driver)
    except Exception as e:
        print(e)
    finally:
        driver.close()
