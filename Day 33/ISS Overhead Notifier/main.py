import smtplib
import time
from datetime import datetime

import requests
import yaml
from dateutil import tz

with open("Day 33\ISS Overhead Notifier\data.yml") as yaml_file:
    data = yaml.safe_load(yaml_file)

MY_EMAIL = data["email"]
MY_PASSWORD = data["password"]
LATITUDE = data["latitude"]
LONGITUDE = data["longitude"]


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if LATITUDE - 5 <= iss_latitude <= LATITUDE + 5 and LONGITUDE - 5 <= iss_longitude <= LONGITUDE + 5:
        return True


def is_night():
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d")
    parameters = {"lat": LATITUDE, "lng": LONGITUDE, "formatted": 0, "date": date_time}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = convert_to_datetime(data["results"]["sunrise"])
    sunset = convert_to_datetime(data["results"]["sunset"])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


def convert_to_datetime(date):
    to_zone = tz.gettz("Brazil/São Paulo")
    date_converted = datetime.fromisoformat(date)
    date_converted = date_converted.astimezone(to_zone)
    date_converted = date_converted.replace(tzinfo=None)
    return date_converted


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
