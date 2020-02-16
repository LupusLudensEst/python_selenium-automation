from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame") # 1 frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("packageFrame") # 2 frame
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("classFrame") # 3 frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()

# driver quit
driver.quit()
