from lesson_21.dbconnection import get_session
from lesson_21.operations import update_course

session = get_session()

try:
    update_course(
        session,
        course_id = 5,
        name = "SQL Fundamentals",
        description = "Learn SQL queries, joins, and database basics"
    )

finally:
    session.close()