# TODO: Get 10 new questions every time the program is run and populate question_data

import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
