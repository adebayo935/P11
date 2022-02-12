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


def test_should_purchasePlaces(client):

    placesRequired = 9
    competition = "Spring Festival"
    club = "Simply Lift"
    response = client.post('/purchasePlaces', data={"competition":competition,"club":club,"places":placesRequired})
    assert response.status_code == 200

def test_should_not_purchasePlaces_toomuch(client):

    placesRequired = 13
    competition = "Spring Festival"
    club = "Simply Lift"
    error = 'You can&#39;t book more than 12 places'
    response = client.post('/purchasePlaces', data={"competition":competition,"club":club,"places":placesRequired})
    data = response.data.decode()
    assert error in data


def test_should_not_purchasePlaces_notenough(client):

    placesRequired = 9
    competition = "Spring Festival"
    club = "Simply Lift"
    error = 'You don&#39;t have enough points to do that'
    response = client.post('/purchasePlaces', data={"competition":competition,"club":club,"places":placesRequired})
    data = response.data.decode()
    assert error in data