from flask import Flask
from datetime import datetime, timezone 
from backend.astrology.planet_positions import PlanetPositions

app = Flask('app')

@app.route("/")
def current():
    current_utc = datetime.now(timezone.utc) # UTC time 
    print(current_utc)
    # eventually I will have another input : UTC offset 
    pp = PlanetPositions(dt=current_time, dt_utc=current_utc)
    return pp.planet_positions()