import os
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth

GENDER = os.environ["GENDER"]
WEIGHT_KG = os.environ["WEIGHT_KG"]
HEIGHT_CM = os.environ["HEIGHT_CM"]
AGE = os.environ["AGE"]
sheet_endpoint = os.environ["SHEET"]
auth =os.environ["AUTH"]

APP_ID=os.environ["APP_ID"]
API_KEY=os.environ["API_KEY"]
username=os.environ["USERNAME"]
password = os.environ["PASSWORD"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# print(result)

sheet_response = requests.post(exercise_endpoint, json=parameters,auth=(username, password), headers=headers)

result = sheet_response.json()
print(result)

#today_date = datetime.now().strftime("%d%m%Y")
today_date = datetime.now().date()
now_time=datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": str(today_date),
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth = (username, password))
    print(sheet_response.text)