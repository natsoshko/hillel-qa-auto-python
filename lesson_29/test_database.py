from db_connection import get_dbconnection

def create_users_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)

def test_db_connection():
    connection = get_dbconnection()
    assert connection is not None
    connection.close()

def test_insert_user():
    connection = get_dbconnection()
    cursor = connection.cursor()

    create_users_table(cursor)
    connection.commit()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", ("Test User", "insert@example.com"))
    user_id = cursor.fetchone()[0]
    connection.commit()
    assert user_id is not None
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()

def test_select_user():
    connection = get_dbconnection()
    cursor = connection.cursor()

    create_users_table(cursor)
    connection.commit()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", ("Test User", "select@example.com"))
    user_id = cursor.fetchone()[0]
    connection.commit()
    cursor.execute("SELECT name, email FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    assert user == ("Test User", "select@example.com")
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()

def test_update_user():
    connection = get_dbconnection()
    cursor = connection.cursor()

    create_users_table(cursor)
    connection.commit()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", ("Test User", "update@example.com"))
    user_id = cursor.fetchone()[0]
    connection.commit()
    cursor.execute("UPDATE users SET name = %s WHERE id = %s", ("Updated User", user_id))
    connection.commit()
    cursor.execute("SELECT name FROM users WHERE id = %s", (user_id,))
    assert cursor.fetchone()[0] == "Updated User"
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()

def test_delete_user():
    connection = get_dbconnection()
    cursor = connection.cursor()

    create_users_table(cursor)
    connection.commit()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", ("Test User", "delete@example.com"))
    user_id = cursor.fetchone()[0]
    connection.commit()
    cursor.execute( "DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )
    assert cursor.fetchone() is None
    cursor.close()
    connection.close()