from behave import given, then
from selenium.webdriver.common.by import By
from time import sleep

EIGHT_BOXES = (By.CSS_SELECTOR, "p.a-text-bold")

@given('Open Amazonprime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')

@then('Verify there are {expected_amount} boxes')
def verify_boxes(context, expected_amount):
    sleep(3)
    print('There are: ', len(context.driver.find_elements(*EIGHT_BOXES)), 'items total.')
    actual_boxes = len(context.driver.find_elements(*EIGHT_BOXES))
    assert actual_boxes == int(expected_amount), \
        f'Expected {expected_amount} items but got {actual_boxes}'