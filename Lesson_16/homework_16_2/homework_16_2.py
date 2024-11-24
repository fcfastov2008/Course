from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, side1_length,side2_lenght):
        self.__side1_length = side1_length
        self.__side2_lenght = side2_lenght

    def area(self):
        return self.__side1_length * self.__side2_lenght

    def perimeter(self):
        return (self.__side1_length + self.__side2_lenght) * 2

class Triangle(Figure):
    def __init__(self, side_lenght):
        self.__side_lenght = side_lenght

    def area(self):
        return (3**0.5 / 4) * (self.__side_lenght**2)

    def perimeter(self):
        return self.__side_lenght * 3

class Parallelepiped(Figure):
    def __init__(self, side1_lenght,side2_lenght,side3_lenght):

        self.__side1_lenght = side1_lenght
        self.__side2_lenght = side2_lenght
        self.__side3_lenght = side3_lenght

    def area(self):
        return ((self.__side1_lenght * self.__side2_lenght) + (self.__side2_lenght * self.__side3_lenght) + (self.__side1_lenght * self.__side3_lenght)) * 2
    def perimeter(self):
        return (self.__side1_lenght + self.__side2_lenght + self.__side3_lenght) * 4

area_perimetr = ["Rectangle", "Triangle","Parallelepiped"]

for k in area_perimetr:
    if k == "Rectangle":
        rectangle = Rectangle(5,10)
    elif k == "Triangle":
        triangle = Triangle(12)
    elif k == "Parallelepiped":
        parall = Parallelepiped(7,8,9)





print(f'Площа прямокутника: {rectangle.area()} та Периметр прямокутника: {rectangle.perimeter()}')
print(f'Площа трикутника: {triangle.area()} та Периметр трикутника: {triangle.perimeter()}')
print(f'Площа паралелепіпеда: {parall.area()} та Периметр паралелепіпеда: {parall.perimeter()}')