from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://yandex.ru/')
expected_word_one = 'Management'
expected_word_two = 'Ме́неджмент'
search = driver.find_element(By.ID, 'text')
search.clear()
search.send_keys(expected_word_one)

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.CLASS_NAME, 'search2__button').click()

# verify
actual_text_one = driver.find_element(By.XPATH, "(//div[contains(@class,'text-container typo typo_text_m typo_line_m')])[1]").text
actual_text_two = driver.find_element(By.XPATH, "(//div[@class='text-container typo typo_text_m typo_line_m organic__text'])[2]").text
assert expected_word_one in actual_text_one
assert expected_word_two in actual_text_two
print(f'Actual text one: {actual_text_one}')
print(f'Actual text two: {actual_text_two}!')

# driver quit
driver.quit()

