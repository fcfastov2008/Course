# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_average(*numbers):
    return sum(numbers)/len(list_numbers)

list_numbers = list(range(1,33))
print(f'Cереднє арифметичне списку чисел: {arithmetic_average(*list_numbers)}')
