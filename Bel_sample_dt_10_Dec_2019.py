from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.discountmugs.com/')
sleep(4)

assert 'Empowering you to share your message and create a lasting impression since 1995' in driver.find_element(By.XPATH, "//div[@class='home-line-text']").text
print(driver.find_element(By.XPATH, "//div[@class='home-line-text']").text)

driver.quit()