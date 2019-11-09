from behave import when, given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2") #type of data tuple-can not be changed
EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
CART = (By.ID, 'nav-cart')
CART_EMPTY = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")
#SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, "span.action-inner") #(By.XPATH, "//span[@class='nav-action-inner']")

@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_page()

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

#================================================TOOLTIP===========================================================
# @then("Verify SignIn tooltip is present and clickable")
# def verify_signin_toopltip_clickable(context):
#     context.driver.wait.until(
#         EC.element_to_be_clickable(SIGN_IN_TOOLTIP)
#     )
#
# @when("Wait until SignIn tooltip disappears")
# def wait_sign_in_tooltip_disappears(context):
#     context.driver.wait.until(
#         EC.invisibility_of_element_located(SIGN_IN_TOOLTIP)
#     )
#
#
# @then("Verify SignIn tooltip is not clickable")
# def wait_sign_in_tooltip_not_clickable(context):
#     # Wait until NOT!
#     context.driver.wait.until_not(
#         EC.element_to_be_clickable(SIGN_IN_TOOLTIP)
#     )