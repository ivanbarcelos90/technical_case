# Question 4: Faça um gráfico de série temporal contando
# a quantidade de gorjetas de cada dia, nos últimos 3 meses de 2012.

# Import Packages
import pandas as pd
import matplotlib.pyplot as plt
import source_code.connection_class as c

# create sqlalchemy engine.
con = c.connection().engine.connect()

# Set up the query string to be executed by pandas dataframe
query_str = """
            SELECT  YEAR(dropoff_datetime) AS [YEAR]
           ,MONTH(dropoff_datetime) AS [MONTH]
           ,DAY(dropoff_datetime) AS [DAYS]
           ,COUNT(tip_amount) AS TIP_AMOUNT
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            WHERE YEAR(dropoff_datetime) = 2012
            AND   MONTH(dropoff_datetime) IN (8,9,10)
            GROUP BY YEAR(dropoff_datetime), MONTH(dropoff_datetime),DAY(dropoff_datetime)
            ORDER BY YEAR(dropoff_datetime),MONTH(dropoff_datetime),DAY(dropoff_datetime)
            """

# Read data from the database and create a pandas dataframe.
df = pd.read_sql(query_str, con)
print(df)

# Use matplotlib package to create a time series graph with the dataframe data.
plt.plot(df['DAYS'], df['TIP_AMOUNT'])
plt.xlabel('Days')
plt.ylabel('Tip Amount')
plt.title('Time Series Graph')
plt.grid()
plt.show()
