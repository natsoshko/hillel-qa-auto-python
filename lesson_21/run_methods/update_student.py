from lesson_21.dbconnection import get_session
from lesson_21.operations import update_student

session = get_session()

try:
    update_student(
        session,
        student_id = 1,
        first_name = "Mark",
        email = "mark_333@gmail.com"
    )
finally:
    session.close()