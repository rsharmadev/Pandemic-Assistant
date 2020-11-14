import json

with open('population.json', 'r') as f:
    population = json.load(f)

with open('county_area.json', 'r') as f:
    county_area = json.load(f)

with open('info.json', 'r') as f:
    counties = json.load(f)

populations = []
popd = []
for key, value in counties.items():
    populations.append(int(value['population']))
    popd.append(float(value['population_density']))

print(max(populations))
print(max(popd))


counties.update({"highest": {
                    "population": {
                        "state_fips": "06",
                        "county_fips": "06037",
                        "county": "Los Angeles",
                        "state": "California",
                        "value": "10098052"
                    },
                    "population_density": {
                        "state_fips": "06",
                        "county_fips": "06075",
                        "county": "San Francisco",
                        "state": "California",
                        "value": "18561.73063384038"
                    }
    }
    })


with open("info.json", "w") as f:
    f.write(json.dumps(counties, indent=4))