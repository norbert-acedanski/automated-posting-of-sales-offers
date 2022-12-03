from contextlib import suppress
from selenium.common.exceptions import NoSuchElementException

from main import PRIVATE_OFFER

class PostOLX():
    button_add_new_offer_xpath = "//button[@data-cy='post-new-ad-button']"

    textfield_title_xpath = "//textarea[@name='title']"
    dropdown_menu_category_xpath = "//p[@class='css-rflibz-Text eu5v0x0']"
    button_photos_xpath = "(//input[@id='photo-attachment-files'])[1]"
    textfield_description_xpath = "//textarea[@name='description']"
    textfield_price_xpath = "//input[@data-testid='price-input']"
    switch_negotiate_xpath = "(//input[@data-testid='negotiable-switch'] //.. // span)[1]"

    button_offer_kind_xpath = "//button[text()='choice']"

    dropdown_menu_condition_xpath = "//label[contains(text(), 'Stan')] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_condition_choice_xpath = "//a[text()='choice']"

    dropdown_menu_size_xpath = "//label[contains(text(), 'Rozmiar')] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_size_choice_xpath = "//a[text()='choice']"

    dropdown_menu_sex_xpath = "//label[contains(text(), 'Płeć')] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_sex_choice_xpath = "//a[text()='choice']"

    dropdown_menu_color_xpath = "//label[text()='Kolor'] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_color_choice_xpath = "//ul[@data-testid='dropdown-list'] //*[text()='choice']"

    dropdown_menu_brand_xpath = "//label[text()='Marka'] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_brand_choice_xpath = "//ul[@data-testid='dropdown-list'] //*[text()='choice']"

    dropdown_menu_material_xpath = "//label[text()='Materiał'] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_material_choice_xpath = "//ul[@data-testid='dropdown-list'] //*[text()='choice']"

    switch_autorenewal_xpath = "(//p[text()='AutoPrzedłużenie'] //.. //.. //.. //span)[1]"

    button_add_offer_xpath = "//button[@data-testid='submit-btn']"
    
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_offer(self):
        self.driver.find_element_by_xpath(self.button_add_new_offer_xpath).click()

    def add_title(self, title):
        self.driver.find_element_by_xpath(self.textfield_title_xpath).clear()
        self.driver.find_element_by_xpath(self.textfield_title_xpath).send_keys(title)

    def add_category(self, category):
        pass

    def add_photos(self, path):
        self.driver.find_element_by_xpath(self.button_photos_xpath).send_keys(path)

    def add_description(self, description):
        self.driver.find_element_by_xpath(self.textfield_description_xpath).send_keys(description)

    def add_price(self, price):
        self.driver.find_element_by_xpath(self.textfield_price_xpath).send_keys(price)

    def switch_negotiable(self, negotiable=False):
        if negotiable:
            self.driver.find_element_by_xpath(self.switch_negotiate_xpath).click()

    def set_offer_kind(self, offer_kind=PRIVATE_OFFER):
        self.driver.find_element_by_xpath(self.button_offer_kind_xpath.replace("choice", offer_kind)).click()

    def set_offer_condition(self, offer_condition):
        try:
            self.driver.find_element_by_xpath(self.dropdown_menu_condition_xpath).click()
            self.driver.find_element_by_xpath(self.dropdown_menu_condition_choice_xpath.replace("choice", offer_condition)).click()
        except NoSuchElementException:
            pass

    def set_offer_size(self, offer_size):
        try:
            self.driver.find_element_by_xpath(self.dropdown_menu_size_xpath).click()
            self.driver.find_element_by_xpath(self.dropdown_menu_size_choice_xpath.replace("choice", offer_size)).click()
        except NoSuchElementException:
            pass

    def set_offer_sex(self, offer_sex):
        try:
            self.driver.find_element_by_xpath(self.dropdown_menu_sex_xpath).click()
            self.driver.find_element_by_xpath(self.dropdown_menu_sex_choice_xpath.replace("choice", offer_sex)).click()
        except NoSuchElementException:
            pass

    def set_offer_color(self, offer_color):
        try:
            self.driver.find_element_by_xpath(self.dropdown_menu_color_xpath).click()
            self.driver.find_element_by_xpath(self.dropdown_menu_color_choice_xpath.replace("choice", offer_color)).click()
        except NoSuchElementException:
            pass

    def set_offer_brand(self, offer_brand):
        try:
            self.driver.find_element_by_xpath(self.dropdown_menu_brand_xpath).click()
            self.driver.find_element_by_xpath(self.dropdown_menu_brand_choice_xpath.replace("choice", offer_brand)).click()
        except NoSuchElementException:
            pass

    def set_offer_material(self, offer_material):
        try:
            self.driver.find_element_by_xpath(self.dropdown_menu_material_xpath).click()
            self.driver.find_element_by_xpath(self.dropdown_menu_material_choice_xpath.replace("choice", offer_material)).click()
        except NoSuchElementException:
            pass

    def switch_auto_renewal(self, renew=True):
        if renew:
            self.driver.find_element_by_xpath(self.switch_autorenewal_xpath).click()

    def click_add_offer(self):
        self.driver.find_element_by_xpath(self.button_add_offer_xpath).click()

    def fill_offer_with_data(self, data: dict, path, negotiable_price=False, offer_kind=PRIVATE_OFFER, auto_renewal=True):
        title = data["title"]
        category = data["category"]
        description = data["description"]
        price = data["price"]
        with suppress(KeyError): condition = data["condition"]
        with suppress(KeyError): size = data["size"]
        with suppress(KeyError): sex = data["sex"]
        with suppress(KeyError): color = data["color"][0]
        with suppress(KeyError): brand = data["brand"]
        with suppress(KeyError): material = data["material"]
        self.add_title(title)
        self.add_category(category)
        self.add_photos(path)
        self.add_description(description)
        self.add_price(price)
        self.switch_negotiable(negotiable_price)
        self.set_offer_kind(offer_kind)
        self.set_offer_condition(condition)
        self.set_offer_size(size)
        self.set_offer_sex(sex)
        self.set_offer_color(color)
        self.set_offer_brand(brand)
        self.set_offer_material(material)
        self.switch_auto_renewal(auto_renewal)

class PostAllegroLokalnie():
    pass

class PostSprzedajemy():
    feedback_modal_xpath = "//div[@data-testid='feedback-modal']"
    feedback_modal_close_xpath = "//button[@data-testid='feedback-resolved-close']"

class PostVinted():
    pass