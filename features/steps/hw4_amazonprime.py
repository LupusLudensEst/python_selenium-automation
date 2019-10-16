from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
use_step_matcher("re")

AMAZONPRIME_BOXES_RESULTS = (By.XPATH, "//div[@class='a-section img-wrapper']")

@given("Open Amazonprime page")
def open_amazon_prime_page(context):
    context.driver.get('https://www.amazon.com/amazonprime')
    sleep(4)


@then("Verify there are 8 boxes")
def verify_there_eight_boxes(context):
    sleep(4)
    print(len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS)))
    assert len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS)) == 8, \
        f'Expected 8 items  but got {len(context.driver.find_elements(*AMAZONPRIME_BOXES_RESULTS))}'