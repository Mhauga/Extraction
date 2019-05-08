import requests
import openpyxl

def get_business_lists(city):
    print(city)

    # API Definition
    my_API_Key = "DbicrMm0HPuDhJIfDZeyJDHPSx1DOOJhvYJ9RGw9dnO_99veGi2XzxDknfAlEi8rcwm_3wOg6t239020EZAPfJKiaGOLtPPCPCuO1XmkhXto_2yk4wgQU-g-WiTSXHYx"
    endPoint = "https://api.yelp.com/v3/businesses/search"
    api_headers = {'Authorization': 'bearer {}'.format(my_API_Key)}

    # Parameters
    offset = 0
    limit = 50
    total = 1000

    # Variable declarations
    biz_name = []
    biz_address = []
    biz_phone = []

    while offset < total:
        parameters = {"term": "Restaurants",
                     "limit": limit,
                     "location": city,
                     "price": "2,3",
                     "sort_by": "rating",
                     "offset": offset}

        #  Make the request and then convert the json to a dictionary
        businesses_json_response = requests.get(url=endPoint, params=parameters, headers=api_headers)
        businesses = businesses_json_response.json()



        # Update Total
        try:
            total = businesses["total"]
        except:
            print("Total is less than 50")
            break

        # Append business names, addresses, and phones to their respective lists
        for business in businesses["businesses"]:
            biz_name.append(business["name"])
            biz_address.append(business["location"]["address1"])
            biz_phone.append(business['display_phone'])

        if total - limit >= 50:
            offset += 50
        elif total - limit < 50:
            offset += (total - limit)
            limit = (total - limit)

    return

def main():
    MSA_Columbus = (
        "Columbus", "Dublin", "Newark", "Delaware", "Lancaster", "Pickerington", "London", "Marysville", "Circleville",
        "Marion", "Zanesville", "Chillicothe", "New Lexington", "Cambridge", "Washington Court House")
    MSA_Dayton = ("Centerville", "Dayton", "Kettering", "Beavercreek", "Huber Heights", "Fairborn", "Miamisburg",
                  "West Carrollton", "Springfield", "Urbana", "Greenville", "Sidney")

    for city in MSA_Dayton:
        get_business_lists(city)


# BEGIN PROGRAM
main()