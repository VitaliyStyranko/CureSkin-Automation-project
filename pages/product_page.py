from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class ProductPage(Page):

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".button[type='submit'], [name='add']")
    CONF_SHOWN = (By.XPATH, "//div[@class='cart-notification focus-inset animate active']"
                            "//h2[contains(text(), 'added to your cart')]")
    VIEW_MY_CART_BTN = (By.XPATH, '//*[@class="cart-notification__links"]//a[@href="/cart"]')
    PRODUCT_TITLE = (By.XPATH, '//a[@class="cart-item__name h4 break"]')

    def open_collections_page(self):
        self.driver.get('https://shop.cureskin.com/collections')

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_confirmation(self):
        self.wait_for_element_appear(*self.CONF_SHOWN)

    def click_view_btn(self):
        self.click(*self.VIEW_MY_CART_BTN)

    def verify_item(self, expected_result):
        actual_result = self.driver.find_element(*self.PRODUCT_TITLE).text
        assert expected_result == actual_result, \
            f'Error! Actual text {actual_result} does not match expected{expected_result}'


















