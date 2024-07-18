from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_customers(driver, search_term):
    try:
        search_box = driver.find_element(By.XPATH, '//input[@aria-label="Search Facebook"]')
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Error performing search: {e}")
        driver.quit()
        exit()
