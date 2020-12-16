from app.maps.maps_api import get_location


def test_get_location_returns_correct_locations(monkeypatch):
    results = {'location': {'lat': 48.856614, 'lng': 2.3522219}, 'address': 'Paris, France'}

    class MockRequestsGet:
        def __init__(self, url, params):
            self.url = url
            self.params = params

        def json(self):
            return {
                'results': [{
                    'address_components': [
                        {'long_name': 'Paris',
                         'short_name': 'Paris',
                         'types': ['locality', 'political']},
                        {'long_name': 'Paris',
                         'short_name': 'Paris',
                         'types': ['administrative_area_level_2', 'political']},
                        {'long_name': 'Île-de-France',
                         'short_name': 'IDF',
                         'types': ['administrative_area_level_1', 'political']},
                        {'long_name': 'France',
                         'short_name': 'FR',
                         'types': ['country', 'political']}],
                    'formatted_address': 'Paris, France',
                    'geometry': {
                        'bounds': {
                            'northeast': {'lat': 48.9021449, 'lng': 2.4699208},
                            'southwest': {'lat': 48.815573, 'lng': 2.224199}},
                        'location': {'lat': 48.856614, 'lng': 2.3522219},
                        'location_type': 'APPROXIMATE',
                        'viewport': {
                            'northeast': {'lat': 48.9021449, 'lng': 2.4699208},
                            'southwest': {'lat': 48.815573, 'lng': 2.224199}}},
                    'place_id': 'ChIJD7fiBh9u5kcRYJSMaMOCCwQ',
                    'types': ['locality', 'political']}],
                'status': 'OK'}

    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert get_location('Paris') == results
