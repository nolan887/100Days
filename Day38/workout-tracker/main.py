import requests
import os
from datetime import datetime

# --------------- API SETUP --------------- #
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_key = os.environ.get("NUTRITIONIX_KEY")
nutrition_app_id = os.environ.get("NUTRITIONIX_APP_ID")

headers = {
    "x-app-id": nutrition_app_id,
    "x-app-key": nutrition_key,
    "Content-Type": "application/json"
}

sheets_endpoint = "https://api.sheety.co/d3eeb7849c23a914bd8cf7c738fe696c/myWorkouts/workouts"
sheet_token = os.environ.get("SHEETY_TOKEN")

# --------------- DEFINING CONSTANTS --------------- #
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


# --------------- ASKING FOR USER INPUT AND PASSING TO NUTRITIONIX TO REQUEST WORKOUT DATA --------------- #
exercise_data = {
    "query": input("What excercise did you perform? (i.e: ran XX miles): "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": MY_AGE
}

workout_response = requests.post(url=nutrition_endpoint, json=exercise_data, headers=headers)
workout_details = workout_response.json()["exercises"]

# --------------- COMBINING WORKOUT DATA, DATE, AND TIME FOR PUSH TO SHEET --------------- #
today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")

for exercise in workout_details:
    sheet_inputs = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

bearer_headers = {
"Authorization": f"Bearer {sheet_token}"
}


sheet_response = requests.post(url=sheets_endpoint, json=sheet_inputs, headers=bearer_headers)
print(sheet_response.text)
