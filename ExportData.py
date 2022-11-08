import json
import os
import requests
import datetime

senec_login_url = 'https://app-gateway-prod.senecops.com/v1/senec/login'
senec_misc_url = 'https://app-gateway-prod.senecops.com/v1/senec/anlagen'
senec_data_url = 'https://app-gateway-prod.senecops.com/v1/senec/anlagen'
login_file = os.path.join(os.getenv('APPDATA'), 'SenecSim', 'login_data.json')

data_type = 'TAG'
timezone = 'Europe%2FBerlin'
formatted_now = datetime.datetime.now().strftime("%Y-%m-%d") + 'T12%3A00%3A00Z'


with open(login_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)
    username = json_data["username"]
    password = json_data["password"]

login_params = {
    "password": password,
    "username": username
}

login_request = requests.post(senec_login_url, json=login_params)
token = json.loads(login_request.text)["token"]

misc_request = requests.get(senec_misc_url, headers={'Authorization': token})
battery_id = json.loads(misc_request.text)[0]["id"]


def format_url(datetime: datetime.datetime):
    formatted_datetime = datetime.strftime("%Y-%m-%d") + 'T12%3A00%3A00Z'
    return f'https://app-gateway-prod.senecops.com/v1/senec/anlagen/{battery_id}/zeitverlauf?' \
    f'periode={data_type}&timezone={timezone}&before={formatted_datetime}'


# data_request = requests.get(url=format_url(datetime.datetime(year=2022, month=7, day=8)), headers={'Authorization': token})
# data_points = len(json.loads(data_request.text)["datenpunkte"])


historic_data = []
data_points = 1
# current_date = datetime.datetime(year=2022, month=1, day=16)
current_date = datetime.datetime.now()
while data_points > 0:
    # data_request = requests.get(url=format_url(datetime.datetime.now()), headers={'Authorization': token})
    data_request = requests.get(url=format_url(current_date), headers={'Authorization': token})
    json_response = json.loads(data_request.text)
    data_points = len(json_response["datenpunkte"])
    historic_data.extend(json_response["datenpunkte"])

    json_object = json.dumps(json_response["datenpunkte"], indent=4)
    with open(os.path.join(os.getenv('APPDATA'), 'SenecSim', 'historic_data', f'{current_date.strftime("%Y-%m-%d")}.json'), "w") as outfile:
        outfile.write(json_object)

    print(f'Requesting for day: {current_date.strftime("%Y-%m-%d")}')

    # current_date = current_date - datetime.timedelta(days=1)
    current_date = datetime.datetime.strptime(json_response["datenpunkte"][0]["zeitstempel"], "%Y-%m-%dT%H:%M:%SZ")
