from behave import *
from selenium.webdriver.common.by import By

# SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
# TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")


@when("Search for {product}")
def search_product(context, product):
    # search_field = context.driver.find_element(*SEARCH_INPUT)
    # search_field.clear()
    # search_field.send_keys(product)
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.main_page.search_for_keyword(product)


@then("Search results for {product} is shown")
def verify_results(context, product):
    # result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    # assert result_text == product, f"Expected text is {product}, but got {result_text}"
    # print('Result text is: ', result_text, '.')
    context.app.search_results_page.verify_results_shown(product)
