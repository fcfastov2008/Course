from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Curse(Base):
    __tablename__ = 'curses'

    id = Column(Integer, primary_key=True)
    name_curse = Column(String)
    student_courses = relationship("StudentCourse", back_populates="curse")


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    student_courses = relationship("StudentCourse", back_populates="student")

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    curse_id = Column(Integer, ForeignKey('curses.id'))
    student = relationship("Student", back_populates="student_courses")
    curse = relationship("Curse", back_populates="student_courses")
