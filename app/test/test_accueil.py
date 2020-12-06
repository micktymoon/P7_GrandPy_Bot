import requests
from bs4 import BeautifulSoup
from flask_testing import TestCase
import urllib3
from app import app


def test_accroche():
    url = "http://127.0.0.1:5000/accueil"
    result = requests.get(url)
    r_soup = BeautifulSoup(result.text, "html.parser")
    tag = r_soup.h1
    print(tag.string)
    assert tag.string == "GrandPyBot raconte moi une histoire!"


def test_accroche2():
    with app.test_client() as test_client:
        response = test_client.get("/accueil")
        result = response.data.decode("utf-8")
    r_soup = BeautifulSoup(result, "html.parser")
    tag = r_soup.h1
    assert tag.string == "GrandPyBot raconte moi une histoire!"


def test_accroche_urllib3():
    http = urllib3.PoolManager()
    url = "http://127.0.0.1:5000/accueil"
    result = http.request('GET', url)
    print(result.data)
    r_soup = BeautifulSoup(result.data, "html.parser")
    tag = r_soup.h1
    print(tag.string)


class TestViews(TestCase):

    def create_app(self):
        return app

    def test_2(self):
        flask_app = self.create_app()

        with flask_app.test_client() as test_client:
            response = test_client.get("/accueil")
            self.assertEqual(response.status_code, 200)
            print(response.data)