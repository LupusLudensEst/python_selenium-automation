from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# locators
LOGN_BTN = (By.CSS_SELECTOR, "a.oauthloginbutton.btn.btn-social.btn-primary.da11y-submenu")
LGN_FLD = (By.CSS_SELECTOR, "input#username.validate")
PSWRD_FLD = (By.ID, "password")
LOGN_BTN_ENTRD = (By.ID, "kc-login")
ALRT_TEXT = (By.CSS_SELECTOR, "span.kc-feedback-text")

# open the url
driver.get( 'https://4tellus.com/' )

# click on login button
driver.find_element( *LOGN_BTN ).click()

# enter wrong login
e = driver.find_element( *LGN_FLD )
e.clear()
e.send_keys('WrongLogin1234!@gmail.com')
sleep(4)

# enter wrong password
e = driver.find_element( *PSWRD_FLD )
e.clear()
e.send_keys('WrongPassword1234!')
sleep(4)

# click on login button after login and password are entered
driver.find_element( *LOGN_BTN_ENTRD ).click()

# verify page has a text 'Invalid user name or password.'
actual_text = driver.find_element( *ALRT_TEXT ).text
assert 'Invalid user name or password.' in actual_text
print(f'Text is here: {actual_text} ')

# driver quit
driver.quit()