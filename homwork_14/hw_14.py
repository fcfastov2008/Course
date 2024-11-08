
class Student:
    def __init__(self,firstname,lastname,age,average_value):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.average_value = average_value

    def change_avarege(self,new_avarege):
        self.average_value = new_avarege

    def info_student(self):
        print(f'Firstname and Lastname student: {self.firstname} {self.lastname}\nAge:{self.age}\nAvarage value : {self.average_value}')

my_student = Student("Dmytro","Malytskyi",38,75)

print("Information about student before changes:")
my_student.info_student()
print("-"*80)
my_student.change_avarege(100)
print(f'Information about student after changes:')
my_student.info_student()


