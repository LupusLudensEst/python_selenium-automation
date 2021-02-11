#import allure
from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2") #type of data tuple-can not be changed
EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
CART = (By.ID, "nav-cart")
CART_EMPTY = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")
# AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
# AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")
SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, '#nav-signin-tooltip span')
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')
#SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, "span.action-inner") #(By.XPATH, "//span[@class='nav-action-inner']") #(By.CSS_SELECTOR, '#nav-signin-tooltip span')
#HAM_MENU = (By.ID, 'nav-hamburger-menu')

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

@when("Click on hamburger menu")
def click_on_hamburger_menu(context):
   # context.driver.find_element(*HAM_MENU).click()
    context.app.main_page.click_menu()
    sleep(2)

@then("Click on Amazon music menu item")
def click_on_amazon_music_menu_item(context):
    # sleep(2)
    # context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()
    context.app.side_menu.click_amazon_music()


@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    # expected_item_count = int(expected_item_count)
    # sleep(4)
    # actual_item_count = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)
    # assert actual_item_count == int(expected_item_count) \
    #     f'Expected 6 items  but got {len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))}'
    context.app.side_menu.verify_amount_of_items(expected_item_count)


#see hw5.3_regular_product_names.py str#14
@given('Open Amazon {product_id} page')
def open_product(context, product_id):
    context.app.product_page.open_product(product_id)

@when('Hover over Add To Cart button')
def hover_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()

@then('Veryfy size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_size_tooltip()
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