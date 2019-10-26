from behave import when, given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#---name
# PRODUCT_NAME = (By.CSS_SELECTOR, 'span.a-text-strike')
# PRODUCT_NAME = (By.CSS_SELECTOR, "span.a-size-medium.wfm-sales-item-card__product-name.a-text-bold")
# PRODUCT_NAME = (By.XPATH, "//span[@class='a-size-medium wfm-sales-item-card__product-name a-text-bold']")
#---Regular
SELECTED_WORD = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li")

@given("Open Amazon {productid} page")
def open_amazon_wholefoods_page(context, productid):
    context.driver.get(f'https://www.amazon.com/{productid}/')

@then('Verify every product on the page has a text Regular and a product name')
def verify_product_has_word(context):
    expected_word = 'Regular'
#---name
# def verify_product_has_name(context):
#     expected_product_element = context.driver.find_elements(*PRODUCT_NAME)
# ---Regular
    word_webelements = context.driver.find_elements(*SELECTED_WORD)
    print('The actual word is: ', (context.driver.find_element(*SELECTED_WORD).text), '.')
# ---name
#     product_name_webelements = context.driver.find_elements(*PRODUCT_NAME).text
#     print('The actual product element is: ', (context.driver.find_element(*PRODUCT_NAME).text), '.')
# ---Regular
    for x in range(len(word_webelements)):
        actual_word = context.driver.find_element(*SELECTED_WORD).text
        assert expected_word in actual_word, f'Expected, "{expected_word}", but got, "{actual_word}"'
# ---name
#     for element in product_name_webelements:
#         element.find_element(*PRODUCT_NAME)
#         assert expected_product_element in actual_product_element, f'Expected, "{expected_product_element}", but got, "{actual_product_element}"'
