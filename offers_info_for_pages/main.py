from offers_info_for_pages import OffersInfoForPages

if __name__ == "__main__":
    offers_info = OffersInfoForPages()
    offers_info.print_bounds_for_title()
    offers_info.print_bounds_for_description()
    offers_info.print_photos_restrictions()
    offers_info.print_conditions_restrictions()
    offers_info.print_sexes_restrictions()
    offers_info.print_package_size_restrictions()
