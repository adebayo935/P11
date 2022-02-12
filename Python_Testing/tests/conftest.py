import pytest

from server import create_app


@pytest.fixture
def client():
    server = create_app({"TESTING": True})
    with server.test_client() as client:
        yield client


@pytest.fixture
def club():
    club = {   
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    }

@pytest.fixture
def competitions():
    competitions = {"name": "Spring Festival",
            "date": "2023-03-27 10:00:00",
            "numberOfPlaces": "25"}