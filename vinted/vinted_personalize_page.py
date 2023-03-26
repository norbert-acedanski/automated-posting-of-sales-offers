from selenium import webdriver

from vinted.vinted_frame import VintedFrame


class VintedPersonalizePage(VintedFrame):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver=driver, wait_for_essentials=False)
        self.wait_for_essentials()
