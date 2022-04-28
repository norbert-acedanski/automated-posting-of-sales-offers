from prepare_and_check_offers import PrepareAndCheckOffers

if __name__ == "__main__":
    offer_poster = PrepareAndCheckOffers()
    offer_poster.add_offer_folders_with_photos(["Sample offer 1", "Sample offer 2"])
    offer_poster.add_properties_file_to_each_offer_folder()
    offer_poster.print_all_limitations()
    offer_poster.check_all_properties()