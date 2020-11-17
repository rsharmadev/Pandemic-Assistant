from flask import Flask, render_template, request
import pandas as pd
import folium
from folium.plugins import HeatMap
import branca
import requests
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder=os.getcwd())
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

show_spread_zones = False
epicenters = ["Illinois_Cook", "California_Los Angeles", "California_San Francisco", "New York_Erie",
              "Oregon_Multnomah", "Florida_Miami-Dade", "Texas_Harris", "Georgia_Fulton", "Michigan_Wayne"]

counties = []

information = json.loads(open("info.json").read())


@app.route("/", methods=["POST", "GET"])
def main():
    global counties, show_spread_zones
    current_time = str((datetime.now() - datetime(1970, 1, 1)).total_seconds())
    if request.method == "GET":
        counties = []
        show_spread_zones = False
        return render_template("main.html", timestamp=current_time)
    elif request.method == "POST":
        form_data = dict(request.form)
        county = form_data["county_input"].split(", ")
        try:
            county_string = county[1] + "_" + county[0]
            if county_string not in counties:
                counties.append(county_string)
        except IndexError:
            pass

        try:
            checkbox = form_data["checkbox_name"] == "on"
        except KeyError:
            checkbox = False

        show_spread_zones = checkbox
        return render_template("main.html", timestamp=current_time)


@app.route('/drawmap')
def draw_map():
    try:
        os.remove("./templates/heatmap.html")
    except FileNotFoundError:
        pass
    global show_spread_zones, counties, epicenters

    map_data = pd.read_csv("data.csv", sep=',')

    url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
    county_geo = f'{url}/us_counties_20m_topo.json'

    colorscale = branca.colormap.LinearColormap(["white", "red"], vmin=0, vmax=0.1)
    employed_series = map_data.set_index('id')['indexlol']

    def style_function(feature):
        employed = employed_series.get(int(feature['id'][-5:]), None)
        return {
            'fillOpacity': 0.5,
            'weight': 0,
            'fillColor': '#black' if employed is None else colorscale(employed)
        }

    m = folium.Map(
        location=[38, -102],
        tiles='cartodbpositron',
        zoom_start=4.5
    )

    folium.TopoJson(
        json.loads(requests.get(county_geo).text),
        'objects.us_counties_20m',
        style_function=style_function
    ).add_to(m)

    if show_spread_zones:
        hmap_lat = []
        hmap_long = []
        hmap_indexes = []
        for x in map_data.indexlol.values.tolist():
            if x > 1.5:
                x_index = map_data.indexlol.values.tolist().index(x)
                hmap_lat.append(list(map_data.latitude.values)[x_index])
                hmap_long.append(list(map_data.longitude.values)[x_index])
                hmap_indexes.append(x)

        hmap_lat = tuple(hmap_lat)
        hmap_long = tuple(hmap_long)
        hmap_indexes = tuple(hmap_indexes)

        hmap = HeatMap(list(zip(hmap_lat, hmap_long, hmap_indexes)),
                       min_opacity=0.5,
                       radius=40,
                       blur=17,
                       max_zoom=1)

        m.add_child(hmap)

    points_to_render = epicenters + counties
    print(points_to_render)

    for item in points_to_render:
        for key, value in information.items():
            if key == item:
                folium.Marker(
                    location=[value['latitude'], value['longitude']],
                    popup=folium.Popup(f"<h3>{key.split('_')[1]}, {key.split('_')[0]}</h3>"
                                       f"<br>Cases: {str(value['cases_current']).split('.')[0]}"
                                       f"<br>Increase of cases per day: {str(value['cases_diff']).split('.')[0]}"
                                       f"<br><br>Population: {str(value['population']).split('.')[0]}"
                                       f"<br>Population density: {str(value['population_density']).split('.')[0]}",
                                       max_width=300),
                    icon=folium.Icon(color='blue'),
                ).add_to(m)

    print(m.to_json())

    m.save('./templates/heatmap.html')

    return open("./templates/heatmap.html").read()


app.run(host="localhost", port=5000)
