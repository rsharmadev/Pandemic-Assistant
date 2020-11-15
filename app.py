from flask import Flask
from flask import render_template
import pandas as pd
import folium
from folium.plugins import HeatMap
import branca
import requests
import json

app = Flask(__name__)


@app.route('/drawmap')
def draw_map():
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

    m.save('./templates/heatmap.html')

    return render_template('heatmap.html')


app.run()
