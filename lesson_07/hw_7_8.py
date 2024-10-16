# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
user_input = input("Введіть рядок: ")
def unique_id_arg(string):
    unique_ids = [num for num in user_input]
    if len(set(unique_ids)) > 10:
        rez = "True"
    else:
        rez = "False"
    return print(f'Результат підрахунку унікальних адресів: {rez}')

unique_id_arg(user_input)
