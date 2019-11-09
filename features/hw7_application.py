from pages.hw7_main_page import MainPage
from pages.hw7_search_results_page import SearchResultsPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)