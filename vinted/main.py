from open_vinted_page import open_vinted_main_page
from vinted_main_page import VintedMainPage


if __name__ == "__main__":
    vinted_main_page: VintedMainPage = open_vinted_main_page()
    vinted_main_page.choose_cookies_option(option="reject")
    vinted_login_register_modal = vinted_main_page.click_register_login_button()
    vinted_login_register_modal.switch_login_register(to_option="login")
    vinted_login_modal = vinted_login_register_modal.click_login_by_email()
    vinted_login_modal.fill_email_profile_name("Sample profile name")
    vinted_login_modal.fill_password(password="Sample Password")
    vinted_login_modal.click_continue_button()
    vinted_main_page.wait_for_essentials()
    vinted_sell_page = vinted_main_page.click_sell_button()
    photos_paths = []  # With an empty list, a trash offer will not be posted
    vinted_sell_page.add_photos_to_offer(photos_paths)
    vinted_sell_page.add_title_to_offer("Sample title")
    vinted_sell_page.add_description_to_offer("Small description")
    vinted_sell_page.choose_category(["Kobiety", "Ubrania", "Okrycia wierzchnie", "Peleryny i poncza"])
    vinted_sell_page.choose_brand("Sample")
    vinted_sell_page.choose_size("XS")
    vinted_sell_page.choose_status("new without tag")
    vinted_sell_page.choose_colors(["Czarny", "Beżowy"])
    vinted_sell_page.add_price(100)
    vinted_sell_page.choose_package_size("M")
    vinted_sell_page.click_add_item_button()
