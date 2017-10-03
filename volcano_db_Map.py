import folium
import pandas
data = pandas.read_csv("volcano_db.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
nam = list(data["Volcano Name"])
elev = list(data["Elev"])
def color_picker(elev):
    if elev<1000:
        return 'green'
    elif 1000<=elev<=2000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.09,-99.09],zoom_start=5,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,nm,el in zip(lat,lon,nam,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(str(nm)+", Elevation:"+str(el)+"m",parse_html=True),radius=7,color='grey',fill_color=color_picker(el),fill=True,fill_opacity=0.9))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save('volcano_Map1.html')
