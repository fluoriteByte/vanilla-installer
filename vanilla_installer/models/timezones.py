import datetime
import pytz

from gi.repository import GnomeDesktop, GWeather


# TODO: port to a dedicated class
all_timezones = {}
cleanup_rules = [
    "etc",
    "gmt",
]

for timezone in GWeather.Location.get_world().get_timezones():
    _timezone = timezone.get_identifier()

    if len(_timezone.split("/")) < 2:
        continue

    _country = _timezone.split('/')[0]
    _city = _timezone[_country.__len__()+1:]

    if _country.lower() in cleanup_rules:
        continue

    if _country not in all_timezones:
        all_timezones[_country] = []

    all_timezones[_country].append(_city)

all_timezones = dict(sorted(all_timezones.items()))

for country in all_timezones.keys():
    all_timezones[country] = sorted(all_timezones[country])

def get_current_timezone():
    timezone = GnomeDesktop.WallClock().get_timezone()
    timezone = timezone.get_identifier()

    country = timezone.split('/')[0]
    city = timezone[country.__len__()+1:]

    return country, city
    
def get_preview_timezone(country, city):
    timezone = pytz.timezone(f"{country}/{city}")
    now = datetime.datetime.now(timezone)

    return now.strftime("%H:%M"), now.strftime("%A, %d %B %Y")

