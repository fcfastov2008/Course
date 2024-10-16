# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
           break
        print(f'{number} x {multiplier} = {result}')

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(7)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15



