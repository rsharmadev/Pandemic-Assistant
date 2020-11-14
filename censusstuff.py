import json

with open('population.json', 'r') as f:
    population = json.load(f)


print(population)

things = {}

for item in population:
    things.update({item['region'] + "_" + item['subregion']: {"population": item['population']}})
    

with open("info.json", "w") as f:
    f.write(json.dumps(things, indent=4))