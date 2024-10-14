#Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
# First variant
def in_reverse_order(*words):
    return print (f'Рядок  у зворотному порядку: {my_row[::-1]}')
my_row = ["Power","Ira","dima","Vladimir","Anton","Alex"]
in_reverse_order(*my_row)

print("--------------------------------------------------------------")
# Second_variant
def reverse_stirng(words):
    return words[::-1]
input_words = "Hello everybody anywhere"
print (f'Рядок  у зворотному порядку: { reverse_stirng(input_words)}')

