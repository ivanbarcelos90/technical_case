# Set up the sample size (1 - 1000000) - Obs: Higher sample size will demand a lot CPU processing.
sample = '10'

# Set up the query string to be executed by pandas dataframe
query_str_q1 = """
            SELECT CAST(AVG(trip_distance) AS DECIMAL(4,2)) AS Distancia_Média
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            WHERE passenger_count <= 2 
            """

# Set up the query string to be executed by pandas dataframe
query_str_q2 = """
            SELECT TOP 3 [vendor_id] AS Vendors
                        ,SUM(total_amount) AS Total_Amount
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            GROUP BY [vendor_id]
            ORDER BY Total_Amount DESC
            """

# Set up the query string to be executed by pandas dataframe
query_str_q3 = """
            SELECT  YEAR(dropoff_datetime) AS [YEAR]
                   ,MONTH(dropoff_datetime) AS [MONTH]
                   ,total_amount AS TOTAL_AMOUNT
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            WHERE payment_type LIKE 'CASH'
            GROUP BY YEAR(dropoff_datetime), MONTH(dropoff_datetime), total_amount
            ORDER BY YEAR(dropoff_datetime), MONTH(dropoff_datetime)
            """

# Set up the query string to be executed by pandas dataframe
query_str_q4 = """
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

# Set up the query string to be executed by pandas dataframe
query_str_b1 = """
                   SELECT (AVG(DATEDIFF(SECOND,pickup_datetime,dropoff_datetime)))/60 AS Tempo_Médio
                   FROM [NYC_Taxi_Trips].[dbo].[data_sample]
                   WHERE (DATEPART(DW,pickup_datetime) = 1 OR DATEPART(DW,pickup_datetime) = 7)
                   """

# Set up the query string to be executed by pandas dataframe
map_str = """SELECT top
            """ + sample + """
                dropoff_latitude AS Dropoff_Latitude
               ,dropoff_longitude AS Dropoff_Longitude
               ,pickup_latitude AS Pickup_Latitude
               ,pickup_longitude AS Pickup_Longitude
           FROM [NYC_Taxi_Trips].[dbo].[data_sample]
           WHERE YEAR(pickup_datetime) = 2010
            """
