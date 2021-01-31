import requests
import os
from datetime import datetime

# --------------- SETUP - CONSTANTS --------------- #
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_key = os.environ.get("NUTRITIONIX_KEY")
nutrition_app_id = os.environ.get("NUTRITIONIX_APP_ID")

headers = {
    "x-app-id": nutrition_app_id,
    "x-app-key": nutrition_key,
    "Content-Type": "application/json"
}

GENDER = "male"
WEIGHT = 78.47
HEIGHT = 182.88
today = datetime.now()
birthday = datetime(1987, 8, 30)
age_year_end = today.year - birthday.year
if birthday.month == today.month and birthday.day > today.day:
    age = age_year_end - 1
elif birthday.month > today.month:
    age = age_year_end - 1
else:
    age = age_year_end
MY_AGE = age

exercise_data = {
    "query": input("What excercise did you perform? (i.e: ran XX miles): "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": MY_AGE
}

response = requests.post(url=nutrition_endpoint, json=exercise_data, headers=headers)
print(response.text)