from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

DEALS_UNDER_25_LINK = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")
TODAYS_DEALS_HEADER = (By.CSS_SELECTOR, "div.gbh1-bold")
PRODUCT = (By.CSS_SELECTOR, "div a.a-button-text")
FIRST_PRODUCT = (By.CSS_SELECTOR, "img.oct-acs-asin-image")
ADD_TY_CART_BUTTOM = (By.CSS_SELECTOR, "input#add-to-cart-button")
SECOND_BUTTOM = (By.CSS_SELECTOR, "button#attachSiAddCoverage-announce")
CART = (By.CSS_SELECTOR, "span#nav-cart-count")



@when('Store original window')
def store_current_windows(context):
    context.original_window = context.driver.current_window_handle
    old_windows = context.driver.window_handles
    print('\noriginal_window\n', context.original_window)
    print('\nold_windows\n', old_windows)

@when('Click to open Deals under 25')
def click_to_open_deals_under_25(context):
    context.driver.find_element(*DEALS_UNDER_25_LINK).click()

@when('Switch to the newly opened window')
def swich_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    current_windows = context.driver.window_handles
    print('\ncurrent_windows\n', current_windows)

    new_window = current_windows[1]
    #swich freshly opened window
    context.driver.switch_to_window(new_window)

@then('Todays Deals are shown')
def header_is_correct(context):
    actual_header = context.driver.find_element(*TODAYS_DEALS_HEADER).text
    assert actual_header

@then('Open the product')
def open_the_product(context):
    context.driver.find_element(*PRODUCT).click()

@then('Open the first product')
def open_the_first_product(context):
    context.driver.find_element(*FIRST_PRODUCT).click()

@then('Click Add to card buttom')
def add_to_cart(context):
    context.driver.find_element(*ADD_TY_CART_BUTTOM).click()

@then('Click second buttom')
def add_to_cart2(context):
    context.driver.find_element(*SECOND_BUTTOM).click()
    sleep(2)

@then('user can close new window and switch back to original')
def close_and_swich_to_window_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)

@then('User refresh page')
def refresh_page(context):
    context.driver.refresh()

@then('Verify cart has item')
def cart_has_item(context):
    actual_item = context.driver.find_element(*CART)
    assert actual_item