from bs4 import BeautifulSoup
from flask_testing import TestCase
from app.routes import app


def test_catchphrase_presence():
    with app.test_client() as test_client:
        response = test_client.get("/accueil")
        result = response.data.decode("utf-8")
    r_soup = BeautifulSoup(result, "html.parser")
    tag = r_soup.h1
    assert tag.string == "GrandPyBot raconte moi une histoire!"


def test_2():
    with app.test_client() as test_client:
        response = test_client.get("/accueil")
        assert response.status_code == 200
