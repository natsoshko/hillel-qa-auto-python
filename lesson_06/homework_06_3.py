lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

# variant 1 via type and loop
lst2_v1 = []
for i in lst1:
    if type(i) is str:
        lst2_v1.append(i)
print("variant 1:", lst2_v1)

# variant 2 via isinstance and loop
lst2_v2 = []
for j in lst1:
    if isinstance(j, str):
        lst2_v2.append(j)
print("variant 2:", lst2_v1)

# variant 3 via comprehension
lst2_v3 = [k for k in lst1 if isinstance(k, str)]
print("variant 3:", lst2_v3)