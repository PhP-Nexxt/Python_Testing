from server import app
from test.conftest import client, mock_competitions, mock_clubs # import des data de test



def test_valid_process(mock_competitions, mock_clubs):
    # Test login user
    page_content = b"Welcome, jack@simplylift.co" # b = bytes
    data = {
        "email": "jack@simplylift.co" 
    }
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/showSummary", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data # Assertion verifie que le page_content se trouve dans response,data

    # Test Booking places and result
    page_content = "Great-booking complete!" # b = bytes
    data = {
        "club": "Simply Down",
        "competition": "Winter Festival",
        "places": "10",
    }
    
    competition = [c for c in mock_competitions if c['name'] == data['competition']][0]
    club = [c for c in mock_clubs if c['name'] == data['club']][0]
    competition_places_before_booking = int(competition["numberOfPlaces"]) # ici on recupere le nombre de place avant
    club_points_before_booking = int(club["points"])
    
    with app.test_client() as client: # post vers le route /showSummary
        response = client.post("/purchasePlaces", data = data)
        assert response.status_code == 200 # assertion le status code de la la reponse doit etre = à 200
        assert page_content in response.data.decode("utf-8") # Assertion verifie que le page_content se trouve dans response,data
        
        competition = [c for c in mock_competitions if c['name'] == data['competition']][0]
        club = [c for c in mock_clubs if c['name'] == data['club']][0]
        competition_places_after_booking = int(competition["numberOfPlaces"]) # ici on recupere le nombre de place apres
        club_points_after_booking = int(club["points"])
        
        assert competition_places_before_booking != competition_places_after_booking # Ici on verifie si les entier avant et apres sont differends 
        assert club_points_before_booking != club_points_after_booking
        assert competition_places_after_booking == competition_places_before_booking - int(data["places"]) # Ici on verifie que le nombre de place apres ets egale au nombre de places avant - le nombre de places reservées
        assert club_points_after_booking == club_points_before_booking - int(data["places"])
    
    