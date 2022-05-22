import folium
import pandas as pd

tiles = "Stamen Terrain"

# Read Data from file
df = pd.read_csv('Data\Volcanoes.txt', sep=',')
lat = list(df['LAT'])
lon = list(df['LON'])
elev = list(df['ELEV'])
name = list(df["NAME"])

#
html = """<h4>Volcano information:</h4>
Height: %s m
"""
# or add link

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
    # iframe = folium.IFrame(html=html % str(el), width=200, height=100)  - to use if using basic html above
    iframe = folium.IFrame(html=html %  (name, name, el), width=200, height=100) 
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon= folium.Icon(color='red')))
    
map.add_child(fg)

# print(dir(folium))
map.save("output/Map.html")


