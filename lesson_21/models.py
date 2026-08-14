import enum
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Enum

Base = declarative_base()

class StudentStatus(enum.Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(50), nullable=False)
    status = Column(Enum(StudentStatus), nullable=False, default=StudentStatus.ACTIVE)

    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self):
        return (f"Student:"
            f"id={self.id}, "
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}', "
            f"email='{self.email}')",
            f"phone='{self.phone}', "
            f"status='{self.status}'"
        )

    def __str__(self):
        return f"Student with id = {self.id}: {self.first_name} {self.last_name}, {self.email}, {self.phone}"

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")

    def __repr__(self):
        return (f"Course:"
            f"id={self.id}', "
            f"name='{self.name}', "
            f"description='{self.description}'"
        )

    def __str__(self):
        return f"Course with id = {self.id}: {self.name}, {self.description}"

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)

    course = relationship("Course", back_populates="enrollments")
    student = relationship("Student", back_populates="enrollments")

    def __repr__(self):
        return (
            f"Enrollment("
            f"id={self.id}, "
            f"student_id={self.student_id}, "
            f"course_id={self.course_id})"
        )



