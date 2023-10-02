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
    if int(club["points"])>= placesRequired:  # Ajout d'une condition vérifiant si les points du club sont suffisants
        if placesRequired > 12: # Ajout d'une condition vérifiant que le nombre de place est de 12 max
            flash("You can't book more than 12 places !")
        else:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club["points"] = int(club["points"])-placesRequired # Ici on decompte les places (Bug 5)
            flash('Great-booking complete!')
    else:
        flash("damn you don't have enough points")
        
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))