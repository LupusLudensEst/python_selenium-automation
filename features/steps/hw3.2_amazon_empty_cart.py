from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


@when('Click on the shopping cart icon')
def click_on_shopping_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify that the shopping cart is empty')
def verify_cart_is_empty(context):
    result = context.driver.find_element(By.XPATH, "//h1[@class = 'sc-empty-cart-header']").text
    assert "empty" in result, f"Expected text is empty, but got:  {result}."

