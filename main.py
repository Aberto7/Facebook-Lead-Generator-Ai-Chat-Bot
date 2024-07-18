from FB_Automation.login import login_to_facebook
from FB_Automation.Search import search_customers
from FB_Automation.messaging import handle_messages
from selenium import webdriver
import time

# Set up the Edge driver
driver = webdriver.Edge(executable_path='/path/to/edgedriver')
driver.get('https://www.facebook.com')  # Navigate to Facebook login page

your_facebook_email = ''  # Write Your Facebook email to Login to your Account
your_facebook_password = ''  # Write Your Facebook password to Login to your Account

try:
    login_to_facebook(driver, your_facebook_email, your_facebook_password)
    time.sleep(5)  # Wait for the page to load completely
    
    search_customers(driver, 'digital marketing services')
    time.sleep(5)  # Wait for the search results to load
    
    handle_messages(driver)
    
except Exception as e:
    print(f"Error during the process: {e}")
finally:
    driver.quit()  # Optionally, you can close the browser window at the end of your script
