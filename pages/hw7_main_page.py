from selenium.webdriver.common.by import By
from pages.hw7_base_page import Page

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    HAM_MENU = (By.ID, 'nav-hamburger-menu')

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_menu(self):
        self.click(*self.HAM_MENU)


