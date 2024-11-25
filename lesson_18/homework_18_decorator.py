print(f'Декоратор для логування аргументів і результатів функції')

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Викликається: {func.__name__} з аргументами: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'Результат: {result}')
        return result
    return wrapper




@log_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Dmytro", greeting="Hi")

print("-"*80)

print('Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.')

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError as e:
            print(f"Помилка ділення на нуль: {e}")
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

divide(20, 0)
