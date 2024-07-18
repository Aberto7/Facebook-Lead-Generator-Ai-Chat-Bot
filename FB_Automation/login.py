from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login_to_facebook(driver, email, password):
    try:
        username = driver.find_element(By.ID, 'email')  # Locate the username input field by its ID
        password_field = driver.find_element(By.ID, 'pass')  # Locate the password input field by its ID

        username.send_keys(email)  # Replace with your Facebook email
        password_field.send_keys(password)  # Replace with your Facebook password
        password_field.send_keys(Keys.RETURN)  # Press the Return key to log in

    except Exception as e:
        print(f"Error logging in: {e}")
        driver.quit()
        exit()
