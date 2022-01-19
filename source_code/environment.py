# Import packages for database connection and data processing.
import os
import pyodbc
import pandas as pd
import connection_class as c
from connection_class import env_str, create_db_str, create_tbl_str

# First Batch - Create a database environment to process the data.

# Set up the database variable using pyodbc using the database string.
conn = pyodbc.connect(env_str)
conn.autocommit = True
print('Connection with database was successful!')

# After the established connection with the instance of sql server, create a cursor for SQL String Execution.
dbcursor = conn.cursor()
print('Cursor created!')

# This cursor contain all script necessary to set up the database and tables that will be used for data processing.
dbcursor.execute(create_db_str)
print('Database created!')

dbcursor.execute(create_tbl_str)
print('Table created!')

# Closing connection with the database.
dbcursor.close()
print('Cursor closed!')
print('Finished creating the Environment!')

# Second Batch
# The goal here is to perform an ETL:
# Extract: A pandas dataframe will be created to extract the data from the json.
# Transform: Some adjustment will be need it to create the dataframe.
# Load: The dataframe will be sent via sqlalchemy engine connection.

# create sqlalchemy engine
con = c.connection().connect()
print('Connection with sqlalchemy was established!')

# Set up the var for the data files.
trips_path = os.path.abspath('../trips')
files = os.listdir(trips_path)

# Loop to process all the data and sent to the database.
for file in files:
    with open(trips_path + '/' + file, 'r') as f:
        data = f.readlines()  # Read data.
        data_rmv_space = map(lambda x: x.rstrip(), data)  # Remove spaces.
        data_json_str = "[" + ','.join(data_rmv_space) + "]"  # Process of data.
        df_data = pd.read_json(data_json_str)  # Create a pandas dataframe.
        df_data.to_sql('data_sample', con, if_exists='append')  # Sent the data from the dataframe to the database.
        print(f'The file "{file}" was processed and sent to the database!')
print('All data was transfer to the database!')
