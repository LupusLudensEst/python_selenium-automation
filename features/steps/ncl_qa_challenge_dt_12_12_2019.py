from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
use_step_matcher("re")

GET_PORTS_BTN = (By.XPATH, "//a[contains(@href, '/shore-excursions')]")
NAV_EXCURSIONS = (By.CSS_SELECTOR, "button.btn-cta.btn-primary.btn-large.search-submit")
SHORE_EXC_IS_PRESENT = (By.CSS_SELECTOR, "h2.header-title.visible-desktops")

@given("a Guest")


@step("I am on Homepage")
def open_ncl_main_page(context):
    context.driver.get('https://www.ncl.com/')
    sleep(4)


@step('I navigated to "Shore Excursion" page')
def get_ports_btn(context):
    context.driver.find_element(*GET_PORTS_BTN).click()
    sleep(2)


@step("I click Find Excursions")
def nav_excursions(context):
    context.driver.find_element(*NAV_EXCURSIONS).click()
    sleep(2)


@step("Shore Excursions page is present")
def shore_exc_is_present(context):
    TEXT_IS_HERE = context.driver.find_element(*SHORE_EXC_IS_PRESENT).text
    assert 'Shore Excursions' in TEXT_IS_HERE
    print('Text:', TEXT_IS_HERE, '.')
    sleep(2)