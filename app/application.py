from pages.hw7_main_page import MainPage
from pages.hw8_product_page import Product
from pages.hw7_search_results_page import SearchResultsPage
from pages.hw8_side_menu import SideMenu

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.product_page = Product(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.side_menu =SideMenu(self.driver)
