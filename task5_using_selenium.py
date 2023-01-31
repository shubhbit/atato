from selenium import webdriver
from selenium.webdriver.common.by import By


def find_oldest_mined_block(driver):
    """
    this function starts iterating from last ever page and checks for each block on 
    the page in reverse order to check whether the block has any transactions.
    if there is no block in the current page with transaction then move to  
    previous page and repeat the steps again until a block is found with transaction
    """
    page = 1
    old_page = 1
    print("finding oldest mined block..")
    while True:
        block_table = driver.find_element(By.XPATH, '//table')
        for row in block_table.find_elements(By.CSS_SELECTOR, 'tr')[::-1]:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) > 0:
                if int(columns[3].text) > 0:
                    print("oldest mined block of goerli testnet: ",
                          columns[0].text)
                    return

        # change page to previous
        old_page = page
        page += 1
        print("oldest mined block is not found on page: {}, moving to to page: {}".format(
            old_page, page))
        driver.find_element(By.PARTIAL_LINK_TEXT, "Previous").click()


if __name__ == "__main__":
    try:
        driver = webdriver.Firefox()

        driver.get("https://goerli.etherscan.io/blocks")
        print("navigating to the last ever page on etherscan..")
        driver.find_element(By.PARTIAL_LINK_TEXT, "Last").click()
        find_oldest_mined_block(driver)
    except Exception as e:
        print(e)
    finally:
        driver.close()
