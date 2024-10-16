# Cумма усіх парних чисел в цьому листі
# Варыант №1
my_range = range(1,45)
list_my_range = list(my_range)

def sum_par_numbers(*numbers):
    suma = 0
    for number in numbers:
        if number % 2 ==0 :
            suma = suma + number
    return print(f'Сума всіх парних чисел у списку: {suma}')


sum_par_numbers(*list_my_range)

print("------------------------------------------------")

#Варіант №2
def sum_par_numbers_2(*numbers):
    sum_number = sum(number for number in numbers if number % 2 == 0)
    return print(f'Сума всіх парних чисел у списку: {sum_number}')

sum_par_numbers_2(*list_my_range)