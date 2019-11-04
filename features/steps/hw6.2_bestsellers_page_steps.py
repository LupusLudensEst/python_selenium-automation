from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BEST_SELLERS_PAGE = (By.XPATH, "//a[contains(@href, 'bestsellers')]") #(By.XPATH, "//a[@class='nav-a  ']")
TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')

@when('Open Best Sellers page')
def click_on_best_sellers_page(context):
    context.driver.find_element(*BEST_SELLERS_PAGE).click()

@then('User can click through top links and verify correct page opens')
def click_thru_top(context):

    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):

        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link_to_click.text

        link_to_click.click()
        sleep(10)

        new_text = context.driver.find_element(*HEADER).text
        assert link_text in new_text, f'Expected {link_text} to be in {new_text}'
































# SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, "span.action-inner") #(By.XPATH, "//span[@class='action-inner']") #(By.XPATH, "//span[@class='nav-action-inner']")
#
# @then("Verify SignIn tooltip is present and clickable1")
# def verify_signin_toopltip_clickable(context):
#     context.driver.wait.until(
#         EC.element_to_be_clickable(SIGN_IN_TOOLTIP) #Stumble is here. The issue with the time.
#     )
#
#
# @when("Wait until SignIn tooltip disappears1")
# def wait_sign_in_tooltip_disappears(context):
#     context.driver.wait.until(
#         EC.invisibility_of_element_located(SIGN_IN_TOOLTIP)
#     )
#
#
#
# @then("Verify SignIn tooltip is not clickable1")
# def wait_sign_in_tooltip_not_clickable(context):
#     # Wait until NOT!
#     context.driver.wait.until_not(
#         EC.element_to_be_clickable(SIGN_IN_TOOLTIP)
#     )
#     assert EC.element_to_be_clickable(SIGN_IN_TOOLTIP) == FALSE