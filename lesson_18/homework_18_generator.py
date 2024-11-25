print("Напишіть генератор, який повертає послідовність парних чисел від 0 до N")



def even_numbers(N):
    for num in range(0, N + 1, 2):
        yield num


for number in even_numbers(10):
    print(number)

print("-"*80)
print(f'Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.')

#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci(N):

    a, b = 0, 1

    while a <= N :

        yield  a
        a,b = b, a + b

for num in fibonacci(10):
    print(num)