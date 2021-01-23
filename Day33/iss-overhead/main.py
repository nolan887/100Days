import requests
from datetime import datetime
import time

MY_LAT = 41.377289
MY_LONG = -71.827461

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hr = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hr = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now < sunrise_hr or time_now > sunset_hr:
        return True
    return False


while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        print("Its a bird... its a plane... its... THE INTERNATIONAL SPACE STATION!")
    else:
        print("No ISS, bummer.")



