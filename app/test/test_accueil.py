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


def test_page_coord_status_code_is_ok():
    with app.test_client() as test_client:
        response = test_client.get("/accueil")
        assert response.status_code == 200


def test_mock_parser_correct(monkeypatch):
    results = b'{"address":"10 Quai de la Charente, 75019 Paris, France",' \
              b'"history":"Le quai de la Gironde est un quai situ\\u00e9 ' \
              b'le long du canal Saint-Denis, \\u00e0 Paris, dans le 19e ' \
              b'arrondissement.\\n\\n\\n== Situation et acc\\u00e8s ==\\nIl' \
              b' fait face au quai de la Charente, commence au quai de ' \
              b'l\'Oise et se termine avenue Corentin-Cariou.\\nLa ligne ' \
              b'\\u2009 du tramway passe sur ce quai.\\n\\n\\n== Origine du ' \
              b'nom ==\\nLe quai porte le nom que prend le fleuve, la ' \
              b'Garonne, apr\\u00e8s avoir re\\u00e7u la Dordogne au bec ' \
              b'd\'Amb\\u00e8s.\\n\\n\\n== Historique ==\\nCette voie de ' \
              b'l\'ancienne commune de La Villette a \\u00e9t\\u00e9 ' \
              b'class\\u00e9e dans la voirie de Paris par un d\\u00e9cret ' \
              b'du 23 mai 1863 et porte son nom actuel depuis un ' \
              b'arr\\u00eat\\u00e9 du 11 juin 1873.\\n\\n\\n== ' \
              b'B\\u00e2timents remarquables et lieux de m\\u00e9moire ' \
              b'==\\nno 11 : emplacement des Entrep\\u00f4ts ' \
              b'g\\u00e9n\\u00e9raux.\\n\\n\\n== Voir aussi ==\\n\\n\\n=== ' \
              b'Articles connexes ===\\nListe des voies du 19e ' \
              b'arrondissement de Paris\\nListe des voies de ' \
              b'Paris\\n\\n\\n=== Navigation ===\\n Portail de Paris   ' \
              b'Portail de la route\\u2026","latlng":' \
              b'{"lat":48.8975156,"lng":2.3833993},"place":"OpenClassrooms"}\n'
    client = app.test_client()

    def mock_parser():
        return "OpenClassrooms"

    monkeypatch.setattr('app.parser.parser.parser', mock_parser())
    response = client.post('/Coord', data={"question": "Donne moi l'adresse de OpenClassrooms"})
    data = response.get_data()
    assert data == results


def test_mock_parser_false(monkeypatch):
    results = b'{"error":"no place"}\n'
    client = app.test_client()

    def mock_parser():
        return False

    monkeypatch.setattr('app.parser.parser.parser', mock_parser())
    response = client.post('/Coord', data={"question": "Donne moi OpenClassrooms"})
    data = response.get_data()
    assert data == results


