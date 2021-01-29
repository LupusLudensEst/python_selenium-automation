from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.discountmugs.com/')
sleep(2)

# enter the e-mail into the field
search = driver.find_element(By.ID, 'userEmail')
search.clear()
search.send_keys('gurovvic@gmail.com')
# wait for 4 sec
sleep(4)

# click on the sign up btn
driver.find_element(By.XPATH, "//input[@name='']").click()
# wait for 4 sec
sleep(4)

assert 'Empowering you to share your message and create a lasting impression since 1995' in driver.find_element(By.XPATH, "//div[@class='home-line-text']").text
print('Text:', driver.find_element(By.XPATH, "//div[@class='home-line-text']").text, '.')

driver.quit()