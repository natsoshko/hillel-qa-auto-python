# 1 - генератор, який повертає послідовність парних чисел від 0 до N
def func_even_numbers(max_number):
    for i in range(max_number + 1):
        if i % 2 == 0:
            yield i

for num in func_even_numbers(10):
    print(num)

print("-"*25)

# 2 - генератор, який генерує послідовність Фібоначчі до певного числа N
def func_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in func_fibonacci(100):
    print(num)

print("-"*25)

# 3 - ітератор для зворотного виведення елементів списку
class IteratorReverseElements:
    def __init__(self, list_elems):
        self.list_elems = list_elems
        self.index = len(list_elems)

    def __iter__(self):
        return self

    def __next__(self):
        # print("begin:", self.index)
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        # print("end:", self.index)
        return self.list_elems[self.index]

list_num = [10, 20, 30, 40, 50]
for item in IteratorReverseElements(list_num):
    print(item)

print("-"*25)

# 4 - ітератор, який повертає всі парні числа в діапазоні від 0 до N
class IteratorEvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

for num in IteratorEvenNumbers(10):
    print(num)

print("-"*25)

# 5 - декоратор, який логує аргументи та результати викликаної функції
def func_arg_logging(func):
    def wrapper(*args, **kwargs):
        print("Called function:", func.__name__)
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper

@func_arg_logging
def func_add(a, b, c):
    return a + b + c

@func_arg_logging
def func_subtract(a, b):
    return a - b

func_add(5, 7, 3)
func_subtract(15, 7)
print("-"*25)

# 6 - декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції
def func_exception(func):
    def wrapper(a, b):
        try:
            print(f"Arguments: {a}, {b}")
            return func(a, b)
        except Exception as error:
            print(f"Error: {error}")
            return "No result"
    return wrapper

@func_exception
def func_divide(a, b):
    return a / b

print("Result:", func_divide(10, 2))
print("Result:",func_divide(10, 0))