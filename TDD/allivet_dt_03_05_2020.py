from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# locators
MY_ACCNT_BTN = (By.XPATH, "//button[@class='btn btn-account one']")
SGN_IN_BTN = (By.XPATH, "//a[@href='/signin.aspx']")
EMAIL_FLD = (By.NAME, "EMail")
PSWD_FLD = (By.ID, "Password")
LGN_BTN = (By.ID, "LoginButton")
ALRT_TEXT = (By.ID, "ErrorPanel")

# Open the url
driver.get( 'https://www.allivet.com/' )
sleep(2)

# Click MY ACCOUNT button
driver.find_element( *MY_ACCNT_BTN ).click()

# Click Sign In button
driver.find_element( *SGN_IN_BTN ).click()

# Input into e-mail field TestEmail@gmail.com
e = driver.find_element( *EMAIL_FLD )
e.clear()
e.send_keys('TestEmail@gmail.com')
sleep(2)

# Input into password field TestPassword
e = driver.find_element( *PSWD_FLD)
e.clear()
e.send_keys('TestPassword')
sleep(2)

# Click login button
driver.find_element( *LGN_BTN ).click()

# Verify page has a text 'Invalid Login'
actual_text = driver.find_element( *ALRT_TEXT ).text
assert 'Invalid Login' in actual_text
print(f'Text is here: "{actual_text}" ')

# Driver quit
driver.quit()
