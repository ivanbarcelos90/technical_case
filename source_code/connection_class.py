# Import Packages
from sqlalchemy import create_engine

# Set up engine string to the sql server connection
engine_str = 'mssql://@.\SQLEXPRESS/NYC_Taxi_Trips?driver=ODBC Driver 17 for SQL Server'


# create a connection class for sqlalchemy engine
def connection():
    engine = create_engine(engine_str)
    # con = engine.connect(engine)
    return engine
