

def filter_even_numbers(*lst):
    even_numbers = []
    for num in lst:
        if not isinstance(num, int):
            raise TypeError(f'Only integers are allowed, but got {type(num)} for {num}')
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers



def triangle_area(a, b, c):
    for side in (a, b, c):
        if not isinstance(side, (int, float)):
            raise TypeError(f'Sides must be numbers, you provided {type(side)} for {side}')

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError(f'Sides must be positive, you provided: {a}, {b}, {c}')

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle')

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area



def arithmetic_average(*numbers):
    if len(numbers) == 0:
        raise ZeroDivisionError(f'Помилка ділення на нуль: {len(numbers)}')
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError(f'Only int allowed, you provided {type(num)} for {num}')
    return sum(numbers) / len(numbers)


def find_longest_word(word_list):

    if not isinstance(word_list, list):
        raise TypeError(f"Expected list but received {type(word_list)}")

    for word in word_list:
        if not isinstance(word, str):
            raise ValueError(f"The list should contain only text, but it was found {type(word)}")

    if not word_list:
        return None

    longest_word = max(word_list, key=len)
    return longest_word

def unique_id_arg(user_input):

    if not isinstance(user_input, str):
        raise TypeError(f"A string was expected but received {type(user_input)}")

    unique_ids = user_input.split()

    if len(set(unique_ids)) > 10:
        rez = "True"
    else:
        rez = "False"

    return rez

