from tests.conftest import client

def test_should_showIndex(client):
    response = client.get('/')
    assert response.status_code == 200


def test_should_showSummary(client):
    response = client.post('/showSummary', data={'email':'john@simplylift.co'})
    assert response.status_code == 200


def test_should_book(client):

    competition = "Spring Festival"
    club = "Simply Lift"
    url = '/book/{}/{}'.format(competition,club)
    response = client.get(url)
    assert response.status_code == 200


