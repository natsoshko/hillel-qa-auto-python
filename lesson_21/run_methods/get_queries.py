from lesson_21.dbconnection import get_session
from lesson_21.operations import get_students_by_course, get_courses_by_student, get_all_students, get_all_courses

session = get_session()
try:
    students = get_all_students(session)
    for student in students:
        print(student)

    print("="*80)

    courses = get_all_courses(session)
    for course in courses:
        print(course)

    print("="*80)

    search_course_id = 8
    students = get_students_by_course(session, course_id = search_course_id)
    print(f"Students on course {search_course_id}:")
    for student in students:
        print(student)

    print("="*80)

    search_student_id = 25
    courses = get_courses_by_student(session, student_id = search_student_id)
    print(f"Courses of student {search_student_id}:")
    for course in courses:
        print(course)

finally:
    session.close()