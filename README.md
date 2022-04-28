# automated-issuing-of-sales-offers

# About The Project
Script allows to automatically post sales offers in four polish sales portals: OLX, Allegro Lokalnie, Sprzedajemy, Vinted.

# Built With
Python 3.9.10

# Getting started
### Methods:
- ***add_offer_folders_with_photos(list_of_offers)*** - accepts a list with offers' names and creates a folder & file structure in **offers_to_post** directory. 
- ***add_properties_file_to_each_offer_folder*** - iterates through all folders in **offers_to_post** directory and adds sample **properties.json** file to each. It is the model of the file to read data from and stores information such as title, description, size etc. about the offer. If any file exists, will not be overwritten.  
After creating files, fill it with the information about the items to post.
- ***print_bounds_for_title*** and ***print_bounds_for_description*** - these methods print the boundaries for title and description in all portals [as of the day 18.04.2022]
- ***check_title_lengths***, ***check_description_lengths*** and ***print_photos_restrictions*** - these methods iterate through all folders in **offers_to_post** directory, load data from **properties.json** file and check lengths of titles and descriptions in each. They also check number of photos for each offer and extensions of these offers.  
It is handy to check these kinds of information before starting the process of automated posting.

### Working with automated-issuing-of-sales-offers:
1. Run the tests from .\tests\ directory to ensure proper setup before running the script.
2. In **offers_to_post** directory, all folders for desired items should be placed (name is not important). In these folders, there should be folder for photos and file with proper information about the item. To do that, use ***add_offer_folders_with_photos_and_properties*** method, that accepts the list of the folder names and then - ***add_properties_file_to_each_offer_folder***.
3. In each offer, modify **properties.json** file with the proper information. All properties should be included, otherwise the script will fail.
4. Add photos of items to .\photos\ directories in all folders.
5. To see what are limitations, when posting an offer in a particular site, use ***print_all_limitations*** to print all limitations or use ***print_bounds_for_title***, ***print_bounds_for_description***, ***print_photos_restrictions***, ***print_sexes_restrictions*** methods. The result will be printed in the terminal.
6. Check, whether the information included in **properties.json** file and photos meet the expectations of the sites the script will post them in. To do that, use ***check_all_properties*** to go through all offers you created and check each individually or use ***check_title_lengths***, ***check_description_lengths***, ***check_number_of_photos_and_extension***, ***check_sex_of_the_item*** methods. The result will be printed in the terminal.

# To Do:
- add method, that checks the price of the item
- add method, that checks the colors of the item
- add method, that checks the package size of the item
- add method, that checks the condition of the item
- add method, that checks the category of the item (later if the list of categories is stored)
- add coloring of the output properties of properties
- add method, that reads login and password for each site
- add basic login and logout method for each site
- add login and logout tests
- add checking proper site tests
- add posting method for each site
- add posting tests

# Licence
Distributed under the MIT License. See LICENSE file for more information.
