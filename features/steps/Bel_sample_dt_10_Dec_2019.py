from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
# driver = webdriver.Chrome()
# driver.maximize_window()

# open the url
@given('Open discountmugs page')
def open_the_url(context):
    context.driver.get('https://www.discountmugs.com/')
    sleep(2)

# enter the e-mail into the field
@then('Enter the e-mail into the field')
def enter_the_email(context):
    search = context.driver.find_element(By.ID, 'userEmail')
    search.clear()
    search.send_keys('gurovvic@gmail.com')
# wait for 4 sec
sleep(4)

# click on the sign up btn
@then('Click on the sign up btn')
def click_on_sign_btn(context):
    context.driver.find_element(By.XPATH, "//input[@name='']").click()

# assert that given text is on the page
@then('Assert that given text is on the page')
def assert_text_is_here(context):
    assert 'Empowering you to share your message and create a lasting impression since 1995' in driver.find_element(By.XPATH, "//div[@class='home-line-text']").text
    print('Text:', driver.find_element(By.XPATH, "//div[@class='home-line-text']").text, '.')

# driver.quit()