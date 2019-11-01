from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BEST_SELLERS = (By.CSS_SELECTOR, "#nav-xshop > a:nth-child(2)")
EXPECTED_NAMES = (By.CSS_SELECTOR, "div#zg_banner_text_wrapper")
WEB_LINKS = (By.CSS_SELECTOR, "div#zg_tabs li")



@when('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('Click on Best Sellers')
def click_on_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@then('Clicks on each top link and verify that new page opens')
def verify_all_links(context):
    expected_names_page = ['Amazon Best Sellers', 'Amazon Hot New Releases', 'Amazon Movers & Shakers', 'Amazon Most Wished For', 'Amazon Gift Ideas']
    web_links = context.driver.find_element(*WEB_LINKS)
    for x in range(len(web_links)):
        web_links[x].click()
        assert context.driver.find_element(*EXPECTED_NAMES).text