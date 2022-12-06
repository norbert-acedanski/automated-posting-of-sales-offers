from offers_data_handling.offers_data_collector import OffersDataCollector

if __name__ == "__main__":
    offers_data_collector = OffersDataCollector()
    print(offers_data_collector.get_offers_names())
    print(offers_data_collector.get_offer_properties("Sample offer 1"))
