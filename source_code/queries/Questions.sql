-- Questão 1
SELECT CAST(AVG(trip_distance) AS DECIMAL(4,2)) AS Distancia_Media
FROM [NYC_Taxi_Trips].[dbo].[data_sample]
WHERE passenger_count <= 2 

-- Questão 2
SELECT TOP 3 [vendor_id] AS Vendedores
            ,SUM(total_amount) AS Dinheiro_Arrecadado
FROM [NYC_Taxi_Trips].[dbo].[data_sample]
GROUP BY [vendor_id]
ORDER BY Dinheiro_Arrecadado DESC

-- Questão 3
SELECT  YEAR(dropoff_datetime) AS [YEAR]
       ,MONTH(dropoff_datetime) AS [MONTH]
       ,total_amount AS TOTAL_AMOUNT
FROM [NYC_Taxi_Trips].[dbo].[data_sample]
WHERE payment_type LIKE 'CASH'
GROUP BY YEAR(dropoff_datetime), MONTH(dropoff_datetime), total_amount
ORDER BY YEAR(dropoff_datetime), MONTH(dropoff_datetime)

-- Questão 4
SELECT  YEAR(dropoff_datetime) AS [YEAR]
       ,MONTH(dropoff_datetime) AS [MONTH]
       ,DAY(dropoff_datetime) AS [DAYS]
       ,COUNT(tip_amount) AS TIP_AMOUNT
FROM [NYC_Taxi_Trips].[dbo].[data_sample]
WHERE YEAR(dropoff_datetime) = 2012
AND   MONTH(dropoff_datetime) IN (8,9,10)
GROUP BY YEAR(dropoff_datetime), MONTH(dropoff_datetime),DAY(dropoff_datetime)
ORDER BY YEAR(dropoff_datetime),MONTH(dropoff_datetime),DAY(dropoff_datetime)

-- Questão Bonus 1
SELECT (AVG(DATEDIFF(SECOND,pickup_datetime,dropoff_datetime)))/60 AS Tempo_Médio
FROM [NYC_Taxi_Trips].[dbo].[data_sample]
WHERE (DATEPART(DW,pickup_datetime) = 1 OR DATEPART(DW,pickup_datetime) = 7)

-- Questão Bonus 2
SELECT dropoff_latitude AS Dropoff_Latitude
      ,dropoff_longitude AS Dropoff_Longitude
      ,pickup_latitude AS Pickup_Latitude
      ,pickup_longitude AS Pickup_Longitude
FROM [NYC_Taxi_Trips].[dbo].[data_sample]
WHERE YEAR(pickup_datetime) = 2010







 