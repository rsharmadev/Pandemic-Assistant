import requests
from json import loads
from json import dumps

with open("info_temp.json") as f:
    information = loads(f.read())
"""
params = {
    "iso": "USA",
    "region_province": "Virginia"
}

r = requests.get("https://covid-api.com/api/reports/", params=params)

print(r.text)
"""
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
          "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
          "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
          "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Dakota", "South Dakota", "Ohio",
          "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
          "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

states = ["Utah"]

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

with open("info_temp.json", "w+") as f:
    f.write(dumps(information, indent=4))