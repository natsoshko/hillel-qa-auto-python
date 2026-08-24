import random
from models import Student, Course, Enrollment

def fill_students(session):

    students_data = [
        ("John", "Smith", "john@gmail.com", "+380972581425"),
        ("Anna", "Brown", "anna@gmail.com", "+380975553322"),
        ("Michael", "Wilson", "michael@gmail.com", "+380975553311"),
        ("Emily", "Taylor", "emily@gmail.com", "+380975553300"),
        ("David", "Anderson", "david@gmail.com", "+380975553344"),
        ("Sophia", "Thomas", "sophia@gmail.com", "+380976663300"),
        ("James", "Jackson", "james@gmail.com", "+380976661100"),
        ("Olivia", "White", "olivia@gmail.com", "+380976662200"),
        ("Daniel", "Harris", "daniel@gmail.com", "+380976664400"),
        ("Emma", "Martin", "emma@gmail.com", "+380968883301"),
        ("Alex", "Thompson", "alex@gmail.com", "+380968883302"),
        ("Mia", "Garcia", "mia@gmail.com", "+380968883303"),
        ("William", "Martinez", "william@gmail.com", "+380968883304"),
        ("Isabella", "Robinson", "isabella@gmail.com", "+380968883305"),
        ("Henry", "Clark", "henry@gmail.com", "+380968889988"),
        ("Charlotte", "Rodriguez", "charlotte@gmail.com", "+380968889977"),
        ("Lucas", "Lewis", "lucas@gmail.com", "+380968889966"),
        ("Amelia", "Lee", "amelia@gmail.com", "+380968889955"),
        ("Oliver", "Walker", "oliver@gmail.com", "+380968889944"),
        ("Ella", "Hall", "ella@gmail.com", "+380968889933")
    ]

    for first_name, last_name, email, phone in students_data:
        student = Student(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone
        )
        session.add(student)
    session.commit()
    print(f"{len(students_data)} students added.")


def fill_courses(session):

    courses_data = [
        ("Python Pro", "Advanced Python programming and best practices"),
        ("Claude Code", "AI-assisted coding with Claude"),
        ("Java Basic", "Introduction to Java programming"),
        ("Playwright", "Web automation testing with Playwright"),
        ("SQL", "Database queries and SQL fundamentals"),
        ("QA Manual", "Manual software testing fundamentals"),
        ("QA Automation Python", "Test automation with Python and Pytest")
    ]

    for course_name, course_description in courses_data:
        course = Course(
            name = course_name,
            description = course_description
        )
        session.add(course)
    session.commit()

    print(f"{len(courses_data)} courses added.")

def fill_enrollments(session):

    students = session.query(Student).all()
    courses = session.query(Course).all()
    for student in students:
        course = random.choice(courses)
        enrollment = Enrollment(
            student_id=student.id,
            course_id=course.id
        )
        session.add(enrollment)
    session.commit()

    print("Enrollments created.")