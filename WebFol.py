import folium
import pandas


data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(el):
    if el<1000:
        return 'green'
    elif 1000 <=el <3000:
        return 'orange'
    else:
        return 'blue'


map = folium.Map(location=[38.43,-99.84], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="MyMap.html")
for lt, ln,el in zip(lat,lon, elev) :
    fg.add_child(folium.Marker(location= [lt,ln], popup=str(el), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("MyMap.html")


