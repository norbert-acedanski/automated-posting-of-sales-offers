from selenium import webdriver
from selenium.webdriver.common.by import By


class VintedGenericModal:
    modal_xpath = "//div[contains(@class, 'ReactModal__Content--after-open')]"
    x_button_xpath = "//span[@data-icon-name='x']//ancestor::button"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_x_button(self) -> None:
        self.driver.find_element(by=By.XPATH, value=self.modal_xpath + self.x_button_xpath).click()