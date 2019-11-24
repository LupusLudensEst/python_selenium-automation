from behave import when, given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRODUCTS = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li") #12 or 15 goods below the agreed line, all products as search field
PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name') #All strings on the page consisting description of the goods

@given("Open Amazon {product_id} page as Lana did")
def open_wholefoods_deals(context, product_id):
    context.driver.get((f'https://www.amazon.com/{product_id}/'))

@then("Verify every product on the page has a text {expected_word} and a product name as Lana did")
def verify_regular_price(context, expected_word):
    product_elements = context.driver.find_elements(*PRODUCTS)

    for product_element in product_elements:
        assert expected_word in product_element.text, f"Expected, '{expected_word}', to be in: {product_element.text}"
        print('Product element: ',  product_element.text, '===')

        product_description = product_element.find_element(*PRODUCT_DESCRIPTION).text
        print('\n', product_description, ';')
        assert '' != product_description, f'Expected non-empty product name'
