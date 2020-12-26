from app.wikipedia.wiki_api import get_pageid, get_history


def test_get_pageid_returns_correct_page_id(monkeypatch):
    results = 10

    class MockRequestsGet:
        def __init__(self, url, params):
            self.url = url
            self.params = params

        def json(self):
            return {
                'batchcomplete': '',
                'query': {
                    'geosearch': [
                        {'pageid': 10,
                         'ns': 0,
                         'title': 'Tour Eiffel',
                         'lat': 48.858296,
                         'lon': 2.294479, 'dist': 8.2,
                         'primary': ''},
                        {'pageid': 4641538,
                         'ns': 0,
                         'title': 'Le Jules Verne',
                         'lat': 48.85825,
                         'lon': 2.2945,
                         'dist': 13.4,
                         'primary': ''}]}}

    monkeypatch.setattr('app.wikipedia.wiki_api.requests.get', MockRequestsGet)
    assert get_pageid(48.85837009999999, 2.2944813) == results


def test_get_pageid_returns_false(monkeypatch):
    results = False

    class MockRequestsGet:
        def __init__(self, url, params):
            self.url = url
            self.params = params

        def json(self):
            return {
                'error': {
                    'code': 'invalid-coord',
                    'info': 'Invalid coordinate provided',
                    '*': 'See https://fr.wikipedia.org/w/api.php for API '
                         'usage. Subscribe to the mediawiki-api-announce '
                         'mailing list at &lt;https://lists.wikimedia.org/'
                         'mailman/listinfo/mediawiki-api-announce&gt; for '
                         'notice of API deprecations and breaking changes.'},
                'servedby': 'mw1377'}

    monkeypatch.setattr('app.wikipedia.wiki_api.requests.get', MockRequestsGet)
    assert get_pageid(48.85837009999999, 2.2944813) == results


def test_get_history_returns_correct_history(monkeypatch):
    results = 'test historique'

    class MockRequestsGet:
        def __init__(self, url, params):
            self.url = url
            self.params = params

        def json(self):
            return {'batchcomplete': '', 'query': {'pages': {'1359783': {
                'pageid': 1359783,
                'ns': 0,
                'title': 'Tour Eiffel',
                'extract': 'test historique',
                'contentmodel': 'wikitext',
                'pagelanguage': 'fr',
                'pagelanguagehtmlcode': 'fr',
                'pagelanguagedir': 'ltr',
                'touched': '2020-12-16T03:14:08Z',
                'lastrevid': 177684275,
                'length': 132316,
                'fullurl': 'https://fr.wikipedia.org/wiki/Tour_Eiffel',
                'editurl': 'https://fr.wikipedia.org/w/index.php?title='
                           'Tour_Eiffel&action=edit',
                'canonicalurl': 'https://fr.wikipedia.org/wiki/Tour_Eiffel'}}}}

    monkeypatch.setattr('app.wikipedia.wiki_api.requests.get', MockRequestsGet)
    assert get_history(1359783) == results


def test_get_history_returns_false(monkeypatch):
    results = False

    class MockRequestsGet:
        def __init__(self, url, params):
            self.url = url
            self.params = params

        def json(self):
            return {'batchcomplete': '', 'query': {'pages': {'1': {
                'pageid': 1,
                'missing': ''}}}}

    monkeypatch.setattr('app.wikipedia.wiki_api.requests.get', MockRequestsGet)
    assert get_history(1) == results
