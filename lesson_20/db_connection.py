import psycopg2

def get_dbconnection():
    return psycopg2.connect(
        dbname = 'hillel_db',
        user = 'postgres',
        password = 'postgres_6949',
        host = '127.0.0.1',
        port = '5432'
    )

