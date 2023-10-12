from server import app

def test_point_board(mock_competitions, mock_clubs):
    
    with app.test_client() as client: # post vers le route /showSummary
        response = client.get("/points")
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200