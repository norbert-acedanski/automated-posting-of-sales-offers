from offers_data_handling.offers_data_collector import OffersDataCollector
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
    data_collector = OffersDataCollector()
    offers_names = data_collector.get_offers_names()
    for offer_name in offers_names:
        vinted_sell_page = vinted_main_page.click_sell_button()
        current_offer_properties = data_collector.get_offer_properties(offer_name)
        vinted_sell_page.add_photos_to_offer(current_offer_properties["photos"])
        vinted_sell_page.add_title_to_offer(current_offer_properties["title"])
        vinted_sell_page.add_description_to_offer(current_offer_properties["description"])
        vinted_sell_page.choose_category(current_offer_properties["category"]["vinted"])
        vinted_sell_page.choose_brand(current_offer_properties["brand"])
        vinted_sell_page.choose_size(current_offer_properties["size"])
        vinted_sell_page.choose_condition(current_offer_properties["condition"])
        vinted_sell_page.choose_colors(current_offer_properties["colors"])
        vinted_sell_page.add_price(current_offer_properties["price"])
        vinted_sell_page.choose_package_size(current_offer_properties["package size"])
        vinted_sell_page.click_add_item_button()
