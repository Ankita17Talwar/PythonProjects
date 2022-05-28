
import folium as fl
import pandas as pd

tiles = "Stamen Terrain"

def get_color(el):
    if el <1000:
        return 'green'
    elif el >= 1000 and el < 3000:
        return 'blue'
    else :
        return 'red'


lat =[]
lon = []
elev =[]
name =[]

def read_data_csv(file_name):
    # Read Data from file
    global lat
    global lon
    global elev
    print('read')
    df = pd.read_csv(file_name, sep=',')
    lat = list(df['LAT'])
    lon = list(df['LON'])
    elev = list(df['ELEV'])
    name = list(df["NAME"])
    print(elev)

read_data_csv('Data\Volcanoes.txt')


map = fl.Map(location=[38.58,-99.89], zoom_start=5, tiles = tiles)

fg = fl.FeatureGroup(name='Map_with_markers&Polygon')

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(fl.CircleMarker(location=[lt,ln], radius =10, popup=el, fill_color= get_color(el),
    color='grey',fill_opacity=0.7))

fg.add_child(fl.GeoJson(data=(open('Data\world.json', 'r', encoding='utf-8-sig')).read(),
 style_function= lambda x: {'fillColor': 'yellow' if x['properties']['POP2005']< 10000000 
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'} ))

map.add_child(fg)
map.save("output/Map_circleMrk_polygon.html")