def test_mock_get_location_correct(monkeypatch):
    results = b'{"address":"10 Quai de la Charente, 75019 Paris, France",' \
              b'"history":"Le quai de la Gironde est un quai situ\\u00e9 ' \
              b'le long du canal Saint-Denis, \\u00e0 Paris, dans le 19e ' \
              b'arrondissement.\\n\\n\\n== Situation et acc\\u00e8s ==\\nIl' \
              b' fait face au quai de la Charente, commence au quai de ' \
              b'l\'Oise et se termine avenue Corentin-Cariou.\\nLa ligne ' \
              b'\\u2009 du tramway passe sur ce quai.\\n\\n\\n== Origine du ' \
              b'nom ==\\nLe quai porte le nom que prend le fleuve, la ' \
              b'Garonne, apr\\u00e8s avoir re\\u00e7u la Dordogne au bec ' \
              b'd\'Amb\\u00e8s.\\n\\n\\n== Historique ==\\nCette voie de ' \
              b'l\'ancienne commune de La Villette a \\u00e9t\\u00e9 ' \
              b'class\\u00e9e dans la voirie de Paris par un d\\u00e9cret ' \
              b'du 23 mai 1863 et porte son nom actuel depuis un ' \
              b'arr\\u00eat\\u00e9 du 11 juin 1873.\\n\\n\\n== ' \
              b'B\\u00e2timents remarquables et lieux de m\\u00e9moire ' \
              b'==\\nno 11 : emplacement des Entrep\\u00f4ts ' \
              b'g\\u00e9n\\u00e9raux.\\n\\n\\n== Voir aussi ==\\n\\n\\n=== ' \
              b'Articles connexes ===\\nListe des voies du 19e ' \
              b'arrondissement de Paris\\nListe des voies de ' \
              b'Paris\\n\\n\\n=== Navigation ===\\n Portail de Paris   ' \
              b'Portail de la route\\u2026","latlng":' \
              b'{"lat":48.8975156,"lng":2.3833993},"place":"OpenClassrooms"}\n'
    client = app.test_client()

    def mock_get_location():
        return {'location': {'lat': 48.8975156, 'lng': 2.3833993},
                'address': '10 Quai de la Charente, 75019 Paris, France'}

    monkeypatch.setattr('app.maps.maps_api.get_location', mock_get_location())
    response = client.post('/Coord', data={"question": "Donne moi l'adresse de OpenClassrooms"})
    data = response.get_data()
    assert data == results


def test_mock_get_location_false(monkeypatch):
    results = b'{"error":"no lat-lng","place":":"}\n'
    client = app.test_client()

    def mock_get_location():
        return False

    monkeypatch.setattr('app.maps.maps_api.get_location', mock_get_location())
    response = client.post('/Coord', data={"question": "Donne moi l'adresse de :"})
    data = response.get_data()
    assert data == results


def test_mock_get_pageid_correct(monkeypatch):
    results = b'{"address":"10 Quai de la Charente, 75019 Paris, France",' \
              b'"history":"Le quai de la Gironde est un quai situ\\u00e9 ' \
              b'le long du canal Saint-Denis, \\u00e0 Paris, dans le 19e ' \
              b'arrondissement.\\n\\n\\n== Situation et acc\\u00e8s ==\\nIl' \
              b' fait face au quai de la Charente, commence au quai de ' \
              b'l\'Oise et se termine avenue Corentin-Cariou.\\nLa ligne ' \
              b'\\u2009 du tramway passe sur ce quai.\\n\\n\\n== Origine du ' \
              b'nom ==\\nLe quai porte le nom que prend le fleuve, la ' \
              b'Garonne, apr\\u00e8s avoir re\\u00e7u la Dordogne au bec ' \
              b'd\'Amb\\u00e8s.\\n\\n\\n== Historique ==\\nCette voie de ' \
              b'l\'ancienne commune de La Villette a \\u00e9t\\u00e9 ' \
              b'class\\u00e9e dans la voirie de Paris par un d\\u00e9cret ' \
              b'du 23 mai 1863 et porte son nom actuel depuis un ' \
              b'arr\\u00eat\\u00e9 du 11 juin 1873.\\n\\n\\n== ' \
              b'B\\u00e2timents remarquables et lieux de m\\u00e9moire ' \
              b'==\\nno 11 : emplacement des Entrep\\u00f4ts ' \
              b'g\\u00e9n\\u00e9raux.\\n\\n\\n== Voir aussi ==\\n\\n\\n=== ' \
              b'Articles connexes ===\\nListe des voies du 19e ' \
              b'arrondissement de Paris\\nListe des voies de ' \
              b'Paris\\n\\n\\n=== Navigation ===\\n Portail de Paris   ' \
              b'Portail de la route\\u2026","latlng":' \
              b'{"lat":48.8975156,"lng":2.3833993},"place":"OpenClassrooms"}\n'
    client = app.test_client()

    def mock_get_pageid():
        return 3120649

    monkeypatch.setattr('app.wikipedia.wiki_api.get_pageid', mock_get_pageid())
    response = client.post('/Coord', data={"question": "Donne moi l'adresse de OpenClassrooms"})
    data = response.get_data()
    assert data == results


