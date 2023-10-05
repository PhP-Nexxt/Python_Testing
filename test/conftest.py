import pytest
from server import app

@pytest.fixture #Fichiers de test 
def client(): # Cette fonction indique au server que nous sommes en mode test
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_competitions(mocker): # permet de modifier la valeur de la competition dans le fichier server
    competitions =  [
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
    mocker.patch("server.competitons", competitions)
    return competitions
    
@pytest.fixture
def mock_clubs(mocker):
    clubs = [
        {
            "name":"Simply Lift",
            "email":"john@simplylift.co",
            "points":"13"
        },
        {
            "name":"Iron Temple",
            "email": "admin@irontemple.com",
            "points":"4"
        },
        {   "name":"She Lifts",
            "email": "kate@shelifts.co.uk",
            "points":"12"
        }
    ]
    mocker.patch("server.clubs", clubs)
    return clubs
    