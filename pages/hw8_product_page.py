from pages.hw7_base_page import Page
from selenium.webdriver.common.by import By
#from time import sleep

class Product(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SIZE_SELECTION_TOOLTIP = (By.ID, 'a-popover-content-1') #(By.XPATH, "//div[@class='a-popover-content']") #(By.XPATH, "//div[@id='a-popover-content-1']")

    def open_product(self, product_id):
        #https://www.amazon.com/dp/B074TBCSC8
        self.open_page(f'dp/{product_id}')

    def hover_add_to_cart(self):
        cart_button = self.find_element(*self.ADD_TO_CART_BTN)
        self.actions\
            .move_to_element(cart_button)\
            .perform()
        #sleep(7.5)

    def verify_size_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_SELECTION_TOOLTIP)