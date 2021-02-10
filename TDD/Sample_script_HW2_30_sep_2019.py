from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

sleep(3)

#Input into search field "Cancel order"
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.clear()
search.send_keys('Cancel order')
sleep(1)

#Click on "Go" button
driver.find_element(By.ID, "nav-search-submit-button").click()
sleep(3)

# Verify if "To cancel an Amazon order, visit the Order History section in Your Account." is on page
expected_text = 'To cancel an Amazon order, visit the Order History section in Your Account./'
actual_text = driver.find_element(By.CSS_SELECTOR, "div.a-expander-content.a-expander-partial-collapse-content").text
if expected_text in actual_text:
    print(f'Ok, actual text has expected text inside')
else:
    print(f'Not Ok, expected text: {expected_text},\nbut actual text: {actual_text}')
# Driver quit
driver.quit()

