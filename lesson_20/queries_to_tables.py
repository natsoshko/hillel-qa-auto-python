import psycopg2

dbname = 'hillel_db'
user = 'postgres'
password = 'postgres_6949'
host = '127.0.0.1'
port = '5432'

try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")
    print()

    cursor = connection.cursor()

    # select from tables
    query_from_tables = """
        SELECT p.*, c."name" category_name
        FROM public.products_py p
        JOIN public.categories_py c
            ON p.category_id = c.id
    """
    cursor.execute(query_from_tables)
    response_from_query = cursor.fetchall()
    for product in response_from_query:
        print(product)

    print()

except (Exception, psycopg2.Error) as error:
    print("Error", error)
    connection.rollback()

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")