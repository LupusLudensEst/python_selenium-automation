from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#SEARCH_BAR = (By.NAME, 'q')
BTN_SEARCH = (By.NAME, 'btnK')

# init driver
driver = webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver")
driver.maximize_window()

driver.implicitly_wait(4)

# open the url
driver.get('https://www.google.com/')
driver.wait = WebDriverWait(driver, 10)

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# click search
driver.wait.until(EC.element_to_be_clickable(BTN_SEARCH)).click()

# verify
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text
print('1: ', driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text, ';')
print('2: ', driver.find_element(By.XPATH, "//div[@class='g']").text, '!')

driver.quit()
