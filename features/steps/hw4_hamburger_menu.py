from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
use_step_matcher("re")

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

@when("Click on hamburger menu")
def click_on_hamburger_menu(context):
    context.driver.find_element(*HAM_MENU).click()
    sleep(2)
    #raise NotImplementedError(u'STEP: When Click on hamburger menu')


@step("Click on Amazon music menu item")
def click_on_amazon_music_menu_item(context):
    context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()
    sleep(2)
    #raise NotImplementedError(u'STEP: And Click on Amazon music menu items')


@then("6 menu items are present")
def verify_amount_of_items(context):
    sleep(4)
    print(len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)))
    assert len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)) == 6, \
        f'Expected 6 items  but got {len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))}'
    #raise NotImplementedError(u'STEP: Then 6 menu items are present')
