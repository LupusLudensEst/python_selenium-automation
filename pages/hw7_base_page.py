class Page:

#Opens Amazon main page
    def __init__(self, driver):
        self.driver = driver
        self.base_url ='https://www.amazon.com/'

#Clicks on soem element
    def click(self, *locator):
        self.driver.find_element(*locator).click()

#Clears field, inputs some text
    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

#Opens additional page on Amazon
    def open_page(self, url = ''):
        self.driver.get(self.base_url + url)

#Verifies expected text is here and the text is exactly as expected
    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text: {expected_text}, but get: {actual_text} !!!'