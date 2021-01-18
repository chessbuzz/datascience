# Imports
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# load in the data

df = pd.read_csv("iris.csv")

# df = pd.read_csv("building_permits.csv")
print(df.head())

# instantiate sqlalchemy connection to Postgres
# engine format
# create_engine
    #("<dbms>://<username>:<password>@<hostname>:<port>/<db_name>")
engine = create_engine('postgresql://postgres:Password@911@website.com:5432/buildingpermits')

# create an iterable that will read chunksize 1000 rows at a time
# save the data from the dataframe to the postgres table permitinfo

for df in pd.read_csv('building_permits.csv', chunksize=1000):
    df.to_sql(
    'permitinfo',
    engine,
    index = False,
    if_exists='append' # if table exists append this data
    )
