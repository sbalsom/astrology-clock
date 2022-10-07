from flask import Flask
from datetime import datetime, timezone 
from frontend.astrology.planet_positions import PlanetPositions
from flask import render_template

app = Flask(__name__)

@app.route("/")
def render_current():


    current_utc = datetime.now(timezone.utc) # UTC time 
    # eventually I will have another input : UTC offset 
    pp = PlanetPositions(dt_utc=current_utc)
    return render_template('test.html', planets=pp.planet_positions())

@app.route("/json")
def current():
    current_utc = datetime.now(timezone.utc) # UTC time 
    print(current_utc)
    # eventually I will have another input : UTC offset 
    pp = PlanetPositions(dt_utc=current_utc)
    return pp.planet_positions()