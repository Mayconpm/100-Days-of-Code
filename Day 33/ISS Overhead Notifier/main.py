import sched
import smtplib
import time
from datetime import datetime, timedelta

import requests
import yaml
from dateutil import tz

with open(r"Day 33\ISS Overhead Notifier\data.yml") as yaml_file:
    data = yaml.safe_load(yaml_file)

MY_EMAIL = data["email"]
MY_PASSWORD = data["password"]
RECEIVER_MAIL = data["receiver_mail"]
MY_LATITUDE = data["latitude"]
MY_LONGITUDE = data["longitude"]

scheduler = sched.scheduler(time.time, time.sleep)


def convert_to_datetime(date):
    to_zone = tz.gettz("Brazil/São Paulo")
    date_converted = datetime.fromisoformat(date)
    date_converted = date_converted.astimezone(to_zone)
    date_converted = date_converted.replace(tzinfo=None)
    return date_converted


def get_sunrise_sunset(time_now):
    date_time = time_now.strftime("%Y-%m-%d")
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
        "date": date_time,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = convert_to_datetime(data["results"]["sunrise"])
    sunset = convert_to_datetime(data["results"]["sunset"])

    return sunrise, sunset


def is_ISS_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude - MY_LATITUDE) <= 5 and (iss_longitude - MY_LONGITUDE) <= 5:
        return True
    else:
        return False


def is_night():
    time_now = datetime.now()
    time_tomorrow = time_now + timedelta(days=1)
    _, sunset = get_sunrise_sunset(time_now)
    sunrise, _ = get_sunrise_sunset(time_tomorrow)

    if time_now > sunset and time_now < sunrise:
        return True


time_now = datetime.now()


def ISS_notifier(scheduler):
    if is_night() and is_ISS_overhead():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_MAIL, msg="Look Up!")
            print("Email Sent.")
    scheduler.enter(60, 1, ISS_notifier, (scheduler,))


scheduler.enter(1, 1, ISS_notifier, (scheduler,))
scheduler.run()
