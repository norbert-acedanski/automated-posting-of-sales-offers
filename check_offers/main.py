from check_offers import CheckOffersForSites

if __name__ == "__main__":
    offers_checker = CheckOffersForSites()
    offers_checker.check_title_lengths()
    offers_checker.check_description_lengths()
    offers_checker.check_number_of_photos()
    offers_checker.check_category_trees()
    offers_checker.check_sexes()
    offers_checker.check_prices()
    offers_checker.check_conditions()
    offers_checker.check_package_sizes()
