# function 1
def multiplication_table(number):
    if number <= 0:
        raise ValueError("Number must be greater than 0")

    res = []
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        # print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # res.append(f"{number}x{multiplier}={number * multiplier}")
        res.append(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
    return res

# base_number = int(input("Enter the number: "))
# print(multiplication_table(base_number))
# print()


# function 2
def average_of_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)

# string_numbers = input("Enter numbers separated by a space: ").split()
# list_numbers = list(map(int, string_numbers))
# print("Average of numbers:", average_of_numbers(list_numbers))
# print()


# function 3
def func_computer_price(payment, mon):
    return payment * mon

# monthly_payment = 1179
# months = 18
# print("computer price = monthly_payment * months =", monthly_payment, "*", months, "=", func_computer_price(monthly_payment, months), "UAH")
# print()


# function 4
s_array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def func_sum_array_numbers(s_list):
    array_split = s_list.split(",")
    sum_ = 0
    try:
        for num in array_split:
            sum_ += int(num)
    except ValueError:
        return "Can't do this - not only numbers here!"
    except Exception as e:
        print("Some unexpected error happened")
        print(e)
    return sum_

# for item in s_array:
#     # print(item)
#     print("sum of elements", item, "=", func_sum_array_numbers(item))
