# Covid19 Instant Maps

This is a simple covid-19 tracker that was created on the fly back in March 2020.
It instantly creates both a current map of the world based on covid-19 cases 
as well as a comma separated values (.csv) file that documents
these cases.

**Install all packages**

```
pip install csv
pip install csv
pip install folium
pip install pandas
pip install webbrowser
pip install os
pip install Covid
```

**Adjust it to your file system**

```
Edit the file paths in these 3 lines so that you can choose 
where the mapFile as well as the .csv file get created.

Line 11: mapFile =  "C://Exodus//Y//Pythonian//covid19//Map1.html"
Line 12: covidDataFile = "C://Exodus//Y//Pythonian//covid19//covidData.csv"
Line 84: url =  "C://Exodus//Y//Pythonian//covid19//Map1.html"
```

**Run the script**

Make sure to activate the virtual environment beforehand

```
python covidTrack.py
```
