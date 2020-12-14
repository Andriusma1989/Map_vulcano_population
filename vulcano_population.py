import folium
import pandas
#loading data from text file
data = pandas.read_csv("Volcanoes.txt")
#creating 3 list with longitude and latitude cordinates and elevation
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

#creating function to change color acording to elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'



#create map with cordinates
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")


#creating FeatureGroup, wich helps create multiple markers
fgv = folium.FeatureGroup(name="Volcanos")


#creating multiple markers with for loop
for lt, ln, el in zip(lat, lon, elev):
#creating markers with pop up text on the map and pass icon parameter
#changing circle markers, adding radius for circle size, and opacity for transparacy
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color = color_producer(el), color = 'grey',fill = True, fill_opacity = 0.7))
#creating feature GRoup for population
fgp = folium.FeatureGroup(name="Populiation")

#addind polygob layer from world text file. Adding diferent colors for population size
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
                          if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#adding featureGruops to map
map.add_child(fgv)
map.add_child(fgp)
#adding layer control to change between features
map.add_child(folium.LayerControl())
map.save("Map1.html")


