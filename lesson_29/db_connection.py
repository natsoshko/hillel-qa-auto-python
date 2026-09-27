import time
import os
import psycopg2

time.sleep(30)
def get_dbconnection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
        # dbname = 'hillel_db',
        # user = 'postgres',
        # password = 'postgres_6949',
        # host = '127.0.0.1',
        # port = '5432'
    )
print("Connected to the database!")
