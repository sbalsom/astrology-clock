from datetime import datetime, timezone 
import swisseph as swe
import pytz
from timezonefinder import TimezoneFinder

tf = TimezoneFinder()

def get_current_utc():
    return datetime.now(timezone.utc)

def dt_to_jd(dt: datetime):
    timetuple = dt.timetuple()[:5]
    print(timetuple)
    minutes = timetuple[4]
    minute_fraction = minutes/60
    hour_fraction = timetuple[3] + minute_fraction 
    new_tuple = (timetuple[0],timetuple[1],timetuple[2],hour_fraction)
    print(new_tuple)
    return swe.julday(*new_tuple)

def utc_to_jd(dt_utc: datetime):
    timetuple = dt_utc.timetuple()[:6]
    return swe.utc_to_jd(*timetuple)

def get_utc_offset(y, mo, d, h, mi, s, lat, lon):
    naive = datetime(y, mo, d, h, mi, s)
    timezone = pytz.timezone(tf.timezone_at(lng=lon, lat=lat))
    aware = timezone.localize(naive)
    return aware.utcoffset().total_seconds() / 60 / 60

def naive_dt_to_aware(dt, lat, lon):
    timezone = pytz.timezone(tf.timezone_at(lng=lon, lat=lat))
    return dt.replace(tzinfo=timezone)