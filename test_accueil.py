import requests
from bs4 import BeautifulSoup


def test_accroche():
    url = "http://127.0.0.1:5000/"
    result = requests.get(url)
    r_soup = BeautifulSoup(result.text, "html.parser")
    tag = r_soup.h1
    print(tag.string)
    assert tag.string == "GrandPyBot raconte moi une histoire!"

