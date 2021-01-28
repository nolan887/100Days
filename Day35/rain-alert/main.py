import requests

MY_LAT = 41.377289
MY_LONG = -71.827461

api_key = "c653eb49332fe60957ba3f8f37be99e5"



response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&appid={api_key}")
response.raise_for_status()
data = response.json()

print(data)