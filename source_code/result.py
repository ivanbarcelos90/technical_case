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

# Html string for the body construction of the análises.
with open('./html/results.html', 'r') as f:
    body = f.read().format(q1=q1, q2=q2, plt_hist=plt_hist, plt_plot=plt_plot,  b1=b1)

print('Open HTML!')
# Write html to file
html = open(output_file, "w")
html.write(body)
html.close()
webbrowser.open(output_file, new=2)


