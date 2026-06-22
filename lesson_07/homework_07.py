# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("# task 1")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

base_number = int(input("Enter the number: "))
multiplication_table(base_number)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print()

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("# task 2")
def sum_of_digits(digit1, digit2):
    result = digit1 + digit2
    if result.is_integer():
        return int(result)
    else:
        return result

# можна використати тип int, але тоді не зможемо обчислювати числа з плаваючою точкою.
# тому я використовую тип float
base_number1 = float(input("Enter number1: "))
base_number2 = float(input("Enter number2: "))
print("Sum of 2 digits =", sum_of_digits(base_number1, base_number2))
print()


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("# task 3")
def average_of_numbers(numbers):
    if len(numbers) == 0:
        return 0 # raise ValueError("List is empty")
    return sum(numbers) / len(numbers)

string_numbers = input("Enter numbers separated by a space: ").split()
# list_numbers = [int(x) for x in string_numbers]
list_numbers = list(map(int, string_numbers))
# print(string_numbers)
# print(list_numbers)
print("Average of numbers:", average_of_numbers(list_numbers))
print()


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("# task 4")
def reverse_func(source_str):
    # return "".join(reversed(source_str))
    return source_str[::-1]

string_text_v1 = input("Enter any string: ")
print("original text:", string_text_v1)
print("reverse text:", reverse_func(string_text_v1))
print()


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("# task 5")
def func_max_word(source_text):
    if len(source_text) == 0:
        return 0

    # variant 1
    # max_len_word = ""
    # for word in source_text:
    #     if len(word) > len(max_len_word):
    #         max_len_word = word
    # return max_len_word

    # variant 2
    # return max(source_text, key=len)

    # variant 3 - if the string has multiple words with the same maximum length
    max_len_word = max(source_text, key=len)
    max_len = len(max_len_word)
    return [word for word in source_text if len(word) == max_len]

string_text_v2 = input("Enter any string: ").split()
print("original text:", string_text_v2)
print("max words:", func_max_word(string_text_v2))
print()


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("# task 6")
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1
print()


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7 - from homework 06.4
print("# task 7")
def sum_of_even_numbers(numbers):
    return sum(num for num in num_list_v2 if num % 2 == 0)

num_list_v2 = [3,4,10,9,3,6]
print("sum of even numbers:", sum_of_even_numbers(num_list_v2))


# task 8 - from homework 03 (task 06)
print("# task 8")
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def func_computer_price(payment, mon):
    return payment * mon

monthly_payment = 1179
months = 18
print("computer price = monthly_payment * months =", monthly_payment, "*", months, "=", func_computer_price(monthly_payment, months), "UAH")
print()


# task 9 - from homework 05 (task 01-02)
print("# task 9")
people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

print("# 1 - Add your new record of the beginning of the given list")
def func_insert_row(source, added_row):
    source.insert(0, added_row)
    return source

new_record = ('Jennifer', 'Lawrence', 35, 'Actress', 'Louisville')
people_records = func_insert_row(people_records, new_record)
for person in people_records:
    print(person)
print()

print("# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result")
def func_swap_elements(source_record):
    source_record[1], source_record[5] = source_record[5], source_record[1]
    return source_record

people_records = func_swap_elements(people_records)
for person in people_records:
    print(person)
print()


# task 10 - from homework 05 (task 03)
print("# task 10")
print("# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result")

def func_check_age(source_records, ind_records):
    result = []
    is_age_more_30 = False
    for i in ind_records:
        if source_records[i][2] >= 30:
            is_age_more_30 = True
            result.append(f"person {i}: {source_records[i]}, age >= 30?: {is_age_more_30}")
            #print(f"person {i}: {source_records[i]}, age >= 30?: {is_age_more_30}")
        else:
            is_age_more_30 = False
            result.append(f"person {i}: {source_records[i]}, age >= 30?: {is_age_more_30}")
            #print(f"person {i}: {source_records[i]}, age >= 30?: {is_age_more_30}")
    return result

records_indexes = [6, 10, 13]
dest_records = func_check_age(people_records, records_indexes)
print(*dest_records, sep="\n")
print()
