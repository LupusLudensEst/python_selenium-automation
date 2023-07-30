from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.implicitly_wait(5)

# Locators
CLCK_ME_BTN = (By.XPATH, "//button[@onclick='myFunctionAlert()']")

driver.find_element(*CLCK_ME_BTN).click()

# driver.switch_to_alert().accept() #closes alert window using OK button
driver.switch_to.alert.dismiss() # closes alert window using cancel button

# Driver quit
# driver.quit()
