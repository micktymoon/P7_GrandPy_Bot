import requests
from bs4 import BeautifulSoup
from flask_testing import LiveServerTestCase, TestCase
from flask import Flask
import urllib.request
import urllib3
from app.mon_app import app


def test_accroche():
    url = "http://127.0.0.1:5000/"
    result = requests.get(url)
    r_soup = BeautifulSoup(result.text, "html.parser")
    tag = r_soup.h1
    print(tag.string)
    assert tag.string == "GrandPyBot raconte moi une histoire!"


def test_accroche2():
    with app.test_client() as test_client:
        response = test_client.get("/")
        result = response.data.decode("utf-8")
    r_soup = BeautifulSoup(result, "html.parser")
    tag = r_soup.h1
    assert tag.string == "GrandPyBot raconte moi une histoire!"


def test_accroche_urllib3():
    http = urllib3.PoolManager()
    url = "http://127.0.0.1:5000/"
    result = http.request('GET', url)
    print(result.data)
    r_soup = BeautifulSoup(result.data, "html.parser")
    tag = r_soup.h1
    print(tag.string)


class MyTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        # app.config['LIVESERVER_PORT'] = 8943
        # POURQUOI QUAND J'ENLEVE LA LIGNE DU DESSUS ÇA MARCHE MAIS PAS QUAND JE LA MET????????
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)






class TestViews(TestCase):

    def create_app(self):
        return app

    def test_2(self):
        flask_app = self.create_app()

        with flask_app.test_client() as test_client:
            response = test_client.get("/")
            self.assertEqual(response.status_code, 200)
            print(response.data)