from selenium import webdriver


class VintedEditProfilePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver: webdriver = driver
