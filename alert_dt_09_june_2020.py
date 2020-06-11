from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CLCK_ME_BTN = (By.XPATH, "//button[@onclick='myFunction()']")

driver = webdriver.Chrome(executable_path = "C:\Webdrivers\chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
time.sleep(4)

# driver.switch_to_alert().accept() #closes alert window using OK button
driver.switch_to_alert().dismiss() # closes alert window using cancel button
time.sleep(4)

driver.quit()
