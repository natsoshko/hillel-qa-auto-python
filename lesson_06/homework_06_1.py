from codecs import ignore_errors

user_text = input("Enter your text here:\n")

user_text = user_text.replace(" ", "").lower()

#variant 1 with set collection
print("# variant 1 with set collection:")
print(set(user_text))
if len(set(user_text)) > 10:
    print("Does the text have unique characters > 10?:", True)
else:
    print("Does the text have unique characters > 10?:", False)
print()

#variant 2
print("# variant 2:")
#user_text = user_text.replace(" ", "").lower()
print(user_text)
list_unique = []
dct_duplicates = {}
dct_unique = {}
icount_unique = 0

for char in user_text.strip().lower():
    if char not in list(dct_duplicates.keys()):
        duplicate_number = user_text.count(char)
        if duplicate_number == 1:
            icount_unique += 1
            list_unique.append(char)
        else:
            dct_duplicates.update({char: duplicate_number})

bool_unique_value = False
if icount_unique >= 10:
    bool_unique_value = True
    print(f"Does the text have unique characters > 10?: {bool_unique_value}. And unique numbers = {icount_unique}")
else:
    print(f"Does the text have unique characters > 10?: {bool_unique_value}. And duplicate numbers = {icount_unique}")

print("Unique characters:", list_unique)
print("Duplicate characters:", dct_duplicates)


