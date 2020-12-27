# /usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def get_location(place):
    """ Returns the location and address of a place.

    Get the address, latitude and longitude of a given place in Google Maps.

    :param place: The place we want to find.
    :type place: str
    :return: A dictionary containing the address, latitude and longitude of the searched place.
    :rtype: dict
    """
    api_key = 'AIzaSyAYIr_H7RBFICU0eGWe7hrm6a4AuibiQjI'
    api_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': place,
              'key': api_key}
    response = requests.get(api_url, params)
    response_json = response.json()
    if response_json['status'] != 'ZERO_RESULTS':

        address = response_json['results'][0]['formatted_address']
        location = response_json['results'][0]['geometry']['location']
        return {'location': location, 'address': address}
    else:
        return False
