class PostOLX():
    button_add_offer_xpath = "//button[@data-cy='post-new-ad-button']"

    textfield_title_xpath = "//textarea[@name='title']"
    dropdown_menu_category_xpath = "//p[@class='css-rflibz-Text eu5v0x0']"
    button_photos_xpath = "(//input[@id='photo-attachment-files'])[1]"
    textfield_description_xpath = "//textarea[@name='description']"
    textfield_price_xpath = "//input[@data-testid='price-input']"
    switch_negotiate_xpath = "(//input[@data-testid='negotiable-switch'] //.. // span)[1]"

    button_private_offer_xpath = "(//button[@class='css-19wrg31'])[1]"
    button_business_offer_xpath = "(//button[@class='css-19wrg31'])[2]"

    dropdown_menu_state_xpath = "//label[contains(text()='Stan')] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_state_choice_xpath = "//a[text()='choice']"

    dropdown_menu_size_xpath = "//label[contains(text(), 'Rozmiar')] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_size_choice_xpath = "//a[text()='choice']"

    dropdown_menu_color_xpath = "//label[text()='Kolor'] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_color_choice_xpath = "//ul[@data-testid='dropdown-list'] //*[text()='choice']"

    dropdown_menu_brand_xpath = "//label[text()='Marka'] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_brand_choice_xpath = "//ul[@data-testid='dropdown-list'] //*[text()='choice']"

    dropdown_menu_meterial_xpath = "//label[text()='Materiał'] //.. //button[@data-testid='dropdown-expand-button']"
    dropdown_menu_meterial_choice_xpath = "//ul[@data-testid='dropdown-list'] //*[text()='choice']"

    switch_autorenewal_xpath = "(//p[text()='AutoPrzedłużenie'] //.. //.. //.. //span)[1]"

    button_add_offer_xpath = "//button[@data-testid='submit-btn']"

class PostAllegroLokalnie():
    pass

class PostSprzedajemy():
    pass

class PostVinted():
    pass