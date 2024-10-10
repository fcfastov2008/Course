# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

#Варіант №1

my_lst1 = ['1', '2', 3, True,'7',11, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
my_list2 = []
for num in my_lst1:
    if isinstance(num,str):
        my_list2.append(num)

print(f'Ліст містить лише змінні типу стрінг:{my_list2}')

#Варіант №2

my_list3 = [k for k in my_lst1 if isinstance(k,str)]
print(f'Ліст містить лише змінні типу стрінг:{my_list3}')