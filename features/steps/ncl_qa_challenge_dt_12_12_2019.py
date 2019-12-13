from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
use_step_matcher("re")


@given("a Guest")


@step("I am on Homepage")
def open_ncl_main_page(context):
    context.driver.get('https://www.ncl.com/')
    sleep(4)


@step('I navigated to "Ports" page')
def get_ports_btn(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/port-of-call')]").click()
    sleep(2)


@when('I search for "Honolulu" port')
def honolulu_found(context):
    search = context.driver.find_element(By.ID, "searchbar").click()
    search.clear()
    search.send_keys('Honolulu')
    sleep(2)

def click_on_magnifying_glass(context):
    context.driver.find_element(By.XPATH, "//a[@title='Honolulu, Oahu']").click()
    sleep(4)


@then("Map zoomed to show selected port")
def map_zoomed(context):
    context.driver.find_element(By.XPATH, ).click()
    sleep(4)