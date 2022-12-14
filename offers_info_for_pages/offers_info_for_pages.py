from colors.colors import ForegroundColors as FC, BackgroundColors as BC, Styles


class OffersInfoForPages:
    def __init__(self):
        self.title_boundaries = {"OLX": {"min": 16, "max": 70}, "Allegro Lokalnie": {"min": 1, "max": 50},
                                 "Sprzedajemy": {"min": 3, "max": 60}, "Vinted": {"min": 5, "max": 100}}
        self.description_boundaries = {"OLX": {"min": 80, "max": 9000}, "Allegro Lokalnie": {"min": 1, "max": 3000},
                                       "Sprzedajemy": {"min": 1, "max": 6000}, "Vinted": {"min": 5, "max": 3000}}
        self.number_of_photos_boundaries = {"OLX": {"min": 1, "max": 8}, "Allegro Lokalnie": {"min": 1, "max": 15},
                                            "Sprzedajemy": {"min": 1, "max": 12}, "Vinted": {"min": 1, "max": 20}}
        self.sexes = ["M - men", "K - woman", "U - universal"]
        self.conditions = ["fine", "good", "very good", "new without a tag", "new with a tag"]
        self.package_sizes = ["S", "M", "L"]

    def print_limits_for_title(self):
        print(FC.GREEN + "Title limits [characters]:" + FC.RESET)
        for site, value in self.title_boundaries.items():
            print(FC.YELLOW + site + FC.RESET + ": min - " + FC.BLUE + str(value["min"]) + FC.RESET + ", max - " +
                  FC.BLUE + str(value["max"]) + FC.RESET)
        print("Valid for: 06.12.2022")
        print("")

    def print_limits_for_description(self):
        print(FC.GREEN + "Description limits [characters]:" + FC.RESET)
        for site, value in self.description_boundaries.items():
            print(FC.YELLOW + site + FC.RESET + ": min - " + FC.BLUE + str(value["min"]) + FC.RESET + ", max - " +
                  FC.BLUE + str(value["max"]) + FC.RESET)
        print("Valid for: 06.12.2022")
        print("")

    def print_limits_for_photos(self):
        print(FC.GREEN + "Number of photos limits:" + FC.RESET)
        for site, value in self.number_of_photos_boundaries.items():
            print(FC.YELLOW + site + FC.RESET + ": min - " + FC.BLUE + str(value["min"]) + FC.RESET + ", max - " +
                  FC.BLUE + str(value["max"]) + FC.RESET)
        print("Valid for: 06.12.2022")
        print("")

    def print_limits_for_restrictions(self):
        print(FC.GREEN + "Acceptable list of conditions:" + FC.RESET)
        for condition in self.conditions:
            print("* " + FC.BLUE + condition + FC.RESET)
        print("")

    def print_limits_for_sexes(self):
        print(FC.GREEN + "Acceptable sexes marks:" + FC.RESET)
        for sex in self.sexes:
            print("* " + FC.BLUE + sex + FC.RESET)
        print("")

    def print_limits_for_package_sizes(self):
        print(FC.GREEN + "Acceptable sizes of the package:" + FC.RESET)
        for package_size in self.package_sizes:
            print("* " + FC.BLUE + package_size + FC.RESET)
        print("")
