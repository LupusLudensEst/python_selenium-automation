from behave import when, given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRODUCTS = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li") #All products as search field
PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name') #All strings on the page consisting expected word

@given("Open Amazon {productid} page as Lana did")
def open_wholefoods_deals(context, productid):
    context.driver.get((f'https://www.amazon.com/{productid}/'))

@then("Verify every product on the page has a text {expected_word} and a product name as Lana did")
def verify_regular_price(context, expected_word):
    product_elements = context.driver.find_elements(*PRODUCTS)

    for product_element in product_elements:
        assert expected_word in product_element.text, f"Expected, '{expected_word}', to be in: {product_element.text}"

        product_name = product_element.find_element(*PRODUCT_NAME).text
        print('\n', product_name, ';')
        assert '' != product_name, f'Expected non-empty product name'
