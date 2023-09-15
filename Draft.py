from datetime import datetime
from dateutil import tz
import requests

now = datetime.now()
date_time = now.strftime("%Y-%m-%d")

LATITUDE = -22.267908349563456
LONGITUDE = -42.532616977283155

parameters = {"lat": LATITUDE, "lng": LONGITUDE, "formatted": 0, "date": date_time}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

to_zone = tz.gettz("Brazil/São Paulo")

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise = datetime.fromisoformat(sunrise).astimezone(to_zone).replace(tzinfo=None)

sunset = datetime.fromisoformat(sunset).astimezone(to_zone).replace(tzinfo=None)