def test_mock_get_pageid_false(monkeypatch):
    results = b'{"address":"1189 Virginia Ave NE, Atlanta, GA 30306, USA",' \
              b'"error":"no pageid",' \
              b'"latlng":{"lat":33.77986,"lng":-84.349153},' \
              b'"place":"blabla"}\n'
    client = app.test_client()

    def mock_get_pageid():
        return False

    monkeypatch.setattr('app.wikipedia.wiki_api.get_pageid', mock_get_pageid())
    response = client.post('/Coord', data={"question": "Donne moi l'adresse de blabla"})
    data = response.get_data()
    assert data == results


def test_mock_get_history_correct(monkeypatch):
    results = b'{"address":"10 Quai de la Charente, 75019 Paris, France",' \
              b'"history":"Le quai de la Gironde est un quai situ\\u00e9 ' \
              b'le long du canal Saint-Denis, \\u00e0 Paris, dans le 19e ' \
              b'arrondissement.\\n\\n\\n== Situation et acc\\u00e8s ==\\nIl' \
              b' fait face au quai de la Charente, commence au quai de ' \
              b'l\'Oise et se termine avenue Corentin-Cariou.\\nLa ligne ' \
              b'\\u2009 du tramway passe sur ce quai.\\n\\n\\n== Origine du ' \
              b'nom ==\\nLe quai porte le nom que prend le fleuve, la ' \
              b'Garonne, apr\\u00e8s avoir re\\u00e7u la Dordogne au bec ' \
              b'd\'Amb\\u00e8s.\\n\\n\\n== Historique ==\\nCette voie de ' \
              b'l\'ancienne commune de La Villette a \\u00e9t\\u00e9 ' \
              b'class\\u00e9e dans la voirie de Paris par un d\\u00e9cret ' \
              b'du 23 mai 1863 et porte son nom actuel depuis un ' \
              b'arr\\u00eat\\u00e9 du 11 juin 1873.\\n\\n\\n== ' \
              b'B\\u00e2timents remarquables et lieux de m\\u00e9moire ' \
              b'==\\nno 11 : emplacement des Entrep\\u00f4ts ' \
              b'g\\u00e9n\\u00e9raux.\\n\\n\\n== Voir aussi ==\\n\\n\\n=== ' \
              b'Articles connexes ===\\nListe des voies du 19e ' \
              b'arrondissement de Paris\\nListe des voies de ' \
              b'Paris\\n\\n\\n=== Navigation ===\\n Portail de Paris   ' \
              b'Portail de la route\\u2026","latlng":' \
              b'{"lat":48.8975156,"lng":2.3833993},"place":"OpenClassrooms"}\n'
    client = app.test_client()

    def mock_get_history():
        return False

    monkeypatch.setattr('app.wikipedia.wiki_api.get_history', mock_get_history())
    response = client.post('/Coord', data={"question": "Donne moi l'adresse de OpenClassrooms"})
    data = response.get_data()
    assert data == results


def test_mock_get_history_false(monkeypatch):
    # Normally, it is impossible to have no history if a Wikipedia page exists.
    # So the error returned is 'no pageid' because I cannot find an example to return the error 'no history'
    results = b'{"address":"4 N Santa Fe Ave, Tulsa, OK 74127, USA",' \
              b'"error":"no pageid",' \
              b'"latlng":{"lat":36.1541709,"lng":-96.009076},' \
              b'"place":"error"}\n'

    client = app.test_client()

    def mock_get_history():
        return False

    monkeypatch.setattr('app.wikipedia.wiki_api.get_history', mock_get_history())
    response = client.post('/Coord', data={"question": "Donne moi l'adresse de error"})
    data = response.get_data()
    assert data == results


