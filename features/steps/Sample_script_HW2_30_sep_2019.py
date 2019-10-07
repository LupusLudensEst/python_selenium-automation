from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
#driver.get('https://amazon.com/')
sleep(3)
"""
#Click on "Help" button
driver.find_element(By.XPATH, "//li[@class='nav_last']/a[@class='nav_a']").click()
driver.find_element(By.LINK_TEXT, 'Help').click() #!
driver.find_element(By.XPATH, "//li[@class='nav_last']/a[@class='nav_a']").click()

sleep(3)
"""
#Input into search field "Cancel order"
search = driver.find_element(By.ID, "helpsearch")
"""
search = driver.find_element(By.ID, "helpsearch" #!
search = driver.find_element(By.XPATH, "//input[@id='helpsearch']") #!
search = driver.find_element(By.XPATH, "//input[@autocomplete='off']")
search = driver.find_element(By.XPATH, "//input[@placeholder='']")
search = driver.find_element(By.XPATH, "//input[@class='a-input-text a-span12']")
"""
search.clear()
search.send_keys('Cancel order')
sleep(1)

#Click on "Go" button
driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()
"""
driver.find_element(By.XPATH, "//input[@type='submit']").click()
#driver.find_element(By.XPATH, "//span[@class='a-button-inner']/input[@type='submit']").click()
#driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()
#driver.find_element(By.XPATH, "//span[@id='helpSearchSubmit-announce']").click()
#driver.find_element(By.XPATH, "//span[@class='a-button-text']").click()
"""
sleep(3)

# Verify if "Cancel order" is on page
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

driver.quit()
""" """
