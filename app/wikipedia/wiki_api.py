# /usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def get_pageid(latitude, longitude):
    """ Returns the ID of a Wikipedia page.

    Get the ID of the Wikipedia page of a place given by its latitude and longitude.

    :param latitude: The latitude of the place.
    :type latitude: float
    :param longitude: The longitude of the place.
    :type longitude: float
    :return: The ID of the Wikipedia page.
    :rtype: int
    """
    latitude = latitude
    longitude = longitude
    url_api = "https://fr.wikipedia.org/w/api.php"
    params_geo = {'format': 'json',
                  'action': 'query',
                  'list': 'geosearch',
                  'gsradius': 1000,
                  'gscoord': f"{latitude}|{longitude}"}
    response_geo = requests.get(url=url_api, params=params_geo)
    geosearch_data = response_geo.json()
    if 'batchcomplete' in geosearch_data:
        if geosearch_data['query']['geosearch']:
            page_id = geosearch_data['query']['geosearch'][0]['pageid']
            return page_id
        else:
            return False
    else:
        return False


def get_history(page_id):
    """ Returns the historical part of the information of a Wikipedia page.

    Get the historical part of the information of a Wikipedia page using its ID.

    :param page_id: The ID of the Wikipedia page.
    :type page_id: int
    :return: The historical part of the information of the Wikipedia page.
    :rtype: str
    """
    url_api = "https://fr.wikipedia.org/w/api.php"
    params_page = {"format": "json",
                   "action": "query",
                   "prop": "extracts|info",
                   "inprop": "url",
                   "exchars": 1200,
                   "explaintext": True,
                   "pageids": page_id}
    response_page = requests.get(url_api, params_page)
    extract_data = response_page.json()
    page_id_string = str(page_id)
    if 'missing' not in extract_data['query']['pages'][page_id_string]:
        data = extract_data['query']['pages'][page_id_string]['extract']
        return data
    else:
        return False
