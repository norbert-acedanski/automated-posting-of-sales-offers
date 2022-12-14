from colors.colors import ForegroundColors as FC, BackgroundColors as BC, Styles
from common.limits import GeneralLimits, OLXLimits, AllegroLokalnieLimits, SprzedajemyLimits, VintedLimits


class OffersInfoForPages:
    def __init__(self):
        self.title_boundaries = {"OLX": OLXLimits.title, "Allegro Lokalnie": AllegroLokalnieLimits.title,
                                 "Sprzedajemy": SprzedajemyLimits.title, "Vinted": VintedLimits.title}
        self.description_boundaries = {"OLX": OLXLimits.description,
                                       "Allegro Lokalnie": AllegroLokalnieLimits.description,
                                       "Sprzedajemy": SprzedajemyLimits.description,
                                       "Vinted": VintedLimits.description}
        self.number_of_photos_boundaries = {"OLX": OLXLimits.number_of_photos,
                                            "Allegro Lokalnie": AllegroLokalnieLimits.number_of_photos,
                                            "Sprzedajemy": SprzedajemyLimits.number_of_photos,
                                            "Vinted": VintedLimits.number_of_photos}
        self.sexes = GeneralLimits.sexes
        self.conditions = GeneralLimits.conditions
        self.package_sizes = GeneralLimits.package_sizes

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
