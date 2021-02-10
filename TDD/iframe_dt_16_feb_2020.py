from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# locators
ALERT_ACCEPT = (By.XPATH, "//button[@class='sc-pNWxx sc-jrsJCI dryRrI emsrNO']")

driver.get("https://yandex.ru")
driver.wait = WebDriverWait(driver, 10)

driver.wait.until(EC.element_to_be_clickable(ALERT_ACCEPT)).click()
seq = driver.find_elements_by_tag_name('iframe')
print(f'There are: {len(seq)} iframes')
iframe = driver.find_elements_by_tag_name('iframe')[len(seq)-1]
driver.switch_to.frame(iframe)
driver.switch_to.default_content()

# driver quit
sleep(4)
driver.quit()
