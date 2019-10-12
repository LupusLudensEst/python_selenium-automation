from behave import given, when, then
from selenium.webdriver.common.by import By

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2") #type of data tuple-can not be changed
#EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Amazon Orders Link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()  #*-tells that there are two elements

"""
@then("Verify Sign In page is opened")
def verify_signin_opened(context):
    context.driver.find_element(*EMAIL_FIELD) #*-tells that there are two elements
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
"""