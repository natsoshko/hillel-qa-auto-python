from faker import Faker
from lesson_21.dbconnection import get_session
from lesson_21.operations import delete_student

session = get_session()

try:
    delete_student(
        session,
        student_id = 26
    )

finally:
    session.close()