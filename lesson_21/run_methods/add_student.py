from faker import Faker
from lesson_21.dbconnection import get_session
from lesson_21.operations import add_student

session = get_session()

try:
    faker = Faker()
    student = add_student(session,faker.first_name(), faker.last_name(), faker.email(), faker.phone_number())
    print(student)

finally:
    session.close()