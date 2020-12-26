from app.parser.parser import function_parser


def test_q_complicated():
    quest = "Bonjour GrandPyBot est ce que tu aurais l'adresse de OpenClassrooms, pour mon devoir de Géographie?"
    response = function_parser(quest)
    assert response == "OpenClassrooms"


def test_q_easy():
    quest = "Salut Papy aurais-tu l'adresse de la Tour Eiffel?"
    response = function_parser(quest)
    assert response == "Tour Eiffel"


def test_q_more_complicated():
    quest = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, " \
            "pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
    response = function_parser(quest)
    assert response == "musée d'art d'histoire Fribourg"


def test_other_q_complicated():
    quest = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer " \
            "l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
    response = function_parser(quest)
    assert response == "tour eiffel"


def test_not_address_q():
    quest = "Salut papy!"
    response = function_parser(quest)
    assert response is False


def test_not_q():
    quest = "Donne moi l'adresse de la Tour Eiffel."
    response = function_parser(quest)
    assert response == "Tour Eiffel"


def test_just_place():
    quest = "OpenClassrooms"
    response = function_parser(quest)
    assert response is False


def test_just_address():
    quest = "adresse OpenClassrooms"
    response = function_parser(quest)
    assert response is False
