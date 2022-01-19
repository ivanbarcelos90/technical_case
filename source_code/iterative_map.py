# Questão bonus: Fazer uma visualização em mapa com latitude e longitude de pickups and dropoffs no ano de 2010.

# Import Packages
import pandas as pd
import connection_class as c
import folium
import webbrowser
from os.path import abspath
from query_str import map_str

# create sqlalchemy engine.
con = c.connection().engine.connect()

# Read data from the database and create a pandas dataframe.
df = pd.read_sql(map_str, con)

output_file = abspath('./html/NYC.html')

m = folium.Map(location=['40.730610', '-73.935242'])

# Loop to create the markers at the interative map.
for indice, row in df.iterrows():
    folium.Marker(
        location=[row["Pickup_Latitude"], row["Pickup_Longitude"]],
        popup='Pickup - Trip ' + str(indice),
        icon=folium.map.Icon(color='red')
    ).add_to(m)

    folium.Marker(
        location=[row["Dropoff_Latitude"], row["Dropoff_Longitude"]],
        popup='Dropoff Trip ' + str(indice),
        icon=folium.map.Icon(color='blue')
    ).add_to(m)

m.save(output_file)
webbrowser.open(output_file, new=2)
