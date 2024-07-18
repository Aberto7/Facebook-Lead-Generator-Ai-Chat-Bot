from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Utilities.openai_module import get_response 

def handle_messages(driver):
    try:
        profiles = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="browse-result-content"]')
    except Exception as e:
        print(f"Error locating search results: {e}")
        driver.quit()
        exit()

    for profile in profiles:
        try:
            profile.click()
            time.sleep(2)  # Wait for the profile/page to load
        except Exception as e:
            print(f"Error clicking on profile: {e}")
            continue

        try:
            message_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Message"]')
            message_button.click()

            message_box = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Message"]')
            message_box.send_keys('Hello! We are offering exclusive digital marketing services to help you grow your business.')
            message_box.send_keys(Keys.RETURN)

            time.sleep(2)

            while True:
                try:
                    incoming_messages = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Messages"]')

                    for message in incoming_messages:
                        text = message.text
                        reply = get_response(text)

                        message_box = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Write a message..."]')
                        message_box.send_keys(reply)
                        message_box.send_keys(Keys.RETURN)

                    time.sleep(100)

                except Exception as e:
                    print(f"Error handling incoming messages: {e}")
                    break

        except Exception as e:
            print(f"Could not message profile: {e}")
            driver.back()
            time.sleep(2)
