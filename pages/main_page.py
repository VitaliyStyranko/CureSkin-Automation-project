from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class MainPage(Page):


   def open_main(self):
      self.driver.get('https://shop.cureskin.com/')