from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "C:\Webdrivers\chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# Locators
CLCK_ME_BTN = (By.XPATH, "//button[@onclick='myFunction()']")

driver.find_element(*CLCK_ME_BTN).click()

# driver.switch_to_alert().accept() #closes alert window using OK button
driver.switch_to_alert().dismiss() # closes alert window using cancel button

# Driver quit
driver.quit()
