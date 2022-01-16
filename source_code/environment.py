# Import packages for database connection and data processing.
import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# First Batch - Create a database environment to process the data.
# Create a string connection for the database.
conn_string = """
              Driver={SQL Server};
              Server=.\SQLEXPRESS;
              Trusted_Connection=yes;
              """
# Set up the database variable using pyodbc using the database string.
conn = pyodbc.connect(conn_string)
conn.autocommit = True

# After the established connection with the instance of sql server, create a cursor for SQL String Execution.
dbcursor = conn.cursor()

# This string contain all script necessary to set up the database and tables that will be used for data processing.
db_string = """
            IF NOT EXISTS (SELECT * FROM sys.databases WHERE NAME = 'NYC_Taxi_Trips')
            BEGIN 
                CREATE DATABASE NYC_Taxi_Trips 
            END     
            
            USE NYC_Taxi_Trips 
                                   
            IF OBJECT_ID(N'dbo.data_vendor_lookup') IS NOT NULL
                DROP TABLE data_vendor_lookup
            
            CREATE TABLE data_vendor_lookup
            (
                 [vendor_id] VARCHAR(5) NULL
                ,[name] VARCHAR(50) NULL
                ,[address] NVARCHAR(50) NULL
                ,[city] VARCHAR(20) NULL
                ,[state] VARCHAR(4) NULL
                ,[zip] SMALLINT NULL
                ,[country] VARCHAR(50) NULL
                ,[contact] NVARCHAR(100) NULL
                ,[current] VARCHAR(3) NULL
            )
            
            IF OBJECT_ID(N'dbo.data_sample') IS NOT NULL
                DROP TABLE data_sample
            
            CREATE TABLE data_sample
            (
                 [index] BIGINT NULL
                ,vendor_id VARCHAR(3) NULL       
                ,pickup_datetime DATETIMEOFFSET NULL
                ,dropoff_datetime DATETIMEOFFSET NULL
                ,passenger_count TINYINT NULL
                ,trip_distance FLOAT
                ,pickup_longitude NUMERIC(8,6) NULL
                ,pickup_latitude NUMERIC(8,6) NULL
                ,rate_code NVARCHAR(MAX) NULL
                ,store_and_fwd_flag NVARCHAR(MAX) NULL
                ,dropoff_longitude NUMERIC(8,6) NULL
                ,dropoff_latitude NUMERIC(8,6) NULL
                ,payment_type VARCHAR(10) NULL
                ,fare_amount SMALLINT NULL
                ,surcharge SMALLINT NULL
                ,tip_amount SMALLINT NULL
                ,tolls_amount SMALLINT NULL
                ,total_amount SMALLINT NULL
            )
            """
# Execution of the script.
dbcursor.execute(db_string)
# Closing connection with the database.
dbcursor.close()

# Second Batch
# The goal here is to perform an ETL:
# Extract: A pandas dataframe will be created to extract the data from the json.
# Transform: Some adjustment will be need it to create the dataframe.
# Load: The dataframe will be sent via sqlalchemy engine connection.

# create sqlalchemy engine
engine_str = 'mssql://@.\SQLEXPRESS/NYC_Taxi_Trips?driver=ODBC Driver 17 for SQL Server'
engine = create_engine(engine_str)
con = engine.connect()

# Set up the path variables for the data.
data_path_2009 = 'C:\PersonalProjects/technical_case/trips/data-sample_data-nyctaxi-trips-2009-json_corrigido.json'
data_path_2010 = 'C:\PersonalProjects/technical_case/trips/data-sample_data-nyctaxi-trips-2010-json_corrigido.json'
data_path_2011 = 'C:\PersonalProjects/technical_case/trips/data-sample_data-nyctaxi-trips-2011-json_corrigido.json'
data_path_2012 = 'C:\PersonalProjects/technical_case/trips/data-sample_data-nyctaxi-trips-2012-json_corrigido.json'

# Read the json removing all whitespaces characters.
with open(data_path_2009, 'r') as f1:
    data_2009 = f1.readlines()

with open(data_path_2010, 'r') as f2:
    data_2010 = f2.readlines()

with open(data_path_2011, 'r') as f3:
    data_2011 = f3.readlines()

with open(data_path_2012, 'r') as f4:
    data_2012 = f4.readlines()

# Remove spaces.
data_2009 = map(lambda x: x.rstrip(), data_2009)
data_2010 = map(lambda x: x.rstrip(), data_2010)
data_2011 = map(lambda x: x.rstrip(), data_2011)
data_2012 = map(lambda x: x.rstrip(), data_2012)

# Add brackets in the begin of the file and at the end.
# Add comma at the end of the json object to fit the criteria to send the data to the database.
data_2009_json_str = "[" + ','.join(data_2009) + "]"
data_2010_json_str = "[" + ','.join(data_2010) + "]"
data_2011_json_str = "[" + ','.join(data_2011) + "]"
data_2012_json_str = "[" + ','.join(data_2012) + "]"

# Create a pandas dataframe.
df_data_2009 = pd.read_json(data_2009_json_str)
df_data_2010 = pd.read_json(data_2010_json_str)
df_data_2011 = pd.read_json(data_2011_json_str)
df_data_2012 = pd.read_json(data_2012_json_str)

# Sent the data from the dataframe to the database, appending the data if necessary.
df_data_2009.to_sql('data_sample', con, if_exists='append')
df_data_2010.to_sql('data_sample', con, if_exists='append')
df_data_2011.to_sql('data_sample', con, if_exists='append')
df_data_2012.to_sql('data_sample', con, if_exists='append')
