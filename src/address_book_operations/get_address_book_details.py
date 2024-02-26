

from geopy.distance import geodesic


#Method to calculate the distance
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers


#Method to get the details of  the addresses that are within a given distance and location coordinates.
async def get_address_book_details(address_details,latitude,longitude,distance):
    addresses_within_distance = []
    user_location = (latitude, longitude)
    for address in address_details:
        address_location = (address.latitude, address.longitude)
        if calculate_distance(user_location, address_location) <= distance:
            addresses_within_distance.append(address)
    return addresses_within_distance