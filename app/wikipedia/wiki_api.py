from pprint import pprint
import requests


def recup_info_wiki(latitude, longitude):
    url_api = "https://fr.wikipedia.org/w/api.php"
    latitude = latitude
    longitude = longitude
    params_geo = {'format': 'json',
                  'action': 'query',
                  'list': 'geosearch',
                  'gsradius': 1000,
                  'gscoord': f"{latitude}|{longitude}"}
    response_geo = requests.get(url=url_api, params=params_geo)
    geosearch_data = response_geo.json()
    page_id = geosearch_data['query']['geosearch'][0]['pageid']
    params_page = {"format": "json",
                   "action": "query",
                   "prop": "extracts|info",
                   "inprop": "url",
                   "exchars": 1200,
                   "explaintext": True,
                   "pageids": page_id}
    response_page = requests.get(url_api, params_page)
    extract_data = response_page.json()
    page_id2 = None
    for item in extract_data['query']['pages']:
        page_id2 = item
    data = extract_data['query']['pages'][page_id2]
    return data['extract']





print(recup_info_wiki(48.8975156, 2.3833993))
# print(recup_info_wiki2('Hampi'))

# https://fr.wikipedia.org/w/api.php?action=query&titles=OpenClassrooms&prop=revisions&rvprop=content&rvsection=0&format=json
#
# import requests
#
# S = requests.Session()
#
# URL = "https://en.wikipedia.org/w/api.php"
#
# PARAMS = {
#     "action": "opensearch",
#     "namespace": "0",
#     "search": "Hampi",
#     "limit": "5",
#     "format": "json"
# }
#
# R = S.get(url=URL, params=PARAMS)
# DATA = R.json()
#
# print(DATA)
