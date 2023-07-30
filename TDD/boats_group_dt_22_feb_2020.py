from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()


# locators
CRS_BTN = (By.XPATH, "//li[@class='menu-item menu-item-type-post_type menu-item-object-page menu-item-3954']")
IFRM_LCTR = (By.ID, "gnewtonIframe")
SNR_SFTWR_DVLPR_ENG_MIA = (By.XPATH, "//a[@ns-qa='Senior Software Developer']")
SNR_SFTWR_DVLPR_ENG_MIA_TXT_HR = (By.ID, "gnewtonJobDescriptionText")

# Explicit wait
wait = WebDriverWait(driver, 15)

# open the url
driver.get( 'https://www.boatsgroup.com/' )

# click on careers button
driver.find_element( *CRS_BTN ).click()

# open iframe
# driver.switch_to.frame(driver.find_element( *IFRM_LCTR ))
wait.until(EC.frame_to_be_available_and_switch_to_it("gnewtonIframe"))

# click on QA Automation Engineer in Miami button
driver.find_element( *SNR_SFTWR_DVLPR_ENG_MIA ).click()

# verify page has a text 'Senior Software Developer - Hybrid (Miami)'
sleep(8)
expected_text = 'Senior Software Developer - Hybrid (Miami)'
actual_text = driver.find_element( *SNR_SFTWR_DVLPR_ENG_MIA_TXT_HR).text
assert expected_text in actual_text
print(f'Text is here:\n {actual_text[:len(expected_text)]}')

# # Sleep to see what we have
sleep(2)
#
# # Driver quit
# driver.quit()
