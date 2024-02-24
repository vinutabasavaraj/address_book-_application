

def calculate_distance(lat1, lon1, lat2, lon2):
    # In reality, you'd use a more accurate distance calculation method
    return ((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2) ** 0.5


async def get_address_book_details(address_details,latitude,longitude,distance):
    addresses_within_distance = []
    for address in address_details:
        if calculate_distance(latitude, longitude, address["latitude"], address["longitude"]):
            addresses_within_distance.append(address)
    return addresses_within_distance