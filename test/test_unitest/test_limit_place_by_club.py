from server import app

def test_book_places_with_valid_points(mock_competitions, mock_clubs):
    page_content = "Great-booking complete!" # b = bytes
    data = {
        "club": "Iron cell",
        "competition": "Winter Festival",
        "places": "3",
    }
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/purchasePlaces", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data.decode("utf-8") # Assertion verifie que le page_content se trouve dans response,data
        # print(response.data.decode("utf-8"))
        
def test_book_places_with_more_points(mock_competitions, mock_clubs):
    page_content = "damn you dont have enough points" # b = bytes
    data = {
        "club": "Iron cell",
        "competition": "Winter Festival",
        "places": "6",
    }
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/purchasePlaces", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data.decode("utf-8") # Assertion verifie que le page_content se trouve dans response,data