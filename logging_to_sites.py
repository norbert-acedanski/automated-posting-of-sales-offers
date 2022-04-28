class LoginOLX:
    
    button_cookies_more_xpath = "//button[text()='Pokaż cele']"
    button_cookies_accept_xpath = "//button[text()='Potwierdzenie moich wyborów']"
    button_my_olx_xpath = "//strong[text()='Mój OLX']"
    textbox_email_xpath = "(//input[@id='userEmail'])[1]"
    textbox_password_xpath = "(//input[@id='userPass'])[1]"
    button_login_xpath = "(//button[text()='Zaloguj się'])[1]"
    button_logout_xpath = "//a[text()='Wyloguj']"
    
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        self.driver.find_element_by_xpath(self.button_cookies_more_xpath).click()
        self.driver.find_element_by_xpath(self.button_cookies_accept_xpath).click()

    def click_my_olx(self):
        self.driver.find_element_by_xpath(self.button_my_olx_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

class LoginAllegroLokalnie:
    button_cookies_not_accept_xpath = "//button[text()='Nie zgadzam się']"
    button_go_to_login_xpath = "//a[@data-testid='header-menu__login']"
    button_change_cookies_xpath = "//button[text()='Zmieniam zgody']"
    button_cookies_accept_xpath = "//button[text()='Potwierdź wybór']"
    textbox_login_xpath = "//input[@name='login']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "//a[@data-to='/auth/logout']"
    
    def __init__(self, driver):
        self.driver = driver

    def reject_cookies(self):
        self.driver.find_element_by_xpath(self.button_cookies_not_accept_xpath).click()

    def click_login_page(self):
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

    def click_logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

class LoginSprzedajemy:
    textbox_email_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "//a[@class='logout']"
    
    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

class LoginVinted:
    button_cookies_not_accept_xpath = "//button[@id='onetrust-reject-all-handler']"
    button_go_to_login_1_xpath = "(//span[text()='Zarejestruj się | Zaloguj się'])[1]"
    button_go_to_login_2_xpath = "//span[text()='Zaloguj się']"
    button_go_to_login_3_xpath = "//a[@data-testid='auth-select-type--login-email']"
    textbox_login_xpath = "//input[@id='username']"
    textbox_password_xpath = "//input[@id='password']"
    button_login_xpath = "//span[text()='Kontynuuj']"
    button_logout_xpath = "//a[text()='Wyloguj się']"
    
    def __init__(self, driver):
        self.driver = driver

    def reject_cookies(self):
        self.driver.find_element_by_xpath(self.button_cookies_not_accept_xpath).click()

    def go_to_login(self):
        self.driver.find_element_by_xpath(self.button_go_to_login_1_xpath).click()
        self.driver.find_element_by_xpath(self.button_go_to_login_2_xpath).click()
        self.driver.find_element_by_xpath(self.button_go_to_login_3_xpath).click()


    def set_login(self, email):
        self.driver.find_element_by_xpath(self.textbox_login_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_login_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()