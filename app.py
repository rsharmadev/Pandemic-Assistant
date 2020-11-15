from flask import Flask
from flask import request
from flask import render_template
import pandas as pd
import os
import auth
import csv
import json
import folium
from folium.plugins import HeatMap
import numpy as np 



app = Flask(__name__)


@app.route('/drawmap')
def draw_map():
    map_data = pd.read_csv("data.csv", sep=',')

    lat = map_data['latitude'].mean()
    
    lon = map_data['longitude'].mean()

    # startingLocation = [lat, lon]
    
    hmap = folium.Map(location=[39.065236, -76.9767335], zoom_start=4)
    
    max_amount = float(map_data['indexlol'].max())
    
    hm_wide = HeatMap( list(zip(map_data.latitude.values, map_data.longitude.values, map_data.indexlol.values)),
                        min_opacity=0.5,
                        max_val=max_amount,
                        radius=20, blur=17,
                        max_zoom=1)
    hmap.add_child(hm_wide)
    
    print(hmap)
    
    hmap.save('./templates/heatmap.html')
    
    return render_template('heatmap.html')

app.run()