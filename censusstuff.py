import json

with open('population.json', 'r') as f:
    population = json.load(f)


print(population)

for item in population:
    