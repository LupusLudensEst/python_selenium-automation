from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
use_step_matcher("re")

@when("Search for a Brain Stimulator")
def enter_search_word(context):
    search = context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search.clear()
    search.send_keys('Brain Stimulator')
    sleep(2)

@step("Click on search")
def click_on_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[value='Go']").click()
    sleep(4)

@step("Open the first product search result")
def click_on_search_word(context):
    result = context.driver.find_element(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']").click()
    sleep(2)


@step("Click on Add to Cart button")
def click_on_add_to_cart(context):
    result = context.driver.find_element(By.XPATH, "//input[@name='submit.add-to-cart']").click()
    sleep(2)


@then("Verify cart has 0 item")
def verify_if_product_in_cart(context):
    result = context.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").text
    assert "0" in result, f"Expected text is:  {result}."