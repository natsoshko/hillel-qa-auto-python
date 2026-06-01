# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")
print()

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)
print()

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = 4 * apples
print("apples:", apples)
print("bananas:", bananas)
print()

## task 04 - another version
"""
apples_2 = int(input("Enter apples number: "))
bananas_2 = 4 * apples_2
print("apples:", apples_2, "bananas:", bananas_2)
print()
"""

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = side_1 + side_2 + side_3 + side_4
print(f"side_1 = {side_1}, side_2 = {side_2}, side3 = {side_3}, side4 = {side_4}")
print("perimeter =", perimeter)
print()



"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples_tree = 4
pears_tree = apples_tree + 5
plums_tree = apples_tree - 2
total_trees = apples_tree + pears_tree + plums_tree
print(f"apples_tree = {apples_tree}, pears_tree = {pears_tree}, plums_tree = {plums_tree}")
print("total_trees =", total_trees)
print()

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_before_lunch = 5
temp_after_lunch = temp_before_lunch - 10
temp_evening = temp_after_lunch + 4
print("Temperature before lunch:", temp_before_lunch)
print("Temperature after lunch:", temp_after_lunch)
print("Temperature in the evening:", temp_evening)
print()

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_total = 24
girls_total = int(boys_total/2)
# girls_total = boys_total//2 - the same
boys_today = boys_total - 1
girls_today = girls_total - 2
children_today = boys_today + girls_today
print(f"Total children = {boys_total + girls_total}: boys total = {boys_total}, girls total = {girls_total}")
#print("Total children:", boys_total + girls_total)
print("Total children today:", children_today)
print()

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
total_cost = first_book + second_book + third_book
print(f"first book = {first_book}, second book = {second_book}, third book = {third_book}")
print("total_cost:", total_cost)
print()
