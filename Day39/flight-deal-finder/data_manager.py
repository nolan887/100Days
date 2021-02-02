import requests
import os

sheety_endpoint = "https://api.sheety.co/d3eeb7849c23a914bd8cf7c738fe696c/flightDeals/prices"
sheety_token = os.environ.get("SHEETY_TOKEN")

bearer_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint, headers=bearer_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
