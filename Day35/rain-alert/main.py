import requests

MY_LAT = 41.377289
MY_LONG = -71.827461

api_key = "not to be shared"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

print(data)