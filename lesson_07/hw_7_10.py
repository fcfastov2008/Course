#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими
#Варіант №1

my_area1 = ['1', '2', 3, True,'7',11, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
my_area2 = []
def change_area_1(*new_area):
    for num in new_area:
        if isinstance(num,str):
            my_area2.append(num)
    return print(f'Ліст містить лише змінні типу стрінг:{my_area2}')
change_area_1(*my_area1)

