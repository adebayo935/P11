import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime
import dateutil

def create_app(config):

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
    today = datetime.datetime.now()

    @app.template_filter('strftime')
    def _jinja2_filter_datetime(date, fmt=None):
        date = datetime.datetime.fromisoformat(date)
        return date

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        club = 0
        if request.form:
            for entry in clubs:
                if entry['email'] == request.form['email']:
                    club = entry
                    return render_template('welcome.html', today=today,club=club, clubs=clubs,competitions=competitions)
                else:
                    pass          
        if club == 0:
            flash("Wrong address please try again")
        return render_template('index.html')       
        


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        print(club)
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        if foundClub and foundCompetition:
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', today=today, clubs=clubs, club=club, competitions=competitions)


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])
        if placesRequired > 12 :
            flash('You can\'t book more than 12 places')
            return render_template('booking.html',club=club,competition=competition)
        elif (int(club['points'])-(placesRequired*3)) < 0 :
            flash('You don\'t have enough points to do that')
            return render_template('booking.html',club=club,competition=competition)
        else :
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club['points'] = int(club['points'])-(placesRequired*3)
            flash('Great-booking complete!')
        return render_template('welcome.html', today=today, clubs=clubs, club=club, competitions=competitions)


    # TODO: Add route for points display


    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app

