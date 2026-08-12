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

    # insert values into tables
    categories = [
        ('Fashion', 'Clothes and fashion items'),
        ('Pets', 'Products for pets'),
        ('Electronics', 'Electronic devices and accessories'),
        ('Home', 'Products for home and kitchen'),
        ('Books', 'Books and educational materials'),
        ('Sports', 'Sports equipment and accessories')
    ]
    cursor.executemany(
        """
        INSERT INTO public.categories_py ("name", description)
        VALUES (%s, %s)
        """,
        categories
    )

    products = [
        ('Cotton T-Shirt', 'Basic cotton T-shirt', 19.99, 50, 1),
        ('Running Shoes', 'Lightweight running shoes', 79.90, 18, 1),
        ('Premium Dog Food', 'High-quality dry food for adult dogs', 29.99, 39, 2),
        ('Cat Scratching Post', 'Durable scratching post for cats', 34.50, 27, 2),
        ('Wireless Headphones', 'Bluetooth over-ear headphones', 89.99, 25, 3),
        ('Mechanical Keyboard', 'RGB mechanical keyboard', 74.50, 15, 3),
        ('Coffee Maker', 'Automatic drip coffee maker', 64.99, 10, 4),
        ('Kitchen Scale', 'Digital kitchen scale', 24.50, 22, 4),
        ('Python Programming Book', 'Beginner Python programming guide', 35.00, 30, 5),
        ('SQL for Beginners', 'Introduction to SQL and databases', 42.99, 20, 5),
        ('Yoga Mat', 'Non-slip exercise yoga mat', 29.99, 35, 6),
        ('Dumbbells Set', 'Adjustable dumbbells set', 119.00, 8, 6)
    ]
    cursor.executemany(
        """
        INSERT INTO public.products_py (product_name, description, price, quantity, category_id)
        VALUES (%s, %s, %s, %s, %s)
        """,
        products
    )

    connection.commit()
    print("Values inserted into tables successfully!")

except (Exception, psycopg2.Error) as error:
    print("Error", error)
    connection.rollback()

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")