def test_mock_parser_and_get_location_pageid_history(monkeypatch):
    results = b'{"address":"10 Quai de la Charente, 75019 Paris, France",' \
              b'"history":"Le quai de la Gironde est un quai situ\\u00e9 ' \
              b'le long du canal Saint-Denis, \\u00e0 Paris, dans le 19e ' \
              b'arrondissement.\\n\\n\\n== Situation et acc\\u00e8s ==\\nIl' \
              b' fait face au quai de la Charente, commence au quai de ' \
              b'l\'Oise et se termine avenue Corentin-Cariou.\\nLa ligne ' \
              b'\\u2009 du tramway passe sur ce quai.\\n\\n\\n== Origine du ' \
              b'nom ==\\nLe quai porte le nom que prend le fleuve, la ' \
              b'Garonne, apr\\u00e8s avoir re\\u00e7u la Dordogne au bec ' \
              b'd\'Amb\\u00e8s.\\n\\n\\n== Historique ==\\nCette voie de ' \
              b'l\'ancienne commune de La Villette a \\u00e9t\\u00e9 ' \
              b'class\\u00e9e dans la voirie de Paris par un d\\u00e9cret ' \
              b'du 23 mai 1863 et porte son nom actuel depuis un ' \
              b'arr\\u00eat\\u00e9 du 11 juin 1873.\\n\\n\\n== ' \
              b'B\\u00e2timents remarquables et lieux de m\\u00e9moire ' \
              b'==\\nno 11 : emplacement des Entrep\\u00f4ts ' \
              b'g\\u00e9n\\u00e9raux.\\n\\n\\n== Voir aussi ==\\n\\n\\n=== ' \
              b'Articles connexes ===\\nListe des voies du 19e ' \
              b'arrondissement de Paris\\nListe des voies de ' \
              b'Paris\\n\\n\\n=== Navigation ===\\n Portail de Paris   ' \
              b'Portail de la route\\u2026","latlng":' \
              b'{"lat":48.8975156,"lng":2.3833993},"place":"OpenClassrooms"}\n'
    client = app.test_client()

    def mock_parser():
        return "OpenClassrooms"

    monkeypatch.setattr('app.parser.parser.parser', mock_parser())

    def mock_get_location():
        return {'location': {'lat': 48.8975156, 'lng': 2.3833993},
                'address': '10 Quai de la Charente, 75019 Paris, France'}

    monkeypatch.setattr('app.maps.maps_api.get_location', mock_get_location())

    def mock_get_pageid():
        return 3120649

    monkeypatch.setattr('app.wikipedia.wiki_api.get_pageid', mock_get_pageid())

    def mock_get_history():
        return "Le quai de la Gironde est un quai situé le long du canal " \
               "Saint-Denis, à Paris, dans le 19e arrondissement." \
               "\n\n\n== Situation et accès ==\nIl fait face au quai de la " \
               "Charente, commence au quai de l'Oise et se termine avenue " \
               "Corentin-Cariou.\nLa ligne \u2009 du tramway passe sur ce " \
               "quai.\n\n\n== Origine du nom ==\nLe quai porte le nom que " \
               "prend le fleuve, la Garonne, après avoir reçu la Dordogne " \
               "au bec d'Ambès.\n\n\n== Historique ==\nCette voie de " \
               "l'ancienne commune de La Villette a été classée dans la " \
               "voirie de Paris par un décret du 23 mai 1863 et porte son " \
               "nom actuel depuis un arrêté du 11 juin 1873.\n\n\n== " \
               "Bâtiments remarquables et lieux de mémoire ==\nno 11 : " \
               "emplacement des Entrepôts généraux.\n\n\n== Voir aussi " \
               "==\n\n\n=== Articles connexes ===\nListe des voies du 19e " \
               "arrondissement de Paris\nListe des voies de Paris\n\n\n=== " \
               "Navigation ===\n Portail de Paris   Portail de la route…"

    monkeypatch.setattr('app.wikipedia.wiki_api.get_history', mock_get_history())

    response = client.post('/Coord', data={"question": "Donne moi l'adresse de OpenClassrooms"})
    data = response.get_data()

    assert data == results

