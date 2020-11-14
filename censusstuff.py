import json

with open('population.json', 'r') as f:
    population = json.load(f)

with open('county_area.json', 'r') as f:
    county_area = json.load(f)


counties = {}

for item in population:
    counties.update({item['region'] + "_" + item['subregion']: {"population": item['population'], "state_fips": item['us_state_fips'], "county_fips": item['us_county_fips']}})
    
print(counties)
for key, value in counties.items():
    print(value)
    for county in county_area['features']:
        if county['properties']['STATE'] + county['properties']['COUNTY'] == value['county_fips']:
            print(county['properties']['STATE'] + county['properties']['COUNTY'])
            print(value['county_fips'])
            counties[key]['area'] = str(county['properties']['CENSUSAREA'])


for key, value in counties.items():
    try:
        counties[key]['population_density'] = str((int(value['population'])/float(value['area'])))
    except:
        print(key)
        pass




with open("info.json", "w") as f:
    f.write(json.dumps(counties, indent=4))