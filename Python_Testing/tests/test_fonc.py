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