from lesson_21.dbconnection import get_session
from lesson_21.operations import add_course

session = get_session()

try:
    course = add_course(session, "Docker Essentials", "Understand containers and basic Docker commands")
    print(course)

finally:
    session.close()