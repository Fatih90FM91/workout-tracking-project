import requests, os
from datetime import datetime
from requests.auth import HTTPBasicAuth


APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

USER_NAME = os.environ.get('USER_NAME')
PASSWORD = os.environ.get('PASSWORD')

basic = HTTPBasicAuth(USER_NAME, PASSWORD)

current_day = datetime.now()
DATE = current_day.strftime('%d/%m/%Y')
print(DATE)

TIME= current_day.strftime('%H:%M:%S')
print(TIME)
#https://api.sheety.co/username/projectName/sheetName

sheety_endpoint_url = os.environ.get('sheety_endpoint_url')

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    # 'x-remote-user-id': '0',
}

query_input = input('Tell me which exercise you did: \n')

users_params = {
    "query": query_input,

}

response = requests.post(url=nutritionix_endpoint, json=users_params, headers=headers)
print(response.text)
print(response.json()['exercises'])

new_item_exercise = response.json()['exercises'][0]
print(new_item_exercise['duration_min'])
print(new_item_exercise['nf_calories'])
print(new_item_exercise['name'])

duration_min = new_item_exercise['duration_min']
calories = new_item_exercise['nf_calories']
exercise = new_item_exercise['name']


headers_2 = {
    "Content-Type": "application/json",
    "Authorization": "Basic ZnJhbms5MDkxOjE5OTAwMjAz"
}

sheet_params = {
              "workout": {
                "name": "workouts",
                "email": "hasan9091.fs@gmail.com",
                "date": DATE,
                "time": TIME,
                "exercise": exercise,
                "duration": duration_min,
                "calories": calories,

              }
            }

response_2 = requests.post(url=sheety_endpoint_url, json=sheet_params, headers=headers_2)
print(response_2.text)