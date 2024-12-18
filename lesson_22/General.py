from models import Student, Curse, StudentCourse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_base import Base
from faker import Faker
import random

PS_SQL = "postgresql://postgres:qwerty12345@localhost:5433/shopcars"
engine = create_engine(PS_SQL)

fake = Faker()


Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)


list_courses = ["Mathematics","Physics","Chemistry","Biology","Literature"]

it_courses = [Curse(name_curse=f"{list}") for list in list_courses]
session.add_all(it_courses)
session.commit()

it_students = [Student(name=fake.name()) for _ in range(20)]
session.add_all(it_students)
session.commit()


student_course_relations = []
for student in it_students:

    it_relate = random.sample(it_courses, random.randint(1, 5))
    for course in it_relate:
        student_course_relations.append(StudentCourse(student=student, curse=course))

# Додавання зв'язків до бази даних
session.add_all(student_course_relations)

session.commit()

student = session.query(Student).first()
print(f"Студент: {student.name}")
print("Зареєстровані курси:")
for relation in student.student_courses:
    print(f"- {relation.curse.name_curse}")

print("------------------------------------------------------------------")

course = session.query(Curse).filter_by(name_curse='Chemistry').first()
print(f"Курс: {course.name_curse}")
print("Зареєстровані студенти:")
for relation in course.student_courses:
    print(f"- {relation.student.name}")

print("------------------------------------------------------------------")
course = session.query(Curse).filter_by(id=4).first()
print(f"Старий Курс: {course.name_curse}")
course = session.query(Curse).filter_by(id=4).first()
course.name_curse = "Atletics"
session.commit()
course = session.query(Curse).filter_by(id=4).first()
print(f"Новий Курс: {course.name_curse}")
session.commit()

print("------------------------------------------------------------------")
student = session.query(Student).filter_by(id=4).first()
print(f"Старий Студент: {student.name}")
student = session.query(Student).filter_by(id=4).first()
student.name = "Dmytro Malytskyi"
student = session.query(Student).filter_by(id=4).first()
print(f"Новий Студент: {student.name}")

session.query(StudentCourse).delete()
session.commit()

session.query(Student).delete()
session.commit()

session.query(Curse).delete()
session.commit()