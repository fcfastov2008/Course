# task 01 == Виправте синтаксичні помилки
#print("Hello", end = " ")
#    print("world!")

# task01 Правильний варіант

print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
#hello = "Hello"
#world = "world"
#if True:
#print(f"{hello} {world}!")

# task02 Правильний варіант

hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
#for letter in "Hello world!":
#    print()

# task03 Правильний варіант

for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
#apples = 2
#banana = x

# task04 Правильний варіант

apples = 2
x = apples * 4
banana = x
print('Кількість бананів :',banana)

# Чи так

apples = 2
banana = apples * 4
print('Кількість бананів :',banana)

# task 05 == виправте назви змінних
#1_storona = 1
#?torona_2 = 2
#сторона_3 = 3
#$torona_4 = 4

# task05 Правильний варіант

storona_1 = 1
storona_2 = 2
сторона_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
#perimetery = ? + ? + ? + ?
#print()

# task06 Правильний варіант

storona_1 = 1
storona_2 = 2
сторона_3 = 3
storona_4 = 4
perimetery = storona_1 + storona_2 + сторона_3 + storona_4
print('Периметр фігури :',perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
# У саду посадили 4 яблуні
apples = 4
# Груш на 5 більше, ніж яблунь, отже, груш:
pear = apples + 5
# Слив на 2 менше, ніж груш, отже, слив:
plum = pear -2
# Тепер обчислимо загальну кількість дерев в саду:
all_tree_in_the_garden = apples + pear + plum
print('Загальна кількість дерев в саду :', all_tree_in_the_garden,'дерев' )


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
#До обіду температура була на 5 градусів вище нуля, тобто +5°C.

first_temp = 5

#Після обіду температура опустилася на 10 градусів:

second_temp = first_temp - 10

#Надвечір потепліло на 4 градуси:

final_temp = second_temp + 4
print('Температура надвечір:',final_temp,'градусів')

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
#У театральному гуртку 24 хлопчики, а дівчаток вдвічі менше, тобто:
kol_boy = 24
kol_girl = kol_boy / 2
#1 хлопчик захворів, тому хлопчиків, які прийшли, стало:
kol_boy_comming = kol_boy - 1
kol_girl_comming = kol_girl -2
#Тепер обчислимо загальну кількість дітей, які прийшли до гуртка:

kol_all_children_comming = int(kol_boy_comming + kol_girl_comming)
print('Загальна кількість дітей, які прийшли до гуртка :',kol_all_children_comming,'дитини')

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
#Перша книжка коштує 8 грн.

first_book = 8

#Друга книжка на 2 грн дорожча, тому її ціна:

second_book = first_book + 2

#Третя книжка коштує як половина вартості першої та другої разом:

third_book =  (first_book + second_book) / 2

#Тепер знайдемо загальну вартість усіх трьох книг:

all_book = first_book + second_book + third_book

print('Вартість  усіх книг, якщо купувати по одному примірнику : ' , all_book, 'грн')