from datetime import datetime, timezone 
import swisseph as swe
import pytz
from timezonefinder import TimezoneFinder

tf = TimezoneFinder()

def get_current_utc():
    return datetime.now(timezone.utc)

def dt_to_jd(dt: datetime):
    timetuple = dt.timetuple()[:6]
    return swe.utc_to_jd(*timetuple)[1]

def utc_to_local(dt_utc: datetime, utc_offset):
    # convert UTC to local time 
    timetuple = dt_utc.timetuple()[:6]
    local = swe.utc_time_zone(*timetuple, -utc_offset) # reversing the offset converts UTC back to local
    # round decimal seconds
    dt_local = datetime(*local[:5], round(local[5]))
    return dt_local