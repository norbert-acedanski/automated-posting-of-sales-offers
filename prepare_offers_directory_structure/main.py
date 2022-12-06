from prepare_offers_directory_structure import PrepareOffersDirectoryStructure

if __name__ == "__main__":
    prepare_offers = PrepareOffersDirectoryStructure()
    prepare_offers.add_offers_directories_with_photos_folders(number_of_offers=5)
    prepare_offers.add_properties_file_to_each_offer_directory()
