from behave import when, given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2") #type of data tuple-can not be changed
EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
CART = (By.ID, 'nav-cart')
CART_EMPTY = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')

@when('Click Amazon Orders Link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()  #*-tells that there are two elements

@when('Click on cart icon')
def click_cart_icon(context):
    cart_icon = context.driver.find_element(*CART)
    print(cart_icon)
    context.driver.refresh()
    cart_icon = context.driver.find_element(*CART)
    print(cart_icon)
    cart_icon.click()

@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_cart_empty(context):
    context.driver.find_element(*CART_EMPTY )
    assert 'Your Shopping Cart is empty.' in context.driver.find_element(*CART_EMPTY).text


@then("Verify Sign In page is open")
def verify_signin_opened(context):
    context.driver.find_element(*EMAIL_FIELD) #*-tells that there are two elements
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
