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

    cursor = connection.cursor()
    # cursor.execute("SELECT current_database();")
    # print("Python connected to:", cursor.fetchone())
    # cursor.execute("""
    #     SELECT table_schema, table_name
    #     FROM information_schema.tables
    #     WHERE table_schema = 'public'
    #     ORDER BY table_name;
    # """)

    # print("Tables in hillel_db:")
    # for table in cursor.fetchall():
    #     print(table)

    #create tables
    create_tb_categories = """
        CREATE TABLE public.categories_py (
    	id int4 GENERATED ALWAYS AS IDENTITY NOT NULL,
    	"name" varchar(100) NOT NULL,
    	description text NULL,
    	CONSTRAINT categories_py_pk PRIMARY KEY (id)
    	)
        """

    cursor.execute(create_tb_categories)
    connection.commit()
    print("categories_py created")

    create_tb_products = """
    CREATE TABLE public.products_py (
	id int4 GENERATED ALWAYS AS IDENTITY NOT NULL,
	product_name varchar(255) NOT NULL,
	description text NULL,
	price numeric(10, 2) NOT NULL,
	quantity int4 NOT NULL,
	category_id int4 NOT NULL,
	CONSTRAINT products_py_pk PRIMARY KEY (id),
	CONSTRAINT products_py_categories_fk FOREIGN KEY (category_id) REFERENCES public.categories_py(id) ON DELETE RESTRICT ON UPDATE CASCADE
	)
    """

    cursor.execute(create_tb_products)
    connection.commit()
    print("products_py created")

    print("Tables created successfully!")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL or creating tables", error)
    connection.rollback()

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")