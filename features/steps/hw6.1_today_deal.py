from behave import given, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

SEE_ALL_DEALS = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]") #(By.CSS_SELECTOR, "span.as-title-block-right")
TODAY_DEALS = (By.XPATH, "//a[@href='/gp/goldbox?ref_=nav_cs_gb_azl']") #(By.CSS_SELECTOR, "div.gbh1-bold") #(By.CSS_SELECTOR, 'h1 div.gbh1-bold') #(By.CSS_SELECTOR, "div.gbh1-bold") #(By.CSS_SELECTOR, 'h1 div.gbh1-bold')
PRODUCT = (By.ID, "101_dealView_4") #(By.XPATH, "//a[@id='101 4e309eb6-announce']")
PRODUCT_REAL = (By.XPATH, "//img[contains(@src, 'https://images-na.ssl-images-amazon.com/images/I/718WQGSmINL._AC_SR300,300_.jpg')]") #(By.XPATH, "//a[contains(@href, 'Foldable-Drying-Rack-White')]") #(By.XPATH, "//a[@title='AmazonBasics Foldable Clothes Drying Laundry Rack - White']") #(By.XPATH, "//img[@src='https://images-na.ssl-images-amazon.com/images/I/718WQGSmINL._AC_SR300,300_.jpg']")
ADD_TO_CART = (By.ID, "add-to-cart-button") #(By.XPATH, "//input[@name='submit.add-to-cart']") #(By.NAME, "submit.add-to-cart") #(By.XPATH, "//div[@class='a-button-stack']") #(By.XPATH, "//span[@id='submit.add-to-cart']") #(By.ID, "submit.add-to-cart") #(By.XPATH, "//input[@id='add-to-cart-button']") #(By.XPATH, "//input[@name='submit.add-to-cart']")
ITEMS = (By.ID, "nav-cart-count")
ONE_ITEM = (By.ID, "sc-subtotal-label-activecart")
CLICK_ON_CART = (By.ID, "nav-cart")

# DEALS_UNDER_25_LINK = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")
# TODAYS_DEALS_HEADER = (By.CSS_SELECTOR, "div.gbh1-bold")
# PRODUCT = (By.CSS_SELECTOR, "div a.a-button-text")
# FIRST_PRODUCT = (By.CSS_SELECTOR, "img.oct-acs-asin-image")
# ADD_TY_CART_BUTTOM = (By.CSS_SELECTOR, "input#add-to-cart-button")
# SECOND_BUTTOM = (By.CSS_SELECTOR, "button#attachSiAddCoverage-announce")
# CART = (By.CSS_SELECTOR, "span#nav-cart-count")


#1
@given('Amazon today deal page')
def open_amazon_deal_page(context):
    context.driver.get('https://www.amazon.com/')

#2
@when('Store original windows')
def store_original_window(context):
    original_window = context.driver.current_window_handle
    old_windows = context.driver.window_handles
    print('\n Original_window: \n ', original_window)
    print('\n Old_window: \n', old_windows)

#3
@when('Click on Open Deals')
def click_open_deals(context):
    context.driver.find_element(*SEE_ALL_DEALS).click()

#4
@when('Switch to the new openly window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    current_windows = context.driver.window_handles
    print('\n New_windows: \n', current_windows)

    new_window = current_windows[1]
    context.driver.switch_to_window(new_window)

#5
@when('{expected_header} are shown')
def today_deals_shown(context, expected_header):
    #word = "Today's Deals"
    actual_header = context.driver.find_element(*TODAY_DEALS).text
    print('\n Actual word: \n', actual_header, '\n Expected word: \n', expected_header)
    assert actual_header == expected_header, f'Expected {expected_header}, but got: {actual_header}'

#6
@when('Click on product name')
def click_on_product(context):
    context.driver.find_element(*PRODUCT).click()
    print(context.driver.find_element(*PRODUCT).text)
    sleep(4)

#6.1 #The stumble is here. Can not find proper locator. Or click executing on another page.
    context.driver.find_element(*PRODUCT_REAL).click()
    sleep(4)

#7

@when('Add product to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()

#8
@when('User can close new window and switch back to original')
def close_window_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)

#9
@when('Refresh page')
def refreshing(context):
    driver.refresh()

#10
@when('Click on cart')
def click_on_cart(context):
    context.driver.find_element(*CLICK_ON_CART)

#11
@when('Cart has one item in it')
def cart_has_item(context):
    context.driver.find_element(*ITEMS).click()

#12
@when('Verify there is one item')
def cart_has_one_item(context):
    one = 'Subtotal (1 item)'
    item = context.driver.find_element(*ONE_ITEM).text

