from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
# SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
# CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')
# HAM_MENU = (By.ID, 'nav-hamburger-menu')
# AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
# AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")
# SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, '#nav-signin-tooltip span')

# @when("Click on hamburger menu")
# def click_on_hamburger_menu(context):
#    # context.driver.find_element(*HAM_MENU).click()
#     context.app.main_page.click_menu()
#     sleep(2)


# @then("Click on Amazon music menu item")
# def click_on_amazon_music_menu_item(context):
#     # context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()
#     context.app.side_menu.click_amazon_music()
#     sleep(2)


# @then('{expected_item_count} menu items are present')
# def verify_amount_of_items(context):
#     # sleep(4)
#     # actual_item_count = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)
#     # assert actual_item_count == int(expected_item_count) \
#     #     f'Expected 6 items  but got {len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))}'
#     context.app.side_menu.verify_amount_of_items(expected_item_count)

