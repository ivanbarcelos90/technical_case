# Import Packages
import pandas as pd
import matplotlib.pyplot as plt
import connection_class as c
import webbrowser

# Set up path for the Análise.html file
output_file = 'C:\PersonalProjects/TechnicalCase/source_code/html/Análise.html'

# create sqlalchemy engine.
con = c.connection().engine.connect()

# Set up the query string to be executed by pandas dataframe
query_str_q1 = """
            SELECT CAST(AVG(trip_distance) AS DECIMAL(4,2)) AS Distancia_Média
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            WHERE passenger_count <= 2 
            """

# Read data from the database and create a pandas dataframe.
dfq1 = pd.read_sql(query_str_q1, con)

q1 = dfq1.iat[0, 0]

# Set up the query string to be executed by pandas dataframe
query_str_q2 = """
            SELECT TOP 3 [vendor_id] AS Vendors
                        ,SUM(total_amount) AS Total_Amount
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            GROUP BY [vendor_id]
            ORDER BY Total_Amount DESC
            """

# Read data from the database and create a pandas dataframe.
dfq2 = pd.read_sql(query_str_q2, con)

q2 = dfq2.to_html()

# Set up the query string to be executed by pandas dataframe
query_str_q3 = """
            SELECT  YEAR(dropoff_datetime) AS [YEAR]
           ,MONTH(dropoff_datetime) AS [MONTH]
           ,SUM(total_amount) AS TOTAL_AMOUNT
            FROM [NYC_Taxi_Trips].[dbo].[data_sample]
            WHERE payment_type LIKE 'CASH'
            GROUP BY YEAR(dropoff_datetime), MONTH(dropoff_datetime)
            ORDER BY YEAR(dropoff_datetime), MONTH(dropoff_datetime)
            """

# Read data from the database and create a pandas dataframe.
dfq3 = pd.read_sql(query_str_q3, con)

# Use matplotlib package to create a histogram with the dataframe data.
plt.hist(dfq3['TOTAL_AMOUNT'], bins=10)
plt.xlabel('Total Amount')
plt.ylabel('Month')
plt.title('Monthly Distribuition')
plt.savefig('C:\PersonalProjects/TechnicalCase/source_code/graph/hist.png')

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

# Read data from the database and create a pandas dataframe.
dfq4 = pd.read_sql(query_str_q4, con)

# Use matplotlib package to create a time series graph with the dataframe data.
plt.clf()
plt.plot(dfq4['DAYS'], dfq4['TIP_AMOUNT'])
plt.xlabel('Days')
plt.ylabel('Tip Amount')
plt.title('Time Series Graph')
plt.grid()
plt.savefig('C:\PersonalProjects/TechnicalCase/source_code/graph/time_series.png')

# Set up the query string to be executed by pandas dataframe
query_str_b1 = """
                   SELECT (AVG(DATEDIFF(SECOND,pickup_datetime,dropoff_datetime)))/60 AS Tempo_Médio
                   FROM [NYC_Taxi_Trips].[dbo].[data_sample]
                   WHERE (DATEPART(DW,pickup_datetime) = 1 OR DATEPART(DW,pickup_datetime) = 7)
                   """

# Read data from the database and create a pandas dataframe.
dfb1 = pd.read_sql(query_str_b1, con)

b1 = dfb1.iat[0, 0]

body = '''
<html>
    <body>
        <title>Análise</title>
        <p><font size="6.5"> Resposta das questões para o case Tecnico da DadoEsfera!<br></font>      
       <br>
       <font size="5"> Questão 1 <br></font>
       <br>
       <font size="4"> A distância média percorrida por viagens com no máximo 2 passageiros é de {q1} km. <br></font>
       <br>
       <br>
       <font size="5"> Questão 2 <br></font>
       <br>
       <font size="4"> Os 3 maiores Vendors em quantidade total de dinheiro arrecadado pode ser visualizado pela tabela
       abaixo: <br></font>
       <br>
       {q2}
       <br>
       <font size="5"> Questão 3 <br></font>
       <br>
       <font size="4"> Abaixo demonstra a distribuição mensal das corridas pagas em dinheiro de taxi na cidade 
       de Nova York para os anos de 2009-2012.
       <br>       
       <img src="C:\PersonalProjects/TechnicalCase/source_code/graph/hist.png"></img>
       <br>
       <br>
       <font size="5"> Questão 4 <br></font>
       <br>
       <font size="4"> Abaixo representa o gráfico de série temporal contendo a quantidade de gorjetas de cada dia,
       nos últimos 3 meses de 2012.
       <br>       
       <img src="C:\PersonalProjects/TechnicalCase/source_code/graph/time_series.png"></img>
       <br>  
       <font size="5"> Questão Bonus 1 <br></font>
       <br>
       <font size="4"> O tempo médio das corridas nos dias de sábado e domingo é de {b1} minutos.
       <br>
       <br>  
       <br>
       <br>
       <br>
       <br>
       </p>   
    </body>
</html>
'''.format(q1=q1, q2=q2, b1=b1)

# Write html to file
html = open(output_file, "w")
html.write(body)
html.close()
webbrowser.open(output_file, new=2)


