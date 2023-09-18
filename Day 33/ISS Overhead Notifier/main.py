# Import the necessary library
import sched
import smtplib
import time
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    """
    This function converts an ISO formatted date string to a datetime object
    with the datetime set to the 'Brazil/São Paulo' timezone.

    Parameters:
    date (str): The date in ISO format (YYYY-MM-DD)

    Returns:
    date_converted (datetime.datetime): The date converted to a datetime object with the Sao Paulo timezone.
    Note that timezone information is removed from the final return.
    """
    # Define the timezone you want to convert to
    to_zone = tz.gettz("Brazil/São Paulo")

    # Convert the input date to a datetime object
    date_converted = datetime.fromisoformat(date)

    # Convert the datetime object to the desired timezone
    date_converted = date_converted.astimezone(to_zone)

    # Remove the timezone information from the datetime object
    date_converted = date_converted.replace(tzinfo=None)

    # Return the converted date
    return date_converted


def get_sunrise_sunset(time_now):
    """Get the sunrise and sunset times for a given date and location.

    Args:
        time_now (datetime): The current date and time.

    Returns:
        tuple: A tuple containing the sunrise and sunset times as datetime objects.

    Raises:
        HTTPError: If there is an error in the HTTP request to the API.
    """

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
    """Check if the International Space Station (ISS) is overhead.

    Returns:
        bool: True if the ISS is overhead within a 5 degree latitude and longitude range from MY_LATITUDE and
        MY_LONGITUDE, False otherwise.
    """

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - MY_LATITUDE) <= 1 and abs(iss_longitude - MY_LONGITUDE) <= 1:
        return True
    else:
        return False


def is_night():
    """Check if it is currently night time.

    Returns:
        bool: True if it is currently night time, False otherwise.
    """

    time_now = datetime.now()
    time_tomorrow = time_now + timedelta(days=1)
    _, sunset = get_sunrise_sunset(time_now)
    sunrise, _ = get_sunrise_sunset(time_tomorrow)

    if time_now > sunset and time_now < sunrise:
        return True


def ISS_notifier(scheduler):
    """This function sends an email notification if the International Space Station (ISS) is overhead during the night.
    The function checks if it is night time and if the ISS is overhead.
    If both conditions are met, it sends an email notification.

    Args:
        scheduler (scheduler): The scheduler object used to schedule the function to run periodically.

    Returns:
        None

    Raises:
        None

    """

    # The function checks if it is night time and the ISS is overhead
    # time_now = datetime.now()
    if is_night() and is_ISS_overhead():
        # If both conditions are met, it prepares an email.
        msg = MIMEMultipart()
        msg["From"] = MY_EMAIL
        msg["To"] = RECEIVER_MAIL
        msg["Subject"] = "ISS Overhead"
        body = "Look Up!"
        msg.attach(MIMEText(body, "plain"))
        text = msg.as_string()

        # The function sends the email using a connection to an SMTP server.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_MAIL, msg=text)
            print("Email Sent.")

    # The function is scheduled to run every 60 seconds
    scheduler.enter(60, 1, ISS_notifier, (scheduler,))


try:
    scheduler.enter(30, 1, ISS_notifier, (scheduler,))
    scheduler.run()
except Exception as exc:
    print(f"An error occurred: {exc}")
