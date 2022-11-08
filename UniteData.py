from SenecSim.MomentaryValue import MomentaryValue
from SenecSim.TimeSpanValue import TimeSpanValue
import datetime

import json
import os

filepath_app = os.path.join(os.getenv('APPDATA'), 'SenecSim')


def read_momentary_values() -> list[MomentaryValue]:
    values = []

    for filename in os.listdir(os.path.join(filepath_app, 'historic_data')):
        with open(os.path.join(filepath_app, 'historic_data', filename), 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            for json_value in json_data:
                timestamp = datetime.datetime.strptime(json_value["zeitstempel"], "%Y-%m-%dT%H:%M:%SZ")
                value = MomentaryValue(json_value["messpunkt"], timestamp)
                values.append(value)

    return values


def read_timespan_values() -> list[TimeSpanValue]:
    values = []

    for filename in os.listdir(os.path.join(filepath_app, 'historic_data')):
        with open(os.path.join(filepath_app, 'historic_data', filename), 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            for json_value in json_data:
                timestamp = datetime.datetime.strptime(json_value["zeitstempel"], "%Y-%m-%dT%H:%M:%SZ")
                value = TimeSpanValue(json_value["aggregation"], timestamp)
                values.append(value)

    return values


