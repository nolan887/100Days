import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

iss_position = response.json()["iss_position"]
print(iss_position)

iss_lat = response.json()["iss_position"]["latitude"]
print(iss_lat)

iss_long = response.json()["iss_position"]["longitude"]
iss_loc = (iss_lat, iss_long)
print(iss_loc)