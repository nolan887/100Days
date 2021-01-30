import requests
import os
from twilio.rest import Client

MY_LAT = 41.377289
MY_LONG = -71.827461

# Openweather Info
api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# Twilio Info
account_sid = "AC96f51ba9845b52998cf4d9fdc593f577"
auth_token = os.environ.get("AUTH_TOKEN")

need_umbrella = False

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# slices weather through 13-1 (12 hours)
weather_slice = weather_data["hourly"][:13]

for upcoming_hour in weather_slice:
    condition_code = upcoming_hour["weather"][0]["id"]
    if int(condition_code) < 700:
        need_umbrella = True

if need_umbrella:
    print("It's going to rain, bring an umbrella!")

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, bring an umbrella! ☔️",
        from_='+16692013335',
        to='+14016225183'
    )

    print(message.sid)
