
def sum_of_numbers_in_string(my_list):

    try:
        numbers = my_list.split(',')
        suma = 0
        for num in numbers:
           suma = suma + int(num)
        return suma

    except ValueError:
        return "Не можу це зробити!"


array_of_strings = ["1,2,3,4", "1,2,3,4,50", "dron1,2,3", "4,3,5","rom34" ]


for k in array_of_strings:
    result = sum_of_numbers_in_string(k)
    print(result)



