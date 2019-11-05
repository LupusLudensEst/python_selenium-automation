from behave import *
from selenium.webdriver.common.by import By

TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")


@when("Search for dress")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Search for dress')


@then("Search results for {product} is shown")
def verify_results(context, product):
    result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    assert result_text == product, f"Expected text is {product}, but got {result_text}"
