# Question bonus:  Qual o tempo médio das corridas nos dias de sábado e domingo?

# Import Packages
import pandas as pd
import source_code.connection_class as c

# create sqlalchemy engine.
con = c.connection().engine.connect()

# Set up the query string to be executed by pandas dataframe
query_str = """
            SELECT (AVG(DATEDIFF(SECOND,pickup_datetime,dropoff_datetime)))/60 AS Tempo_Médio
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            WHERE (DATEPART(DW,pickup_datetime) = 1 OR DATEPART(DW,pickup_datetime) = 7)
            """

# Read data from the database and create a pandas dataframe.
df = pd.read_sql(query_str, con)
print(df)
