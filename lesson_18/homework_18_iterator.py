print(f'Реалізуйте ітератор для зворотного виведення елементів списку.')
class ReverseIterator:
    def __init__(self, list):
        self.list = list
        self.index = len(list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.list[self.index]



for k in ReverseIterator([1, 2, 3, 4, 5]):
    print(k)

print("-"*80)
print(f'Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.')

class EvenIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        result = self.current
        self.current += 2
        return result



for num in EvenIterator(10):
    print(num)