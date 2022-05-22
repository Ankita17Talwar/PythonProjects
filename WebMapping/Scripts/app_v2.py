# Color of popup as per the elevation of volcanoe
import folium
import pandas as pd

def get_color(el):
    if el <1000:
        return 'green'
    elif el >= 1000 and el < 3000:
        return 'blue'
    else :
        return 'red'


tiles = "Stamen Terrain"

# Read Data from file
df = pd.read_csv('Data\Volcanoes.txt', sep=',')
lat = list(df['LAT'])
lon = list(df['LON'])
elev = list(df['ELEV'])
name = list(df["NAME"])


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58,-99.89], zoom_start=5, tiles = tiles)

# Add Marker to a Map
#map.add_child(folium.Marker(location=[28.66,77.24], popup="Hi There!!", icon= folium.Icon(color='red')))
fg = folium.FeatureGroup(name="My Map")

for lt,ln, el, name in zip(lat, lon, elev, name):
    #fg.add_child(folium.Marker(location=[lt,ln], popup=el, icon= folium.Icon(color='red')))
    iframe = folium.IFrame(html=html %  (name, name, el), width=200, height=100) 
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon= folium.Icon(color= get_color(el))))
    
map.add_child(fg)

# print(dir(folium))
map.save("output/Map_icon_color.html")


map = folium.Map(location=[38.58,-99.89], zoom_start=5, tiles = tiles)
# Add Circle marker
fg = folium.FeatureGroup(name="My Map")

for lt,ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius =10, popup=el, fill_color= get_color(el), color='grey',fill_opacity=0.7))

map.add_child(fg)
map.save("output/Map_circle_icon.html")

