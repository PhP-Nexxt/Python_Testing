from server import app

def test_book_places_in_past_competition(mock_competitions, mock_clubs):
    page_content = "You cant book places for a past competition" 
    data = {
        "club": "Simply Down",
        "competition": "Down Classic",
        "places": "10",
    }
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/purchasePlaces", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data.decode("utf-8") # Assertion verifie que le page_content se trouve dans response,data
        
