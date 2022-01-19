# Import Packages
import pandas as pd
import matplotlib.pyplot as plt
import connection_class as c
import webbrowser
from os.path import abspath
from query_str import query_str_q1, query_str_q2, query_str_q3, query_str_q4, query_str_b1

# Set up path for the Análise.html file
output_file = abspath('./html/Análise.html')

# create sqlalchemy engine.
con = c.connection().engine.connect()
print('Connection with sqlalchemy was established!')

# Read data from the database and create a pandas dataframe.
dfq1 = pd.read_sql(query_str_q1, con)
q1 = dfq1.iat[0, 0]
print('Dataframe for question 1 was created!')

# Read data from the database and create a pandas dataframe.
dfq2 = pd.read_sql(query_str_q2, con)
print('Dataframe for question 2 was created!')

q2 = dfq2.to_html()
print('Table for question 2 was created!')

# Read data from the database and create a pandas dataframe.
dfq3 = pd.read_sql(query_str_q3, con)
print('Dataframe for question 3 was created!')

month_year = dfq3['YEAR'].astype(str) + '-' + dfq3['MONTH'].astype(str)

# Use matplotlib package to create a histogram with the dataframe data.
plt.figure(figsize=(12, 8))
plt.grid()
plt.hist(month_year)
plt.ylabel('Amount')
plt.xlabel('Period')
plt.xticks(rotation=45, ha='right')
plt.title('Monthly Distribuition')
plt_hist = abspath('./graph/hist.png')
plt.savefig(plt_hist)
print('Histogram graph for question 3 was created!')

# Read data from the database and create a pandas dataframe.
dfq4 = pd.read_sql(query_str_q4, con)
print('Dataframe for question 4 was created!')

# Use matplotlib package to create a time series graph with the dataframe data.
plt.clf()
plt.plot(dfq4['DAYS'], dfq4['TIP_AMOUNT'])
plt.xlabel('Days')
plt.ylabel('Tip Amount')
plt.title('Time Series Graph')
plt.grid()
plt_plot = abspath('./graph/time_series.png')
plt.savefig(plt_plot)
print('Time series graph for question 1 was created!')

# Read data from the database and create a pandas dataframe.
dfb1 = pd.read_sql(query_str_b1, con)
b1 = dfb1.iat[0, 0]
print('Dataframe for question bonus 1 was created!')

# Html string for the body construction of the analises.
body = '''
<html>
    <body>
        <title>Análise</title>
        <p><font size="6.5"> Resposta das questões para o case Tecnico da DadoEsfera!<br></font>      
       <br><br>

       <font size="4"> 
       Para esse case tecnico foi recebido dados em formato json.<br>
       Logo, opós análises dos dados brutos, optei enviar os dados para um banco de dados local (SQL Server).<br>
       Para tal, verifiquei o tipo de dados de cada coluna para criar a tabela que receberia os dados.
       <br>
       <br>
       Criei o arquivo environment.py, apenas para criação do ambiente e envio dos dados.<br>
       Contudo, devido ao estado que estava os dados brutos, foi necessário tratar os dados e assim envia-los para 
       o banco.
       <br>
       <br>
       Utilizei a biblioteca pyodbc para fazer a conexão com o banco e criar as databases e tabelas e o pandas para<br>
       criar os dataframe com os dados e envia-los para o banco.
       <br>
       <br>
       Com os dados dispoíveis no banco, usei a IDE Azure Data Studio para desenvolver as queries que iriam buscar<br>
       as informações desejadas.<br>
       Com as queries prontas para cada questão, criei o arquivo result.py, onde utilizei o pandas para executar as<br>
       queries e armazena-las em dataframes de todas as questões.<br>
       Esses dataframes disponizados em uma string para apresentação em formato .html.
       <br>
       <br>
       Para as questões 3 e 4, foi necessário utilizar a biblioteca matplotlib, reponsável por utilizar os 
       dataframes e visualiza-los em gráficos de histograma e série temporal.
       <br>
       <br>
       Para questão bonus do mapa interativo, criei o arquivo iterative_map.py para criar o mapa interativo <br>
       em html. Foi utilizado a biblioteca folium para essa questão. 
       <br>
       <br>
       Abaixo demonstra as questões e suas respectivas respostas:
       <br>
       <br>
       <br>        
       </font>

       <font size="5"> Questão 1 <br></font>
       <br>      
       <font size="4"> Foi requerido a distância média que é percorrida por viagens com no máximo 2 passageiros.<br>
       De acordo com os dados, estima-se que a média é de {q1} km por viagem. <br></font>
       <br>
       <br>
       <font size="5"> Questão 2 <br></font>
       <br>
       <font size="4"> Foi requerido os 3 maiores "Vendors" no quesito "quantidade total de dinheiro arrecadado"<br>
       E de acordo com os dados da tabela, percebe-se que CMT segue em primeiro com o maior dinheiro arrecado,<br> 
       seguido de VTS e DDS.
       abaixo: <br></font>
       <br>
       {q2}
       <br>
       <font size="5"> Questão 3 <br></font>
       <br>
       <font size="4"> Foi requerido nessa questão uma distribuição mensal das corridas pagas em dinheiro<br> 
       de taxi na cidade de Nova York para os anos de 2009-2012. <br>
       Com o gráfico de distribuição mensal é possível perceber que o período de férias no final do ano <br>
       indicou um aumento dos pagamentos com dinheiro, devido ao aumento de turistas nessa época do ano.</font>      
       <br><br>
       <img src={plt_hist}></img>
       <br>
       <br>
       <font size="5"> Questão 4 <br></font>
       <br>
       <font size="4"> Foi requeido um gráfico de série temporal contendo a quantidade de gorjetas de cada dia,
       nos últimos 3 meses de 2012.<br>
       Logo, pode-se observar que a quantidade de gorjetas por dia, variou entre 3200 e 3500 gorjetas nos últimos
       3 meses de 2012.
       <br><br>       
       <img src={plt_plot}></img>
       <br>  
       <font size="5"> Questão Bonus 1 <br></font>
       <br>
       <font size="4"> Foi requerido o tempo médio das corridas nos dias de sábado e domingo. 
       Os dados sujerem que o tempo médio gasto nas corridas nos final de semana varia em torno de {b1} minutos.
       <br>
       <br>  
       <br>
       <br>
       <br>
       <br>
       </p>   
    </body>
</html>
'''.format(q1=q1, q2=q2, plt_hist=plt_hist, plt_plot=plt_plot,  b1=b1)

print('Open HTML!')
# Write html to file
html = open(output_file, "w")
html.write(body)
html.close()
webbrowser.open(output_file, new=2)


