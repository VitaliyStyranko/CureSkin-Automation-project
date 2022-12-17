from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.collections_page import CollectionsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.collections_page = CollectionsPage(self.driver)

