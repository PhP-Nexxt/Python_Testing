import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST']) 
def showSummary():
    # ERROR 1
    # Verification si club existe si oui continue sinon message erreur
    club = [club for club in clubs if club['email'] == request.form['email']]
    # Error : add condition if list is empty
    if club:
        club = club[0]
        return render_template('welcome.html',club=club,competitions=competitions)
    else:
        return render_template('index.html',error_message="e-mail does not exist")


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    
    min_places = 1
    max_places = 12 if int(foundClub["points"]) > 12 else int(foundClub["points"]) # Ajout d'une double condition >12 si points du club > 12
    
    if foundClub and foundCompetition:
        competition_date = foundCompetition["date"] # recuperation date dans le json competition
        today = datetime.date.today() # recup date du jour
        competition_date = datetime.datetime.strptime(competition_date, "%Y-%m-%d %H:%M:%S").date() # Ici on convertit la date de competition en chaine de caractere
        # BUG 4*
        if competition_date >= today:
            return render_template('booking.html',club=foundClub,competition=foundCompetition, min_places=min_places, max_places=max_places) # Ajout des 2 variables de condition
        else:
            flash("You can't book places for a past competition")
    else:
        flash("Something went wrong-please try again")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    
    competition_date = competition["date"] # recuperation date dans le json competition
    today = datetime.date.today() # recup date du jour
    competition_date = datetime.datetime.strptime(competition_date, "%Y-%m-%d %H:%M:%S").date() # Ici on convertit la date de competition en chaine de caractere
    # BUG 4*
    if competition_date < today:
        flash("You cant book places for a past competition")
    # BUG 2
    elif int(club["points"])>= placesRequired:  # Ajout d'une condition vérifiant si les points du club sont suffisants
        # BUG 3
        if placesRequired > 12: # Ajout d'une condition vérifiant que le nombre de place est de 12 max
            flash("You cant book more than 12 places!")
        else:
            # BUG 5
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club["points"] = int(club["points"])-placesRequired # Ici on decompte les places (Bug 5)
            flash('Great-booking complete!')
    else:
        flash("damn you dont have enough points") # Message
        
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
# FEATURE 6
@app.route('/points')
def points():
    return render_template('points.html', clubs=clubs) # Ajout de la route pour le display (Feature 6)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))