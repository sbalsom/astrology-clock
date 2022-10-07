from datetime import datetime, timezone
import swisseph as swe
from frontend.astrology.time_conversion import * 

PLANET_KEY = ('Sun',  # 0
              'Moon',  # 1
              'Mercury',  # 2
              'Venus',  # 3
              'Mars',  # 4
              'Jupiter',  # 5
              'Saturn'  # 6
              )

class PlanetPositions:

    def __init__(self, dt_utc: datetime, utc_offset: int = 0):

        dt_local = utc_to_local(dt_utc, utc_offset)
        jd_local = dt_to_jd(dt_local)

        self.planet_degrees = [swe.calc(jd_local, i, flags=0)[
            0][0] for i in range(7)]
        
        self.sun = self.planet_degrees[0]
        self.moon = self.planet_degrees[1]
        self.mercury = self.planet_degrees[2]
        self.venus = self.planet_degrees[3]
        self.mars = self.planet_degrees[4]
        self.jupiter = self.planet_degrees[5]
        self.saturn = self.planet_degrees[6]
        #  TODO : Add neptune
        
    def planet_positions(self):
        return {
            "moon": self.moon,
            "sun": self.sun,
            "mercury": self.mercury,
            "venus": self.venus,
            "mars": self.mars,
            "jupiter": self.jupiter,
            "saturn": self.saturn
        }
