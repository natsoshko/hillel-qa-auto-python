# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

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

# 1 - Add your new record of the beginning of the given list
print("# 1 - Add your new record of the beginning of the given list")
new_record = ('Jennifer', 'Lawrence', 35, 'Actress', 'Louisville')
people_records.insert(0, new_record)
for person in people_records:
    print(person)
print()


# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
print("# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result")
# variant 1 - swap using 'temp' parameter
# temp = people_records[1]
# people_records[1] = people_records[5]
# people_records[5] = temp
# for person in people_records:
#   print(person)
# print()

# variant 2 - swap using tuple unpacking
people_records[1], people_records[5] = people_records[5], people_records[1]
for person in people_records:
    print(person)
print()


# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result
print("# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result")

records_indexes = [6, 10, 13]

is_age_more_30 = False
for i in records_indexes:
    if people_records[i][2] >= 30:
      is_age_more_30 = True
      print(f"person {i}: {people_records[i]}, age >= 30?: {is_age_more_30}")
    else:
      is_age_more_30 = False
      print(f"person {i}: {people_records[i]}, age >= 30?: {is_age_more_30}")
print()