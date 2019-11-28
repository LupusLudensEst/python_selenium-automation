from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#TEXT_HERE = (By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']")
#ELEVEN_ITEMS_HERE = (By.CSS_SELECTOR, "ul.white")

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://lingocard.com/')
driver.maximize_window()

# Verify if "International Educational Platform" is on page
assert 'International Educational Platform' in driver.find_element(By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']").text
print('The text: ', driver.find_element(By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']").text, '.')
sleep(3)

# Verify if there are 11 boxes in the hamburger menu
driver.find_element(By.XPATH, "//div[@class='menu-link']").click()
sleep(3)
print('There are: ', len(driver.find_elements(By.CSS_SELECTOR, "ul.white")), 'items total.')
sleep(3)
driver.quit()