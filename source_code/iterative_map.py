# Question bonus: Fazer uma visualização em mapa com latitude e longitude de pickups and dropoffs no ano de 2010.

# Import Packages
import pandas as pd
import connection_class as c
import folium
import webbrowser
from os.path import abspath

# create sqlalchemy engine.
con = c.connection().engine.connect()

# Set up the sample size (1 - 1000000) - Obs: Higher sample size will demand a lot CPU processing.
sample = '10'

# Set up the query string to be executed by pandas dataframe
query_str = """SELECT top
            """ + sample + """
                dropoff_latitude AS Dropoff_Latitude
               ,dropoff_longitude AS Dropoff_Longitude
               ,pickup_latitude AS Pickup_Latitude
               ,pickup_longitude AS Pickup_Longitude
           FROM [NYC_Taxi_Trips].[dbo].[data_sample]
           WHERE YEAR(pickup_datetime) = 2010
            """

# Read data from the database and create a pandas dataframe.
df = pd.read_sql(query_str, con)

output_file = abspath('./html/NYC.html')

map = folium.Map(location=['40.730610', '-73.935242'])

for indice, row in df.iterrows():
    folium.Marker(
        location=[row["Pickup_Latitude"], row["Pickup_Longitude"]],
        popup='Pickup - Trip ' + str(indice),
        icon=folium.map.Icon(color='red')
    ).add_to(map)

    folium.Marker(
        location=[row["Dropoff_Latitude"], row["Dropoff_Longitude"]],
        popup='Dropoff Trip ' + str(indice),
        icon=folium.map.Icon(color='blue')
    ).add_to(map)

map.save(output_file)
webbrowser.open(output_file, new=2)
