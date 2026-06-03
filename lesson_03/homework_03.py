alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said '
                       'the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)
print()
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436402
area_azov_sea = 37800

print(f"area_black_sea = {area_black_sea} km2, area_azov_sea = {area_azov_sea} km2")
print("total area = area_black_sea + area_azov_sea =", area_black_sea + area_azov_sea, "km2")
print()

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_products = 375291
first_second_storehouse = 250449
second_third_storehouse = 222950

#version 1 - calculate via total_products
third_storehouse = total_products - first_second_storehouse
first_storehouse_v1 = total_products - second_third_storehouse
second_storehouse_v1 = total_products - (first_storehouse_v1 + third_storehouse)

print("version1 - calculate via total_products:")
print("first storehouse: ", first_storehouse_v1)
print("second storehouse: ", second_storehouse_v1)
print("third storehouse: ", third_storehouse)
print()

#version 2 - calculate via variables
second_storehouse_v2 = second_third_storehouse - third_storehouse
first_storehouse_v2 = first_second_storehouse - second_storehouse_v2

print("version2 - calculate via variables:")
print("first storehouse: ", first_storehouse_v2)
print("second storehouse: ", second_storehouse_v2)
print("third storehouse: ", third_storehouse)
print()

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
months = 18
computer_price = monthly_payment * months
print("computer price = monthly_payment * months =", monthly_payment, "*", months, "=", computer_price, "UAH")
print()

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("remainder of the division:")
print("8019 : 8 => 8019 % 8 = ", (8019 % 8))
print("9907 : 9 => 9907 % 9 = ", (9907 % 9))
print("2789 : 5 => 2789 % 5 = ", (2789 % 5))
print("7248 : 6 => 7248 % 6 = ", (7248 % 6))
print("7128 : 5 => 7128 % 5 = ", (7128 % 5))
print("19224 : 9 => 19224 % 9 = ", (19224 % 9))
print()

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
orders_list = """List of orders:
- pizza big: 4
- pizza middle: 2
- juice: 4
- cake: 1
- water: 3
"""
pizza_big = 4 * 274
pizza_middle = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21

print(orders_list)
print("total cost = pizza big + pizza middle + juice + cake + water =", pizza_big + pizza_middle + juice + cake + water)
#or
detail_text = (f"total cost = pizza big + pizza middle + juice + cake + water = "
               f"{pizza_big} + {pizza_middle} + {juice} + {cake} + {water}")
total_cost = pizza_big + pizza_middle + juice + cake + water
print(detail_text, "=", total_cost)
print()

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
one_page_max = 8

pages_v1 = all_photos // one_page_max
pages_v2 = int(all_photos / one_page_max)

print("max pages =", pages_v1)
print("max pages =", pages_v2)
print()

#another detail decision
list_pages = [1, 2, 3, 4, 5, 6, 7, 8]
for page in list_pages:
    print("for photos on page =", page, "pages =", all_photos//page)

print()

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
tank_volume = 48
spending_unit = 9   # every 100 km

total_fuel = distance // 100 * spending_unit
refueling_times_empty = total_fuel // tank_volume
refueling_times_full = total_fuel // tank_volume - 1
print("total fuel =", total_fuel)
print("refueling times if tank is completely empty before trip =", refueling_times_empty)
print("refueling times if tank is full before trip =", refueling_times_full)

