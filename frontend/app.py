from flask import Flask
from datetime import datetime, timezone 
from frontend.astrology.planet_positions import PlanetPositions
from flask import render_template

app = Flask(__name__)

@app.route("/")
def render_chart():
    return render_template('chart.html')

@app.route("/chart.json")
def current():
    current_utc = datetime.now(timezone.utc) # UTC time 
    # TODO : eventually I will have another input : UTC offset 
    pp = PlanetPositions(dt_utc=current_utc)
    return pp.planet_positions()