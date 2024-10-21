import unittest


from test_functions import arithmetic_average,filter_even_numbers,triangle_area,find_longest_word,unique_id_arg

class FactorialNegativeTest(unittest.TestCase):

    # Тести для виччеслення середьного арефметичного

    def test_zero_numbers(self):
        with self.assertRaises(ZeroDivisionError) as context:
            arithmetic_average()
        self.assertEqual(str(context.exception), 'Помилка ділення на нуль: 0')


    def test_invalid_type(self):

        with self.assertRaises(TypeError) as context:
            arithmetic_average('string',2,3,4)
        self.assertEqual(str(context.exception), "Only int allowed, you provided <class 'str'> for string")
        with self.assertRaises(TypeError) as context:
            arithmetic_average(2, 2, 3, 4.5)
        self.assertEqual(str(context.exception), "Only int allowed, you provided <class 'float'> for 4.5")

    # Тести для знаходження парних чисел

    def test_invalid_filter_even(self):
        with self.assertRaises(TypeError) as context:
            filter_even_numbers(8, "string", 10)

        self.assertEqual(str(context.exception), "Only integers are allowed, but got <class 'str'> for string")

    def test_negative_or_zero_sides(self):
        with self.assertRaises(ValueError) as context:
            triangle_area(3, 0, 5)
        self.assertEqual(str(context.exception), "Sides must be positive, you provided: 3, 0, 5")

    def test_type_error(self):
        with self.assertRaises(TypeError) as context:
            triangle_area(3, 'five', 5)
        self.assertEqual(str(context.exception), "Sides must be numbers, you provided <class 'str'> for five")

    # Тести для вичеслення площі трикутника

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError) as context:
            triangle_area(1, 2, 3)
        self.assertEqual(str(context.exception), "The given sides do not form a valid triangle")

    # Тести для знаходження найдовшого слова

    def test_non_longest_word(self):

        with self.assertRaises(TypeError) as context:
            find_longest_word("кіт, велосипед, дерево")
        self.assertEqual(str(context.exception), "Expected list but received <class 'str'>")



    def test_invalid_longest_word(self):
        words = ["кіт", "велосипед", 123, "автомобіль"]
        with self.assertRaises(ValueError) as context:
            find_longest_word(words)
        self.assertEqual(str(context.exception), "The list should contain only text, but it was found <class 'int'>")

    # Тести для підрахунку кількості унікальних символів в строці.
    # Якщо їх більше 10 - вивести в консоль True, інакше - False.

    def test_non_string_input(self):
        with self.assertRaises(TypeError) as context:
            unique_id_arg(12345)
        self.assertEqual(str(context.exception), "A string was expected but received <class 'int'>")

        with self.assertRaises(TypeError) as context:
            unique_id_arg(["one", "two", "three"])
        self.assertEqual(str(context.exception), "A string was expected but received <class 'list'>")

if __name__ == '__main__':
    unittest.main()