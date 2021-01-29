from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/')

# Locators
SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
TEXT_HERE = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")

search = driver.find_element(*SEARCH_FIELD)
search.send_keys('dress', Keys.ENTER)

expected_text = 'dress'
actual_text = driver.find_element(*TEXT_HERE).text
assert expected_text in actual_text, f'Error. Expected text: {expected_text}, but actual text is: {actual_text}'

# Driver quit
driver.quit()





