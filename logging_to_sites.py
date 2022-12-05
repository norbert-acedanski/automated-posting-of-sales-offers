import time

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains

class LoginOLX:
    
    button_cookies_more_xpath = "//button[text()='Pokaż cele']"
    button_cookies_accept_xpath = "//button[text()='Potwierdzenie moich wyborów']"
    button_my_olx_xpath = "//strong[text()='Mój OLX']"
    textbox_email_1_xpath = "//input[@id='userEmail']"
    textbox_email_2_xpath = "//input[@name='username']"
    textbox_password_1_xpath = "//input[@id='userPass']"
    textbox_password_2_xpath = "//input[@name='password']"
    button_login_1_xpath = "//button[@type='submit']"
    button_login_2_xpath = "//button[@id='se_userLogin']"
    dropdown_menu_xpath = "//a[@class='userbox-login tdnone']"
    button_logout_xpath = "//a[@id='login-box-logout']"
    
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        self.driver.find_element_by_xpath(self.button_cookies_more_xpath).click()
        self.driver.find_element_by_xpath(self.button_cookies_accept_xpath).click()

    def click_my_olx(self):
        self.driver.find_element_by_xpath(self.button_my_olx_xpath).click()

    def set_email(self, email):
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath(self.textbox_email_1_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_email_1_xpath).send_keys(email)
        except NoSuchElementException:
            time.sleep(1)
            self.driver.find_element_by_xpath(self.textbox_email_2_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_email_2_xpath).send_keys(email)

    def set_password(self, password):
        try:
            self.driver.find_element_by_xpath(self.textbox_password_1_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_password_1_xpath).send_keys(password)
        except NoSuchElementException:
            self.driver.find_element_by_xpath(self.textbox_password_2_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_password_2_xpath).send_keys(password)

    def click_login(self):
        try:
            self.driver.find_element_by_xpath(self.button_login_1_xpath).click()
        except ElementNotInteractableException:
            self.driver.find_element_by_xpath(self.button_login_2_xpath).click()

    def click_logout(self):
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath(self.button_logout_xpath).click()
        except ElementNotInteractableException:
            time.sleep(1)
            dropdown_menu = self.driver.find_element_by_xpath(self.dropdown_menu_xpath)
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(dropdown_menu).perform()
            self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def login_to_page(self, login, password):
        self.accept_cookies()
        self.click_my_olx()
        self.set_email(login)
        self.set_password(password)
        self.click_login()

class LoginAllegroLokalnie:
    button_cookies_not_accept_xpath = "//button[text()='Nie zgadzam się']"
    button_extend_menu_xpath = "//button[@aria-controls='masthead-menu']"
    button_go_to_login_xpath = "//a[@data-testid='header-menu__login']"
    button_change_cookies_xpath = "//button[text()='Zmieniam zgody']"
    button_cookies_accept_xpath = "//button[text()='Potwierdź wybór']"
    textbox_login_xpath = "//input[@name='login']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"
    button_confirm_not_robot_1_xpath = "(//button[@type='submit'])[1]"
    button_confirm_not_robot_2_xpath = "//span[@class='geetest_radar_tip_content']"
    button_logout_xpath = "//a[@data-to='/auth/logout']"
    
    def __init__(self, driver):
        self.driver = driver

    def reject_cookies(self):
        self.driver.find_element_by_xpath(self.button_cookies_not_accept_xpath).click()

    def click_login_page(self):
        self.driver.find_element_by_xpath(self.button_extend_menu_xpath).click()
        self.driver.find_element_by_xpath(self.button_go_to_login_xpath).click()

    def change_cookies(self):
        self.driver.find_element_by_xpath(self.button_change_cookies_xpath).click()
        self.driver.find_element_by_xpath(self.button_cookies_accept_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.textbox_login_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_login_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def confirm_not_robot(self):
        number_of_tries = 0
        while number_of_tries < 5:
            try:
                time.sleep(1)
                self.driver.find_element_by_xpath(self.button_confirm_not_robot_1_xpath).click()
                self.driver.find_element_by_xpath(self.button_confirm_not_robot_2_xpath).click()
                break
            except NoSuchElementException:
                number_of_tries += 1
        else:
            input("Please fill captcha if visible, then click enter...")

    def click_logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def login_to_page(self, login, password):
        self.reject_cookies()
        self.click_login_page()
        self.confirm_not_robot()
        self.change_cookies()
        self.set_email(login)
        self.set_password(password)
        self.click_login()
        self.confirm_not_robot()

class LoginSprzedajemy:
    button_accept_cookies_xpath = "//span[text()='Zaakceptuj i zamknij']"
    button_extend_menu_xpath = "(//strong[text()='Zaloguj się'])[1]"
    textbox_email_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    button_login_xpath = "//button[@type='submit']"
    dropdown_menu_xpath = "//div[@class] / span //strong /parent::*/parent::*"
    button_logout_xpath = "//a[@class='logout']"
    
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        self.driver.find_element_by_xpath(self.button_accept_cookies_xpath).click()

    def extend_menu(self):
        self.driver.find_element_by_xpath(self.button_extend_menu_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.dropdown_menu_xpath).click()
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def login_to_page(self, login, password):
        self.accept_cookies()
        self.extend_menu()
        self.set_email(login)
        self.set_password(password)
        self.click_login()
