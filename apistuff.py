import requests
from json import loads

params = {
    "iso": "USA",
    "region_province": "Maryland"
}
r = requests.get("https://covid-api.com/api/reports/", params=params)

print(r)

with open('provinces.json', "w") as f:
    f.write(loads(r.text))
