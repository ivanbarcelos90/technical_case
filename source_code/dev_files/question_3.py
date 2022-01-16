# Question 3: Faça um histograma da distribuição mensal, nos 4 anos, de corridas pagas em dinheiro

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
           ,SUM(total_amount) AS TOTAL_AMOUNT
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            WHERE payment_type LIKE 'CASH'
            GROUP BY YEAR(dropoff_datetime), MONTH(dropoff_datetime)
            ORDER BY YEAR(dropoff_datetime), MONTH(dropoff_datetime)
            """

# Read data from the database and create a pandas dataframe.
df = pd.read_sql(query_str, con)
print(df)

# Use matplotlib package to create a histogram with the dataframe data.
plt.hist(df['TOTAL_AMOUNT'], bins=10)
plt.xlabel('Total Amount')
plt.ylabel('Month')
plt.title('Monthly Distribuition')
plt.grid()
plt.show()
