# Question 2: Quais os 3 maiores vendors em quantidade total de dinheiro arrecadado.
# Import Packages
import pandas as pd
import source_code.connection_class as c

# create sqlalchemy engine.
con = c.connection().engine.connect()

# Set up the query string to be executed by pandas dataframe
query_str = """
            SELECT TOP 3 [vendor_id] AS Vendors
                        ,SUM(total_amount) AS Total_Amount
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            GROUP BY [vendor_id]
            ORDER BY Total_Amount DESC
            """

# Read data from the database and create a pandas dataframe.
df = pd.read_sql(query_str, con)
print(df)
