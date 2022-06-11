import requests

APP_ID = "YOUR ID"
API_KEY = "YOUR KEY"

GENDER = "YOUR INFO"
WEIGHT_KG = "YOUR INFO"
HEIGHT_CM = "YOUR INFO"
AGE = "YOUR INFO"

inp = input("Give me your exercise: ")


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
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
