
#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True,
# інакше - False. Строку отримати за допомогою функції input()
# Варіант №1
my_list = input("Введіть рядок: ")
#print(my_list_1)
unique_ids = []
for num in my_list:
    if num in unique_ids:
       continue
    else:
        unique_ids.append(num)
print(f'Унікальні символи в строці:{unique_ids}')
if len(unique_ids) > 10 :
    print("True")
else:
    print("False")

# Варіант №2

user_input = input("Введіть рядок: ")

unique_ids = [num for num in user_input]

if len(set(unique_ids)) > 10:
    print(True)
else:
    print(False)
