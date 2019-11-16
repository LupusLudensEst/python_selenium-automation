from pages.hw7_base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SideMenu(Page):
    AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def click_amazon_music(self):
        self.wait_for_element_click(*self.AMAZON_MUSIC_MENU_ITEM)
        sleep(1)

    def verify_amount_of_items(self, expected_item_count: int):

        """
        :param expected_item_count: Expected amount of menu items
        """
        actual_item_count = str(len(self.driver.find_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS)))

        assert expected_item_count == actual_item_count, f'Expected {expected_item_count}, but got {actual_item_count}'