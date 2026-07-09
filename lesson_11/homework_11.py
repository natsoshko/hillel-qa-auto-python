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

for item in s_array:
    # print(item)
    print("sum of elements", item, "=", func_sum_array_numbers(item))
