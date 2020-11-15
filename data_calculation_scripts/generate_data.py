import json
with open("info.json") as f:
    information = json.loads(f.read())

result = ""
for x in information:
    temp = x.split("_")
    if temp[0] == "highest":
        continue

    try:
        temp_variable = information[x]["cases_total"]
    except LookupError:
        continue
    result += f'<option value="{temp[1] + ", " + temp[0]}">\n'

with open("html_test.txt", "w+") as f:
    f.write(result)
