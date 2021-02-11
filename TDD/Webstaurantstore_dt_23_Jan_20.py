from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# Locators
SEARCH_STRING = (By.ID, "searchval")
SEARCH_BTN = (By.XPATH, "//button[@value='Search']")
ALL_ITEMS_1 = (By.CSS_SELECTOR, "a.description")
ALL_ITEMS_2 = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
ITEM_ADDED = (By.CSS_SELECTOR, "a.btn-small.btn-primary")
CART_BTN = (By.CSS_SELECTOR,  "input.btn.btn-cart.btn-small")
CART_BUTTON_SPAN = (By.CSS_SELECTOR, "cartItemCountSpan")
EMPTHY_CART_BTN_1 = (By.CSS_SELECTOR, "a.emptyCartButton.btn.btn-mini.btn-ui.pull-right")
EMPTHY_CART_BTN_2 = (By.XPATH, "//button[@class='btn btn-primary']")
CART_EMTHY_TEXT = (By.XPATH, "//div[@class='empty-cart__text']")

# Open the url
driver.get( 'https://www.webstaurantstore.com/' )
wait = WebDriverWait(driver, 15)

# Input search string
search = driver.find_element( *SEARCH_STRING)
search.clear()
search.send_keys( 'stainless work table' )

# Click search
driver.find_element( *SEARCH_BTN ).click()

# Verify all items with Table in the title are here
print( 'There are 1: ', len( driver.find_elements( *ALL_ITEMS_1 ) ), 'items' )
print( 'There are 2: ', len( driver.find_elements( *ALL_ITEMS_2 ) ), 'items' )

# Add the last of found items to cart and empty the cart
driver.find_elements( *ALL_ITEMS_2 )[-1].click()
driver.find_element( *ITEM_ADDED ).click()

target = wait.until(EC.element_to_be_clickable(EMPTHY_CART_BTN_1))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click(on_element = target)
actions.perform()

target = wait.until(EC.element_to_be_clickable(EMPTHY_CART_BTN_2))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click(on_element = target)
actions.perform()

# Verify text "Your cart is empty." is here
searhed_word = ('Your cart is empty.').lower()
actual_text = wait.until(EC.visibility_of_element_located(CART_EMTHY_TEXT)).text.lower()
print(f'Actual text: "{actual_text}" VS Expected text: "{searhed_word}" ')
assert searhed_word in actual_text
if searhed_word in actual_text:
    print(f'Text is here: "{searhed_word}"')
else:
    print(f'Actual text is here: "{actual_text}" ')

# Sleep to see what we have
sleep(2)


driver.quit()