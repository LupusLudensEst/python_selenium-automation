from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

sleep(3)

#Input into search field "Cancel order"
search = driver.find_element(By.ID, "helpsearch")
search.clear()
search.send_keys('Cancel order')
sleep(1)

#Click on "Go" button
driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()
sleep(3)

# Verify if "Cancel order" is on page
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
print('1: ', driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text, ';')
driver.quit()

