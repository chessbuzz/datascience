
# Imports
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# load in the data
df = pd.read_csv("building_permits.csv")

# instantiate sqlalchemy connection to Postgres
# engine format
# create_engine
    #("<dbms>://<username>:<password>@<hostname>:<port>/<db_name>")
engine = create_engine('postgresql://postgres:password@website.com:5432/database')

# save the data from the dataframe to the postgres table permitinfo
df.to_sql('permitinfo', engine, index=False)
