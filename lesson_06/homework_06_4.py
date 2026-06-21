# variant 1 via loop
print("# variant 1 via loop")
num_list_v1 = [3,4,10,9,3,6]
even_list = []
sum_v1 = 0
for num1 in num_list_v1:
    if num1 % 2 == 0:
        sum_v1 += num1
        even_list.append(num1)
print(f"sum of even numbers {even_list} = {sum_v1}")
print()

# variant 2 via comprehension
print("# variant 2 via comprehension")
num_list_v2 = [3,4,10,9,3,6]
result = sum(num2 for num2 in num_list_v2 if num2 % 2 == 0)
print("sum of even numbers:", result)