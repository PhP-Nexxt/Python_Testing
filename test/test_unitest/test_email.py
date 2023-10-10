from server import app
from test.conftest import client, mock_competitions, mock_clubs # import des data de test

def test_valid_email(mock_competitions, mock_clubs):
    page_content = b"Welcome, jack@simplylift.co" # b = bytes
    data = {
        "email": "jack@simplylift.co" 
    }
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/showSummary", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data # Assertion verifie que le page_content se trouve dans response,data


def test_invalid_email(mock_competitions, mock_clubs):
    page_content = b"e-mail does not exist"
    data = {
        "email": "jo@simplylift.co"
    }
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/showSummary", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data # Assertion verifie que le page_content se trouve dans response,data ici il sont differend

