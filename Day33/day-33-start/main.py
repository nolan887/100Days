import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# iss_position = response.json()["iss_position"]
# print(iss_position)
#
# iss_lat = response.json()["iss_position"]["latitude"]
# print(iss_lat)
#
# iss_long = response.json()["iss_position"]["longitude"]
# iss_loc = (iss_lat, iss_long)
# print(iss_loc)




# Using sunrise-sunset API to Determine if the ISS will be visible (only visible at night)

MY_LATITUDE = 41.377289
MY_LONGITUDE = -71.827461

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunset = data["results"]["sunset"]
sunrise = data["results"]["sunrise"]

# print(sunrise)
# sunrise = sunrise.split("T")
# print(sunrise)
# sunrise = sunrise[1].split(":")
# print(sunrise)
# sunrise_hr = sunrise[0]
# print(sunrise_hr)
# sunrise_min = sunrise[1]
# print(sunrise_min)

# Above code block replaced with one single line as follows
sunset_hr = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise_hr = data["results"]["sunrise"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise_hr)
print(sunset_hr)
print(time_now.hour)