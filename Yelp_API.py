# Name: Yelp_API
# Purpose: To download a list of business names, addresses, phone numbers, and city, state
#           and output to an excel document.

# Business Search Endpoint Url: " https://api.yelp.com/v3/businesses/search"

# Import Modules
import requests

# Yelp Documentation URL:   https://www.yelp.com/developers/documentation/v3/business_search

#  Define API
my_API_Key = "DbicrMm0HPuDhJIfDZeyJDHPSx1DOOJhvYJ9RGw9dnO_99veGi2XzxDknfAlEi8rcwm_3wOg6t239020EZAPfJKiaGOLtPPCPCuO1XmkhXto_2yk4wgQU-g-WiTSXHYx"
endPoint = "https://api.yelp.com/v3/businesses/search"
api_headers = {'Authorization': 'bearer {}'.format(my_API_Key)}

# Define parameters
parameters = {"term":"Restaurants",
              "limit": 30,
              "location":"Dayton",
              "price": "2,3",
              "sort_by": "rating",
              "offset": 0}

# Make Request to the API

response = requests.get(url=endPoint, params=parameters, headers=api_headers)

# Convert JSON to dictionary
business_data = response.json()

# Read dictionary
print(business_data["total"])
for biz in business_data["businesses"]:
    print("{:<35}".format(biz['name']), end="\t")
    print(biz["location"]["address1"], end="\t")
    print(biz['display_phone'])