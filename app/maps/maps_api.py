import requests


def get_location(place):
    """ Returns the location and address of a place.

    Get the

    :param place:
    :return:
    """
    api_key = 'AIzaSyAYIr_H7RBFICU0eGWe7hrm6a4AuibiQjI'
    api_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': place,
              'key': api_key}
    response = requests.get(api_url, params)
    response_json = response.json()
    address = response_json['results'][0]['formatted_address']
    location = response_json['results'][0]['geometry']['location']
    return {'location': location, 'address': address}

