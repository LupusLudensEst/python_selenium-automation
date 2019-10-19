from behave import given, then
from selenium.webdriver.common.by import By
from time import sleep

"""
#AMAZONPRIME_BOXES_RESULTS = (By.XPATH, "//div[@class='a-section img-wrapper']")
AMAZONPRIME_BOXES_RESULTS = (By.CSS_SELECTOR, "p.a-text-bold")
EXPECTED_AMOUNT_BOXES = int(input("Enter expected amount of boxes: "))

@given("Open Amazonprime page")
def open_amazon_prime_page(context):
    context.driver.get('https://www.amazon.com/amazonprime')
    sleep(2)

@then("Verify there are EXPECTED AMOUNT of BOXES")
def verify_boxes_amount(context):
    sleep(2)
    print(len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS)))
    assert len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS)) == int(EXPECTED_AMOUNT_BOXES), \
    f'Expected {EXPECTED_AMOUNT_BOXES} items  but got: {len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS))}'
"""

EIGHT_BOXES = (By.CSS_SELECTOR, "p.a-text-bold")

@given('Open Amazonprime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')

@then('Verify there are {expected_amount} boxes')
def verify_boxes(context, expected_amount):
    sleep(3)
    actual_boxes = len(context.driver.find_elements(*EIGHT_BOXES))
    assert actual_boxes == int(expected_amount), \
        f'Expected {expected_amount} items but got {actual_boxes}'