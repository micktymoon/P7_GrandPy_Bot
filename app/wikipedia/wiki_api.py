import wikipedia
import requests


def recup_info_wiki(recherche):
    session = requests.Session()
    url_api = "https://fr.wikipedia.org/w/api.php"
    param = {'action': 'query',
             'titles': recherche,
             'prop': 'extracts',
             'exsentences': 1,
             'format': 'json'}
    response = session.get(url=url_api, params=param)
    response_json = response.json()
    return response_json['query']['pages']





print(recup_info_wiki('OpenClassrooms'))

# https://fr.wikipedia.org/w/api.php?action=query&titles=OpenClassrooms&prop=revisions&rvprop=content&rvsection=0&format=json