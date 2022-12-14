class OLXLimits:
    title = {"min": 16, "max": 70}
    description = {"min": 80, "max": 9000}
    number_of_photos = {"min": 1, "max": 8}


class AllegroLokalnieLimits:
    title = {"min": 1, "max": 50}
    description = {"min": 1, "max": 3000}
    number_of_photos = {"min": 1, "max": 15}


class SprzedajemyLimits:
    title = {"min": 3, "max": 60}
    description = {"min": 1, "max": 6000}
    number_of_photos = {"min": 1, "max": 12}


class VintedLimits:
    title = {"min": 5, "max": 100}
    description = {"min": 5, "max": 3000}
    number_of_photos = {"min": 1, "max": 20}


class GeneralLimits:
    sexes = ["M", "K", "U"]  # M - men, K - woman, U - universal
    conditions = ["fine", "good", "very good", "new without a tag", "new with a tag"]
    package_sizes = ["S", "M", "L"]
