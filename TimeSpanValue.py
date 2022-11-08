import datetime


class TimeSpanValue:

    def __init__(self, json_data, timestamp: datetime.datetime):
        self.timestamp = timestamp
        self.production = json_data["stromerzeugung"]["wert"]
        self.usage = json_data["stromverbrauch"]["wert"]
        self.to_grid = json_data["netzeinspeisung"]["wert"]
        self.from_grid = json_data["netzbezug"]["wert"]
        self.to_battery = json_data["speicherbeladung"]["wert"]
        self.from_battery = json_data["speicherentnahme"]["wert"]
        self.soc = json_data["speicherfuellstand"]["wert"]
        self.autark = json_data["autarkie"]["wert"]
        self.self_use = json_data["eigenverbrauchsquote"]["wert"]

    def __lt__(self, other):
        return self.timestamp < other.timestamp
