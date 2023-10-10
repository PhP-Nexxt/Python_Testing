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
            "name": "Winter Festival", # modif des coordonnées pour le test
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Down Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
    mocker.patch("server.competitions", competitions)
    return competitions
    
@pytest.fixture
def mock_clubs(mocker):
    clubs = [
        {
            "name":"Simply Down",
            "email":"jack@simplylift.co",
            "points":"13"
        },
        {
            "name":"Iron cell",
            "email": "info@irontemple.com",
            "points":"4"
        },
        {   "name":"She raise",
            "email": "katya@shelifts.co.uk",
            "points":"12"
        }
    ]
    mocker.patch("server.clubs", clubs)
    return clubs
    