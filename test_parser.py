from parser import parser


def test_q_compliquee():
    quest = "Bonjour GrandPyBot est ce que tu aurais l'adresse de OpenClassrooms, pour mon devoir de Géographie?"
    response = parser(quest)
    assert response is not False


def test_q_simple():
    quest = "Salut Papy aurais-tu l'adresse de la Tour Eiffel?"
    response = parser(quest)
    assert response is not False


def test_pas_une_q():
    quest = "Salut papy!"
    response = parser(quest)
    assert response is False


def test_pas_une_q2():
    quest = "Donne moi l'adresse de la Tour Eiffel."
    response = parser(quest)
    assert response is not False


def test_juste_adresse():
    quest = "OpenClassrooms"
    response = parser(quest)
    assert response is False


def test_juste_adresse2():
    quest = "adresse de OpenClassrooms"
    response = parser(quest)
    assert response is False