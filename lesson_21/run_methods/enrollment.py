from lesson_21.dbconnection import get_session
from lesson_21.operations import enroll_student_to_course, unenroll_student_from_course

session = get_session()

try:
    enroll_student_to_course(
        session,
        student_id = 26,
        course_id = 10
    )

    unenroll_student_from_course(
        session,
        student_id = 25,
        course_id = 8
    )

finally:
    session.close()