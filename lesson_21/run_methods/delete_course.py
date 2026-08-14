from faker import Faker
from lesson_21.dbconnection import get_session
from lesson_21.operations import delete_course

session = get_session()

try:
    delete_course(
        session,
        course_id = 12
    )

finally:
    session.close()