from behave import when, given, then
from selenium.webdriver.common.by import By
from time import sleep

# PRODUCT_NAME = ("//span[@class='a-size-medium wfm-sales-item-card__product-name a-text-bold']")
SELECTED_WORD = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li")


@given("Open Amazon {productid} page")
def open_amazon_wholefoods_page(context, productid):
    context.driver.get(f'https://www.amazon.com/{productid}/')


@then('Verify every product on the page has a text Regular and a product name')
def verify_product_has_word_and_name(context):
    expected_word = 'Regular'

    word_webelements = context.driver.find_elements(*SELECTED_WORD)
    print('The actual word is: ', context.driver.find_element(*SELECTED_WORD).text, '.')

    for x in range(len(word_webelements)):
        actual_word = context.driver.find_element(*SELECTED_WORD).text
        assert expected_word in actual_word, f'Expected, "{expected_word}", but got, "{actual_word}"'
