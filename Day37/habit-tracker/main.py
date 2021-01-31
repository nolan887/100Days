import requests
import os
import datetime as dt

USERNAME = "cloudbreak"
pixela_token = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_user_params = {
    "token": pixela_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": pixela_token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = dt.datetime.now()

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)


