from lesson_21.dbconnection import get_session
from lesson_21.models import Student, Course, Enrollment

# ===========================================================
# add student / course
# ===========================================================
def add_student(session, first_name, last_name, email, phone):
    student = Student(
        first_name = first_name,
        last_name = last_name,
        email = email,
        phone = phone
    )
    session.add(student)
    session.commit()
    return student

def add_course(session, name, description):
    course = Course(
        name=name,
        description = description
    )

    session.add(course)
    session.commit()
    return course

# ===========================================================
# get students / courses
# ===========================================================
def get_students_by_course(session, course_id):
    students = session.query(Student).join(Enrollment).filter(Enrollment.course_id == course_id).all()
    return students

def get_courses_by_student(session, student_id):
    courses = session.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id).all()
    return courses

def get_all_students(session):
    return session.query(Student).order_by(Student.id).all()

def get_all_courses(session):
    return session.query(Course).order_by(Course.id).all()

# ===========================================================
# update student / course
# ===========================================================
def update_student(session, student_id, **fields):
    student = session.get(Student, student_id)
    if student is None:
        print(f"Student with id={student_id} not found.")
        # return None

    allowed_fields = {
        "first_name",
        "last_name",
        "email",
        "phone",
        "status"
    }

    for key, value in fields.items():
        if key in allowed_fields:
            setattr(student, key, value)
    session.commit()
    print(f"Student updated: {student}")

def update_course(session, course_id, **fields):
    course = session.get(Course, course_id)
    if course is None:
        print(f"Course with id={course_id} not found.")

    allowed_fields = {
        "name",
        "description"
    }
    for key, value in fields.items():
        if key in allowed_fields:
            setattr(course, key, value)
    session.commit()
    print(f"Course updated: {course}")

# ===========================================================
# delete student / course
# ===========================================================
def delete_student(session, student_id):
    student = session.get(Student, student_id)
    if student is None:
        print(f"Student with id={student_id} not found.")

    session.delete(student)
    session.commit()

def delete_course(session, course_id):
    course = session.get(Course, course_id)
    if course is None:
        print(f"Course id={course_id} not found.")
    session.delete(course)
    session.commit()

# ===========================================================
# enroll / unenroll
# ===========================================================
def enroll_student_to_course(session, student_id, course_id):
    student = session.get(Student, student_id)
    course = session.get(Course, course_id)
    if student is None or course is None:
        print(f"Error: student with id={student_id} or course with id={course_id} not found.")

    already_enrolled = session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    if already_enrolled:
        print(f"Student {student.first_name} {student.last_name} is already enrolled in course '{course.title}'.")

    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    session.add(enrollment)
    session.commit()
    print(f"Student {student_id} enrolled in course {course_id}.")

def unenroll_student_from_course(session, student_id, course_id):
    enrollment = session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    if enrollment is None:
        print(f"Student {student_id} is not enrolled in course {course_id}.")

    session.delete(enrollment)
    session.commit()
    print(f"Student {student_id} unenrolled from course {course_id}.")