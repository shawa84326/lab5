import pandas as pd
import psycopg2

# Load CSV data into DataFrame
events_data = pd.read_csv('eventseattle.csv')

# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
    user="xbmqnounao",
    password="12D177O375IC8KO7$",
    host="ankit25-lab5-redo-server.postgres.database.azure.com",
    port=5432,
    database="ankit25-lab5-redo-database"
)
# Insert data into the PostgreSQL database
events_data.to_sql('events_table', connection, index=False, if_exists='replace')

