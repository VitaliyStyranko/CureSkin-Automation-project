from pages.base_page import Page
from selenium.webdriver.common.by import By

class CollectionsPage(Page):

    PRODUCT_COLLECTION = (By.XPATH, "//a[@href='/collections/body']"
                                    "//h2[contains(text(),'Body')]")

    def open_collections_page(self):
        self.driver.get('https://shop.cureskin.com/collections')

    def click_product_clt_link(self):
        self.click(*self.PRODUCT_COLLECTION)


