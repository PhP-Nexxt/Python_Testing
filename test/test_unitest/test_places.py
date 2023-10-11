from server import app

def test_book_places_less_12(mock_competitions, mock_clubs):
    page_content = "Great-booking complete!" # b = bytes
    data = {
        "club": "Simply Down",
        "competition": "Winter Festival",
        "places": "10",
    }
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/purchasePlaces", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data.decode("utf-8") # Assertion verifie que le page_content se trouve dans response,data
        # print(response.data.decode("utf-8"))
        
def test_book_places_more_12(mock_competitions, mock_clubs):
    page_content = "You cant book more than 12 places!" # b = bytes
    data = {
        "club": "Simply Down",
        "competition": "Winter Festival",
        "places": "13",
    }
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/purchasePlaces", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data.decode("utf-8") # Assertion verifie que le page_content se trouve dans response,data
    