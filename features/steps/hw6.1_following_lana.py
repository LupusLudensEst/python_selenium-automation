from behave import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
use_step_matcher("re")

SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, "span.action-inner") #(By.XPATH, "//span[@class='action-inner']") #(By.XPATH, "//span[@class='nav-action-inner']")

@then("Verify SignIn tooltip is present and clickable1")
def verify_signin_toopltip_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_TOOLTIP)
    )


@when("Wait until SignIn tooltip disappears1")
def wait_sign_in_tooltip_disappears(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_TOOLTIP)
    )



@then("Verify SignIn tooltip is not clickable1")
def wait_sign_in_tooltip_not_clickable(context):
    # Wait until NOT!
    context.driver.wait.until_not(
        EC.element_to_be_clickable(SIGN_IN_TOOLTIP)
    )
    assert EC.element_to_be_clickable(SIGN_IN_TOOLTIP) == FALSE