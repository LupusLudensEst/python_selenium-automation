from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://yandex.ru/')


search = driver.find_element(By.ID, 'text')
search.clear()
search.send_keys('Management')


# wait for 4 sec
sleep(4)


# click search
driver.find_element(By.CLASS_NAME, 'search2__button').click()


# verify
assert 'Management' in driver.find_element(By.XPATH, "//div[contains(@class,'text-container typo typo_text_m typo_line_m')]").text
assert 'Management' in driver.find_element(By.XPATH, "//div[@class='text-container typo typo_text_m typo_line_m organic__text']").text
print('1: ', driver.find_element(By.XPATH, "//div[contains(@class,'text-container typo typo_text_m typo_line_m')]").text, ';')
print('2: ', driver.find_element(By.XPATH, "//div[@class='text-container typo typo_text_m typo_line_m organic__text']").text, '!')


driver.quit()

