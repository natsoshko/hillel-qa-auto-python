from dbconnection import engine, get_session
from models import Base
from data_tables import fill_students, fill_courses, fill_enrollments

# print(Base.metadata.tables.keys())
Base.metadata.create_all(engine)
session = get_session()

try:
    fill_students(session)
    fill_courses(session)
    fill_enrollments(session)
finally:
    session.close()