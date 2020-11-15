from flask import Flask, render_template, request
from json import loads, dumps
import os
app = Flask(__name__, static_folder=os.getcwd())

information = loads(open("info.json").read())


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "GET":
        return render_template("main.html")
    elif request.method == "POST":
        form_data = dict(request.form)
        county = form_data["county_input"].split(", ")
        county_string = county[1] + "_" + county[0]

        county_information = information[county_string]

        try:
            checkbox = form_data["checkbox_name"] == "on"
        except KeyError:
            checkbox = False

        return render_template("main.html", county_data=county_information, spread_zones=checkbox)


app.run(host="localhost", port=5000)
