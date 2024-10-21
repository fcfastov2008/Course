import unittest

from test_functions import arithmetic_average,filter_even_numbers, triangle_area, find_longest_word,unique_id_arg

class FactorialPositiveTest(unittest.TestCase):

    # Тести для виччеслення середьного арефметичного
    def test_average_of_positive_numbers(self):
        actual_result = arithmetic_average(1, 2, 3, 4)
        excepted_result = 2.5
        self.assertEqual(excepted_result, actual_result)

    def test_average_of_negative_numbers(self):
        actual_result = arithmetic_average(-1, -2, -3, -4)
        excepted_result = -2.5
        self.assertEqual(excepted_result, actual_result)

    def test_average_of_mixed_numbers(self):
        actual_result = arithmetic_average(1, -1, 1, -1)
        excepted_result = 0
        self.assertEqual(excepted_result, actual_result)

    def test_single_number(self):
        actual_result = arithmetic_average(20)
        excepted_result = 20
        self.assertEqual(excepted_result, actual_result)


    def test_zero_input(self):

        actual_result = arithmetic_average(0,0,0,0)
        excepted_result = 0
        self.assertEqual(excepted_result, actual_result)

    # Тести для знаходження парних чисел

    def test_even_numbers(self):

        actual_result = filter_even_numbers(7, 9, 10, 11)
        excepted_result = [10]
        self.assertEqual(excepted_result, actual_result)

    def test_no_even_numbers(self):

        actual_result = filter_even_numbers(7, 9, 11,13)
        excepted_result = []
        self.assertEqual(excepted_result, actual_result)

    def test_all_even_numbers(self):

        actual_result = filter_even_numbers(2, 4, 6, 8)
        excepted_result = [2, 4, 6, 8]
        self.assertEqual(excepted_result, actual_result)

    def test_empty_even_numbers(self):

        actual_result = filter_even_numbers()
        excepted_result = []
        self.assertEqual(excepted_result, actual_result)

    # Тести для вичеслення площі трикутника
    def test_valid_triangle(self):
        actual_result = triangle_area(3, 4, 5)
        excepted_result = 6.0
        self.assertEqual(excepted_result, actual_result)

    def test_valid_longest_word(self):
        words = ["кіт", "велосипед", "дерево", "автомобіль"]
        self.assertEqual(find_longest_word(words), "автомобіль")

    # Тести для знаходження найдовшого слова
    def test_empty_longest_word(self):
        words = []
        self.assertIsNone(find_longest_word(words))

    def test_single_longest_word(self):
        words = ["автомобіль"]
        self.assertEqual(find_longest_word(words), "автомобіль")

    def test_all_words_same_length(self):
        words = ["кіт", "сон", "лід"]
        self.assertEqual(find_longest_word(words), "кіт")

    # Тести для підрахунку кількості унікальних символів в строці.
    # Якщо їх більше 10 - вивести в консоль True, інакше - False.

    def test_more_than_ten_unique_ids(self):
        input_string = "one two three four five six seven eight nine ten eleven"
        self.assertEqual(unique_id_arg(input_string), "True")

    def test_exactly_ten_unique_ids(self):
        input_string = "one two three four five six seven eight nine ten "
        self.assertEqual(unique_id_arg(input_string), "False")

    def test_less_than_ten_unique_ids(self):
        input_string = "one two three four five"
        self.assertEqual(unique_id_arg(input_string), "False")

    def test_duplicate_ids(self):
        input_string = "one two three one two"
        self.assertEqual(unique_id_arg(input_string), "False")

if __name__ == '__main__':
    unittest.main()