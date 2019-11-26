from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

@when("Click on the Cart icon First")
def click_on_shopping_cart_1(context):
    context.driver.find_element(By.ID, 'nav-cart').click()
    sleep(2)

@step("Click on the Sign in icon Enter")
def click_on_sign_in_enter(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.action-inner").click() #(By.XPATH, "//span[@class='action-inner']").click()
    sleep(2)

@step("Enter email into Email field")
def enter_email(context):
    search = context.driver.find_element(By.ID, 'ap_email')
    search.clear()
    search.send_keys('sanoy2006@rambler.ru')
    sleep(2)

@step("Click on the Continue icon")
def click_on_continue_icon(context):
    context.driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()
    sleep(2)

@then("Enter password into Password field")
def enter_password(context):
    search = context.driver.find_element(By.ID, 'ap_password') #(By.XPATH, "//input[@type='password']")
    search.clear()
    search.send_keys('MyUSA2016')
    sleep(3)

@step("Click on the Sign in icon Continue")
def click_on_sign_in_continue(context):
    context.driver.find_element(By.ID, 'signInSubmit').click() #(By.XPATH, "//input[@id='signInSubmit']").click()
    sleep(3)

@then('Enter "Brain Stimulator" into search field')
def enter_search_word(context):
    search = context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search.clear()
    search.send_keys('Brain Stimulator')
    sleep(2)

@step("Click on search button")
def click_on_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[value='Go']").click()
    sleep(3)

@step("Click on first good int he list")
def click_on_search_word(context):
    result = context.driver.find_element(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']").click()
    sleep(2)

@then("Click on Add to Cart button")
def click_on_add_to_cart(context):
    result = context.driver.find_element(By.XPATH, "//input[@name='submit.add-to-cart']").click()
    sleep(3)

@then("Click on No Thanks button")
def click_on_no_thanks_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "button#siNoCoverage-announce.a-button-text").click() #(By.XPATH, "//button[@id='siNoCoverage-announce']").click() #(By.ID, 'siNoCoverage-announce').click()
    sleep(2)

@then("Click on the Cart icon Second")
def click_on_shopping_cart_2(context):
    context.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").click()
    sleep(2)

@then('Verify that text "Muse: The Brain Sensing Headband, Black" is on the page')
def verify_if_product_in_cart(context):
    result = context.driver.find_element(By.XPATH, "//span[@class='a-size-medium sc-product-title a-text-bold']").text
    assert "tDCS Device - TheBrainDriver v2. tDCS Digital Precision + Safety Features. (Everything Included. Ready-to-Use)" in result, f"Expected text is:  {result}."