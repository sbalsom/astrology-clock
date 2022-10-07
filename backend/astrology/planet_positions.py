from datetime import datetime, timezone
import swisseph as swe
from backend.astrology.time_conversion import * 

PLANET_KEY = ('Sun',  # 0
              'Moon',  # 1
              'Mercury',  # 2
              'Venus',  # 3
              'Mars',  # 4
              'Jupiter',  # 5
              'Saturn'  # 6
              )

class PlanetPositions:

# TODO : Do instead of lat & long, use the offset passed from a dropdown
# for lat / long its probably actually better to have a drop down where the user selects their UTC offset 
# TODO : Its possible i should use ET (ephemeris time) instead of UT (universal time)
# TODO : Use my own bday for testing 
# here are some julian days examples : 
# converted UTC to Julian Day
# Ephemeris Time :2459856.871437315  this one is somehow a tiny bit later than UTC. only by like one minute 
#  Universal Time : 2459856.8406131254  this one is the UTC Julian day (what time it is in Britain ) 
# Without converting to UTC first, the julain day is (not sure if UT or ET) 
# 2459856.923611111 -- this one is the time in Berlin 
    def __init__(self, dt_utc: datetime):
        # set variables

        # timetuple = dt.timetuple()[:6]
        # self.utc_offset = get_utc_offset(*timetuple, lat, lon)

        # # get local bday
        # self.local_naive_bday = dt
        # self.local_aware_bday = naive_dt_to_aware(
        #     self.local_naive_bday, lat, lon)

        # # convert local to utc bday
        # self.utc_bday_tuple = swe.utc_time_zone(*timetuple, self.utc_offset)
        # # replace decimal seconds w 0
        # self.utc_bday = datetime(*self.utc_bday_tuple[:5], 0)
        # self.utc_aware_bday = self.utc_bday.replace(tzinfo=timezone.utc)

        julian_day_from_utc = utc_to_jd(dt_utc)
        # julian_day = dt_to_jd(dt)
        print(julian_day_from_utc)
        # print(julian_day)
        self.planet_degrees = [swe.calc(julian_day_from_utc[0], i, flags=0)[
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
