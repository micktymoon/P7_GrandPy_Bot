import requests
from bs4 import BeautifulSoup
from flask_testing import LiveServerTestCase, TestCase
from flask import Flask
import urllib.request
import urllib3
from app.mon_app import *
import jsonify
# def test_accroche():
#     url = "http://127.0.0.1:5000/"
#     result = requests.get(url)
#     r_soup = BeautifulSoup(result.text, "html.parser")
#     tag = r_soup.h1
#     print(tag.string)
#     assert tag.string == "GrandPyBot raconte moi une histoire!"

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
        # port défaut est le 5000
        app.config['LIVESERVEUR_PORT'] = 0

        return app

    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_accroche(self):
        response = self

@app.route('/')
def some_jason():
    return jsonify(success=True)


class TestViews(TestCase):
    def test_some_json(self):
        response = self.client.get('/')
        self.assertEquals(response.json, dict(success=True))

