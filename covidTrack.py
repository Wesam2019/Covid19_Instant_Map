import csv
import folium
import pandas
import webbrowser
import os
from covid import Covid

def comma_val(number): 
    return ("{:,}".format(number))

mapFile =  "C://Exodus//Y//Pythonian//covid19//Map1.html"
covidDataFile = "C://Exodus//Y//Pythonian//covid19//covidData.csv"
    
if os.path.exists(mapFile):
    os.remove(mapFile)
elif os.path.exists(covidDataFile):
    os.remove(covidDataFile)

covid = Covid()

confirmed = covid.get_total_confirmed_cases()
recovered = covid.get_total_recovered()
deaths = covid.get_total_deaths()

csv_columns = ['id', 'country', 'confirmed', 'active', 'deaths',
            'recovered', 'latitude', 'longitude', 'last_update']
csv_file = "covidData.csv"
dict_data = covid.get_data()

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")

data = pandas.read_csv("covidData.csv")
country = list(data["country"])
confirmed = list(data["confirmed"])
active = list(data["active"])
deaths = list(data["deaths"])
recovered = list(data["recovered"])
latitude = list(data["latitude"])
longitude = list(data["longitude"])

map = folium.Map(location=[83.670077, 42.918783], zoom_start=3, min_zoom=3, max_bounds=True)

try:
    folium.Marker(
        location=[83.670077, 35],
        popup=comma_val(covid.get_total_confirmed_cases()),
        icon=folium.Icon(color='orange', icon='info-sign')
    ).add_to(map)

    folium.Marker(
        location=[83.670077, 45],
        popup=comma_val(covid.get_total_recovered()),
        icon=folium.Icon(color='green', icon='info-sign')
    ).add_to(map)

    folium.Marker(
        location=[83.670077, 55],
        popup=comma_val(covid.get_total_deaths()),
        icon=folium.Icon(color='blue', icon='cloud')
    ).add_to(map)

    fg = folium.FeatureGroup(name="Covid19")



    for cou, con, act, dea, rec, lat, lon in zip(country, confirmed, active, deaths, recovered, latitude, longitude):
        fg.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(str(cou) + "\nConfirmed: " + str(con) + "\nActive: " + str(
            act) + "\nDeaths: " + str(dea) + "\nRecovered: " + str(rec), parse_html=True), icon=folium.Icon(color='red')))


except ValueError:
    pass

map.add_child(fg)
map.save("Map1.html")

url =  "C://Exodus//Y//Pythonian//covid19//Map1.html"

webbrowser.open_new_tab(url)