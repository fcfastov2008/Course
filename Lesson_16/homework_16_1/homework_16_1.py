class Employee:
    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department):
        Employee.__init__(self,name, salary)
        self.department = department




class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self,name, salary)
        self.programming_language = programming_language




class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):

        Employee.__init__(self, name, salary)
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size





employee = Employee("Myke Tyson", 500000)
manager = Manager("James Lebron", 8000000, "NBA")
developer = Developer("Bob Dilan", 7000000, "Java")
team_lead = TeamLead("Dima Malytskyi", 950000, "QA", "Python", 5)
