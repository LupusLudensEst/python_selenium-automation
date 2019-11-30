import allure
from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

#TEXT_HERE = (By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']")
#ELEVEN_ITEMS_HERE = (By.CSS_SELECTOR, "ul.white")

# # init driver
# driver = webdriver.Chrome()
#
# # open the url
# driver.get('https://lingocard.com/')
# driver.maximize_window()

@given('Open Lingocard page')
def open_lingocard(context):
    context.driver.get('https://lingocard.com/')
    sleep(3)

# Verify if "International Educational Platform" is on page
# assert 'International Educational Platform' in driver.find_element(By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']").text
# print('The text: ', driver.find_element(By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']").text, '.')
# sleep(3)

@then('Verify if "International Educational Platform" is on page')
def verify_text_here(context):
    assert 'International Educational Platform' in context.driver.find_element(By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']").text
    print('The text: ', context.driver.find_element(By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']").text, '.')
    sleep(3)

# # Verify if there are 11 boxes in the hamburger menu
# driver.find_element(By.XPATH, "//div[@class='menu-link']").click()
# sleep(3)
# print('There are: ', len(driver.find_elements(By.CSS_SELECTOR, "ul.white")), 'items total.')
# sleep(3)

@then('Verify if there are 11 boxes in the hamburger menu')
def verify_items_here(context):
    context.driver.find_element(By.XPATH, "//div[@class='menu-link']").click()
    sleep(1)
    menu_items = context.driver.find_elements(By.CSS_SELECTOR, "#menu ul a")
    assert 11 == len(menu_items), f'Expected 11, but got {len(menu_items)} items total.'
    print('There are: ', len(context.driver.find_elements(By.CSS_SELECTOR, "#menu ul a")), 'items total.')
# driver.quit()