import json

with open('population.json', 'r') as f:
    population = json.load(f)

with open('county_area.json', 'r') as f:
    county_area = json.load(f)


with open('info.json', 'r') as f:
    counties = json.load(f)

    
for key, value in counties.items():
    for county in county_area['features']:
        if county['properties']['STATE'] + county['properties']['COUNTY'] == value['county_fips']:
            counties[key]['area'] = str(county['properties']['CENSUSAREA'])
            lat = 0
            long_ = 0
            coordinates = county['geometry']['coordinates']
            

            print(coordinates)
            if len(coordinates[0]) != 1:
                for item in coordinates[0]:
                    print(item)
                    lat += item[1]
                    long_ += item[0]
                counties[key]['latitude'] = str(lat/len(coordinates[0]))
                counties[key]['longitude'] = str(long_/len(coordinates[0]))
            else:
                for item in coordinates[0][0]:
                    print(item)
                    lat += item[1]
                    long_ += item[0]
                counties[key]['latitude'] = str(lat/len(coordinates[0][0]))
                counties[key]['longitude'] = str(long_/len(coordinates[0][0]))

            


for key, value in counties.items():
    try:
        counties[key]['population_density'] = str((int(value['population'])/float(value['area'])))
    except:
        pass




with open("info.json", "w") as f:
    f.write(json.dumps(counties, indent=4))