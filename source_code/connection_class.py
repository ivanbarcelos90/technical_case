# Import Packages
from sqlalchemy import create_engine


# Set up engine string to the sql server connection
engine_str = 'mssql://@.\SQLEXPRESS/NYC_Taxi_Trips?driver=ODBC Driver 17 for SQL Server'


# create a connection class for sqlalchemy engine
def connection():
    engine = create_engine(engine_str)
    return engine


#  A string for connection at the database.
env_str = """
              Driver={SQL Server};
              Server=.\SQLEXPRESS;
              Trusted_Connection=yes;
              """

# This string contain all script necessary to set up the database and tables that will be used for data processing.

create_db_str = """
                IF NOT EXISTS (SELECT * FROM sys.databases WHERE NAME = 'NYC_Taxi_Trips')
                BEGIN 
                    CREATE DATABASE NYC_Taxi_Trips 
                END
                """

create_tbl_str = """
                USE NYC_Taxi_Trips  
            
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
