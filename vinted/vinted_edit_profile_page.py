from selenium import webdriver

from vinted.vinted_frame import VintedFrame


class VintedEditProfilePage(VintedFrame):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver=driver)
