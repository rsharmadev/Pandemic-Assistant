import requests
from json import loads
from json import dumps
import json


with open("info.json") as f:
    information = loads(f.read())
"""
largest = 0

for key in information:
    try:
        temp = (information[key]["cases_total"] * 0.356) - information[key]["deaths_total"]
    except KeyError:
        continue

    information[key]["cases_current"] = temp
    if temp > largest:
        largest = temp

print(largest)

with open("info_temp.json", "w+") as f:
    f.write(dumps(information, indent=4))
"""




"""
params = {
    "iso": "USA",
    "region_province": "Virginia"
}

r = requests.get("https://covid-api.com/api/reports/", params=params)
"""
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
          "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
          "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
          "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Dakota", "South Dakota", "Ohio",
          "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
          "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming", "North Carolina"]

for x in states:

    params = {
        "iso": "USA",
        "region_province": x
    }
    r = requests.get("https://covid-api.com/api/reports/", params=params)

    data = loads(r.text)

    for i in data["data"][0]["region"]["cities"]:
        for key in information:
            temp = key.split("_")
            if temp[0].lower() == x.lower() and temp[1].lower() == i["name"].lower():
                information[key]["cases_total"] = i["confirmed"]
                information[key]["deaths_total"] = i["deaths"]
                information[key]["cases_diff"] = i["confirmed_diff"]
                information[key]["deaths_diff"] = i["deaths_diff"]
                break

with open("info.json", "w+") as f:
    f.write(dumps(information, indent=4))
    f.close()

with open('info.json', 'r') as f:
    info = json.load(f)

with open('county_area.json', 'r') as f:
    county_area = json.load(f)

csv = "id,latitude,longitude,sizelol,indexlol,state,county\n"
for key, item in info.items():
    try:
        index = (((100 * ((0.35 * (float(item['population_density']) / float(18561.73))) + (
                0.1 * (float(item['population']) / float(10098053))) + (
                                  0.25 * (float(item['cases_total']) / float(5945))) + (
                                  0.30 * (float(item['cases_current']) / float(111253))))) / (
                          195.981629212551 * 7.37039125000001))) * 10
        csv += f"{item['county_fips']},{item['latitude']},{item['longitude']},{item['area']},{index},{key.split('_')[0]},{key.split('_')[1]}\n"
    except Exception as a:
        pass


with open('data.csv', "w") as f:
    f.write(csv)
