from bs4 import BeautifulSoup
from app.routes import app


def test_catchphrase_present():
    with app.test_client() as test_client:
        response = test_client.get("/accueil")
        result = response.data.decode("utf-8")
    r_soup = BeautifulSoup(result, "html.parser")
    tag = r_soup.h1
    assert tag.string == "GrandPyBot raconte moi une histoire!"


def test_page_accueil_status_code_is_ok():
    with app.test_client() as test_client:
        response = test_client.get("/accueil")
        assert response.status_code == 200


def test_mock_all_function_and_returns_all_info(monkeypatch):
    results = b'{"address":"test adresse",' \
              b'"history":"test historique",' \
              b'"latlng":{"lat":1,"lng":2},' \
              b'"place":"test_lieu"}\n'
    client = app.test_client()

    def mock_parser(text):
        return "test_lieu"

    monkeypatch.setattr('app.routes.function_parser', mock_parser)

    def mock_get_location(place):
        return {'location': {'lat': 1, 'lng': 2},
                'address': 'test adresse'}

    monkeypatch.setattr('app.routes.get_location', mock_get_location)

    def mock_get_pageid(lat, long):
        return 10

    monkeypatch.setattr('app.routes.get_pageid', mock_get_pageid)

    def mock_get_history(page_id):
        return "test historique"

    monkeypatch.setattr('app.routes.get_history', mock_get_history)

    response = client.post('/Coord', data={"question": "test"})
    data = response.get_data()

    assert data == results


def test_mock_all_function_and_returns_no_history(monkeypatch):
    results = b'{"address":"test adresse",' \
              b'"error":"no history",' \
              b'"latlng":{"lat":1,"lng":2},' \
              b'"place":"test_lieu"}\n'
    client = app.test_client()

    def mock_parser(text):
        return "test_lieu"

    monkeypatch.setattr('app.routes.function_parser', mock_parser)

    def mock_get_location(place):
        return {'location': {'lat': 1, 'lng': 2},
                'address': 'test adresse'}

    monkeypatch.setattr('app.routes.get_location', mock_get_location)

    def mock_get_pageid(lat, long):
        return 10

    monkeypatch.setattr('app.routes.get_pageid', mock_get_pageid)

    def mock_get_history(page_id):
        return False

    monkeypatch.setattr('app.routes.get_history', mock_get_history)

    response = client.post('/Coord', data={"question": "test"})
    data = response.get_data()

    assert data == results


def test_mock_all_function_and_returns_no_page_id(monkeypatch):
    results = b'{"address":"test adresse",' \
              b'"error":"no pageid",' \
              b'"latlng":{"lat":1,"lng":2},' \
              b'"place":"test_lieu"}\n'
    client = app.test_client()

    def mock_parser(text):
        return "test_lieu"

    monkeypatch.setattr('app.routes.function_parser', mock_parser)

    def mock_get_location(place):
        return {'location': {'lat': 1, 'lng': 2},
                'address': 'test adresse'}

    monkeypatch.setattr('app.routes.get_location', mock_get_location)

    def mock_get_pageid(lat, long):
        return False

    monkeypatch.setattr('app.routes.get_pageid', mock_get_pageid)

    response = client.post('/Coord', data={"question": "test"})
    data = response.get_data()

    assert data == results


def test_mock_all_function_and_returns_no_lat_long(monkeypatch):
    results = b'{"error":"no lat-lng","place":"test lieu"}\n'
    client = app.test_client()

    def mock_parser(text):
        return "test lieu"

    monkeypatch.setattr('app.routes.function_parser', mock_parser)

    def mock_get_location(place):
        return False

    monkeypatch.setattr('app.routes.get_location', mock_get_location)

    response = client.post('/Coord', data={"question": "test"})
    data = response.get_data()

    assert data == results


def test_mock_all_function_and_returns_no_place(monkeypatch):
    results = b'{"error":"no place"}\n'
    client = app.test_client()

    def mock_parser(value):
        return False

    monkeypatch.setattr('app.routes.function_parser', mock_parser)
    response = client.post('/Coord', data={"question": "test"})
    data = response.get_data()
    assert data == results


