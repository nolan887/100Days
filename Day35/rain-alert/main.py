import requests

# MY_LAT = 41.377289
# MY_LONG = -71.827461

# Werribee, Austraila currently raining
MY_LAT = 37.902900
MY_LONG = 144.658470

api_key = ""
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_ids = []
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
