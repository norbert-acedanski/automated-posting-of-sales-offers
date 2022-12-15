from typing import Union, List, Tuple, Literal, Dict

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from vinted_constants import PAGES_TIMEOUT
from vinted_member_page import VintedMemberPage


class VintedSellItemPage:
    page_xpath = "//div[contains(@id, 'InAppMessage')]/parent::body"

    add_photos_button_xpath = "//div[@class='media-select__input-content']//button"
    add_photos_input_xpath = "//input[@data-testid='add-photos-input']"
    loading_indicator_xpath = "//*[local-name()='circle']"

    title_textfield_xpath = "//input[@id='title']"

    description_textfield_xpath = "//textarea[@id='description']"

    category_textfield_xpath = "//input[@id='catalog_id']"
    category_dropdown_xpath = "//div[@class='input-dropdown']"
    category_arrow_back_button_xpath = "//span[@data-icon-name='arrow-left']/ancestor::button"
    category_generic_element_xpath = "//li[@class='pile__element']"
    category_by_name_element_xpath = "//div[contains(@class, 'Cell__title') and text()='{}']"
    category_expand_arrow_by_name_xpath = category_by_name_element_xpath + \
                                          "/ancestor::div[@role='presentation']/div[contains(@class, 'suffix')]"

    brand_textfield_xpath = "//input[@id='brand_id']"
    brand_dropdown_xpath = category_dropdown_xpath
    brand_by_name_xpath = category_by_name_element_xpath
    custom_brand_element_xpath = "//div[@id='custom-select-brand']"

    size_textfield_xpath = "//input[@id='size_id']"
    size_dropdown_xpath = "//div[@class='input-dropdown']"
    size_generic_element_xpath = category_generic_element_xpath

    item_status_textfield_xpath = "//input[@id='status_id']"
    item_status_xpath = item_status_textfield_xpath + \
                        "/following-sibling::div[@class='input-dropdown']//div[@id='status-{}']"

    color_textfield_xpath = "//input[@id='color']/following-sibling::div/span[contains(@data-icon-name, 'chevron-')]"
    color_dropdown_xpath = "//div[@class='input-dropdown']"
    color_by_name_xpath = category_by_name_element_xpath
    color_generic_element_xpath = category_generic_element_xpath

    price_textfield_xpath = "//input[@id='price']"

    package_size_xpath = "//div[contains(@data-testid, '{}-package-size')]"

    add_item_button_xpath = "//button[@data-testid='upload-form-save-button']/span"

    def __init__(self, driver: webdriver.Chrome):
        self.driver: webdriver = driver
        self.wait_for_essentials()

    def wait_for_essentials(self, timeout: Union[float, int] = PAGES_TIMEOUT) -> None:
        for element_xpath in [self.add_photos_button_xpath, self.title_textfield_xpath, self.description_textfield_xpath,
                              self.brand_textfield_xpath, self.item_status_textfield_xpath, self.price_textfield_xpath,
                              self.add_item_button_xpath]:
            WebDriverWait(self.driver, timeout=timeout).\
                until(EC.element_to_be_clickable((By.XPATH, self.page_xpath + element_xpath)))

    def add_photo_to_offer(self, photo_path: str):
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.add_photos_input_xpath).send_keys(photo_path)

    def add_photos_to_offer(self, photo_paths: List[str]) -> None:
        for photo_path in photo_paths:
            self.add_photo_to_offer(photo_path)
            self.wait_for_photo_to_fully_upload()

    def wait_for_photo_to_fully_upload(self, timeout: Union[int, float] = PAGES_TIMEOUT) -> None:
        try:
            WebDriverWait(self.driver, timeout=1). \
                until(EC.presence_of_element_located((By.XPATH, self.page_xpath + self.loading_indicator_xpath)))
        except TimeoutException:
            pass
        WebDriverWait(self.driver, timeout=timeout). \
            until_not(EC.presence_of_element_located((By.XPATH, self.page_xpath + self.loading_indicator_xpath)))

    def add_title_to_offer(self, title: str) -> None:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.title_textfield_xpath).send_keys(title)

    def add_description_to_offer(self, description: str) -> None:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath +
                                                    self.description_textfield_xpath).send_keys(description)

    def get_all_categories(self, expand_first: bool = False, hide_after: bool = False) \
            -> Dict[str, Union[str, Dict[str, dict]]]:
        if expand_first:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.category_textfield_xpath).click()
        found_category_elements = self.driver.find_elements(by=By.XPATH,
                                                            value=self.page_xpath + self.category_dropdown_xpath +
                                                                  self.category_generic_element_xpath)
        categories = {element.text: None for element in found_category_elements}
        for category_name in categories.keys():
            if self._has_subcategories(category_name):
                self.driver.find_element(by=By.XPATH,
                                         value=self.page_xpath + self.category_dropdown_xpath +
                                               self.category_by_name_element_xpath.format(category_name)).click()
                categories[category_name] = self.get_all_categories()
        try:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.category_dropdown_xpath +
                                                        self.category_arrow_back_button_xpath).click()
        except NoSuchElementException:
            pass
        return categories

    def _has_subcategories(self, category_name: str) -> bool:
        return not self.driver.find_elements(by=By.XPATH,
                                             value=self.page_xpath + self.category_dropdown_xpath +
                                                   self.category_expand_arrow_by_name_xpath.format(category_name))

    def choose_category(self, category_path: Union[List[str], Tuple[str]], expand_first: bool = True) -> None:
        if expand_first:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.category_textfield_xpath).click()
        for category_name in category_path:
            self.driver.find_element(by=By.XPATH,
                                     value=self.page_xpath + self.category_dropdown_xpath +
                                           self.category_by_name_element_xpath.format(category_name)).click()

    def choose_brand(self, brand: str) -> None:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.brand_textfield_xpath).click()
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.brand_textfield_xpath).send_keys(brand)
        try:
            custom_brand_element_xpath = self.page_xpath + self.brand_dropdown_xpath + self.custom_brand_element_xpath
            WebDriverWait(self.driver, timeout=2). \
                until(EC.element_to_be_clickable((By.XPATH, custom_brand_element_xpath)))
            self.driver.find_element(by=By.XPATH, value=custom_brand_element_xpath).click()
        except TimeoutException:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.brand_dropdown_xpath +
                                                        self.brand_by_name_xpath.format(brand))

    def choose_size(self, size: str) -> None:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.size_textfield_xpath).click()
        all_sizes = self.driver.find_elements(by=By.XPATH, value=self.page_xpath + self.size_dropdown_xpath +
                                                                 self.size_generic_element_xpath)
        all_sizes_values = [size_value.text.split(" / ") for size_value in all_sizes]
        for size_values, size_element in zip(all_sizes_values, all_sizes):
            if size in size_values:
                size_element.click()
                break

    def choose_condition(self, status: Literal["new with tag", "new without tag", "very good", "good", "good enough"]) \
            -> None:
        status_dict = {"new with tag": 6, "new without tag": 1, "very good": 2, "good": 3, "good enough": 4}
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.item_status_textfield_xpath).click()
        self.driver.find_element(by=By.XPATH, value=self.page_xpath +
                                                    self.item_status_xpath.format(status_dict[status])).click()

    def get_all_colors(self, expand_first: bool = True, hide_after: bool = True) -> List[str]:
        if expand_first:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.color_textfield_xpath).click()
        colors = [color.text for color in self.driver.find_elements(by=By.XPATH,
                                                                    value=self.page_xpath + self.color_dropdown_xpath +
                                                                          self.color_generic_element_xpath)]
        if hide_after:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.color_textfield_xpath).click()
        return colors

    def choose_colors(self, colors: Union[List[str], str], expand_first: bool = True, hide_after: bool = True) -> None:
        colors = [colors] if isinstance(colors, str) else colors[:2]
        if expand_first:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.color_textfield_xpath).click()
        for color in colors:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.color_dropdown_xpath +
                                                        self.color_by_name_xpath.format(color)).click()
        if hide_after:
            self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.color_textfield_xpath).click()

    def add_price(self, price: Union[int, float]) -> None:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.price_textfield_xpath).send_keys(price)

    def choose_package_size(self, package_size: Literal["S", "M", "L"]) -> None:
        package_size_dict = {"S": "small", "M": "medium", "L": "large"}
        self.driver.find_element(by=By.XPATH,
                                 value=self.page_xpath +
                                       self.package_size_xpath.format(package_size_dict[package_size])).click()

    def click_add_item_button(self) -> VintedMemberPage:
        self.driver.find_element(by=By.XPATH, value=self.page_xpath + self.add_item_button_xpath).click()
        return VintedMemberPage(self.driver)
