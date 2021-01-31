import requests
import os
import datetime as dt

# -------------------- SETUP CONSTANTS -------------------- #
USERNAME = "cloudbreak"
pixela_token = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": pixela_token
}

# -------------------- ACCOUNT CREATION PER API DOCUMENTATION -------------------- #
pixela_endpoint = "https://pixe.la/v1/users"
pixela_user_params = {
    "token": pixela_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_user_params)
# print(response.text)

# -------------------- GRAPH CREATION PER API -------------------- #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "float",
    "color": "momiji",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# -------------------- ADDING PIXELS -------------------- #
today = dt.datetime.now()

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? ")
}

# pixel_config_yesterday = {
#     "date": "20210129",
#     "quantity": "5"
# }

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# -------------------- MODIFYING PIXELS -------------------- #
update_endpoint = f"{pixel_endpoint}/20210129"
new_pixel_data = {
    "quantity": "7.5"
}

# request = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(request.text)

# -------------------- DELETING PIXELS -------------------- #
# response = requests.delete(url=f"{pixel_endpoint}/20200129", headers=headers)
# print(response.text)
