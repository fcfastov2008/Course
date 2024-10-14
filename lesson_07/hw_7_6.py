# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    # Перевіряємо, чи str2 є підрядком str1 за допомогою методу find
    index = str1.find(str2)
    return index


str1 = "Hello Denys!"
str2 = "Denys"
print(find_substring(str1, str2))

str1 = "The weather it rain today"
str2 = "dog"
print(find_substring(str1, str2))