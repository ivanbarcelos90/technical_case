# Question 1: Qual a distância média percorrida por viagens com no máximo 2 passageiros.
# Import Packages
import pandas as pd
import source_code.connection_class as c

# create sqlalchemy engine.
con = c.connection().engine.connect()

# Set up the query string to be executed by pandas dataframe
query_str = """
            SELECT CAST(AVG(trip_distance) AS DECIMAL(4,2)) AS Distancia_Média
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            WHERE passenger_count <= 2 
            """

# Read data from the database and create a pandas dataframe.
df = pd.read_sql(query_str, con)
print(df)

output_file = 'C:\PersonalProjects/TechnicalCase/source_code/Análise.html'

df.to_html()
