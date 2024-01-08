from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver (You'll need to download chromedriver.exe and specify its path)
driver = webdriver.Chrome()
load_dotenv()
username = os.getenv("USERNAMEYOUTUBE")
password = os.getenv("PASSWORDYOUTUBE")

# Open YouTube.com
driver.get("https://www.youtube.com")

# Optional: You can add additional code here to interact with the webpage
sign_in_button = driver.find_element(By.XPATH, "//a[contains(@href,'/account')]")  # XPath may vary, adjust if necessary
sign_in_button.click()


username_field = driver.find_element(By.ID, "identifierId")  # Replace with the actual ID of the username field
# password_field = driver.find_element(By.NAME, "password")    # Replace with the actual name attribute of the password field

username_field.send_keys(username)
username_field.send_keys(Keys.RETURN)  # Press Enter after entering the username

# Wait for the "Next" element to become clickable
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@jsname='LgbsSe']//span[text()='Next']"))
)
# # Click the "Next" button
# next_button.click()
# # password_field.send_keys(password)
# # password_field.send_keys(Keys.RETURN)  # Press Enter after entering the password

# # Wait for the page to stabilize or for a specific element to be visible, clickable, etc.
# try:
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password' and @name='password']")))
#     # Replace "//element_after_click" with the XPath of an element that appears after the click action stabilizes the page
# except Exception as e:
#     print("Exception occurred:", e)
breakpoint()
# Close the browser when done
# driver.quit()