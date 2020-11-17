import json

with open('info.json', 'r') as f:
    info = json.load(f)

with open('county_area.json', 'r') as f:
    county_area = json.load(f)

csv = "id,latitude,longitude,sizelol,indexlol,state,county\n"
for key, item in info.items():
    try:
        index = (((100 * ((0.35*(float(item['population_density'])/float(18561.73))) + (0.1*(float(item['population'])/float(10098053))) + (0.25*(float(item['cases_total'])/float(5945))) + (0.30*(float(item['cases_current'])/float(111253)))))/(195.981629212551*7.37039125000001))) * 10
        csv += f"{item['county_fips']},{item['latitude']},{item['longitude']},{item['area']},{index},{key.split('_')[0]},{key.split('_')[1]}\n"
    except Exception as a:
        print("GOOD WORK")
        pass


with open('data.csv', "w") as f:
    f.write(csv)