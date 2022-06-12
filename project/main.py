import requests
import datetime as dt

APP_ID = "YOUR ID"
API_KEY = "YOUR KEY"

GENDER = "YOUR INFO"
WEIGHT_KG = "YOUR INFO"
HEIGHT_CM = "YOUR INFO"
AGE = "YOUR INFO"

day_time = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

print(now_time)


inp = input("Give me your exercise: ")


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/6ae4f3631e788968bd8434ffdba116e0/workoutTracking/workouts"


natural_lang_parameters = {
    "query": inp,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


resp = requests.post(nutritionix_endpoint,
                     json=natural_lang_parameters, headers=headers)

resp.raise_for_status()
result = resp.json()
print(result)


for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": day_time,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_params)

    print(sheet_response.text)
