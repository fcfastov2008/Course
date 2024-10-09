#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

# Варіант №1

suma = 0
for number in range (1,30):
    if number % 2 ==0 :
       suma = suma + number
print(f'Сума всіх парних чисел у списку: {suma}')

# Варіант №2

sum_number = sum(num for num in range(1,30) if num % 2 == 0)

print(f'Сума всіх парних чисел у списку: {sum_number}')




