from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
use_step_matcher("re")

#AMAZONPRIME_BOXES_RESULTS = (By.XPATH, "//div[@class='a-section img-wrapper']")
AMAZONPRIME_BOXES_RESULTS = (By.CSS_SELECTOR, "p.a-text-bold")
EXPECTED_AMOUNT_BOXES = int(input("Enter expected amount of boxes: "))

@given("Open Amazonprime page")
def open_amazon_prime_page(context):
    context.driver.get('https://www.amazon.com/amazonprime')
    sleep(2)

"""
@then("Verify there are \{EXPECTED_AMOUNT_BOXES} boxes")
def verify_there_eight_boxes(context):
    sleep(2)
    print(len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS)))
    assert len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS)) == 8, \
        f'Expected 8 items  but got {len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS))}'
"""

@then("Verify there are EXPECTED AMOUNT of BOXES")
def verify_boxes_amount(context):
    sleep(2)
    print(len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS)))
    assert len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS)) == int(EXPECTED_AMOUNT_BOXES), \
    f'Expected {EXPECTED_AMOUNT_BOXES} items  but got: {len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS))}'