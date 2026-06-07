adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("# task 01")
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")
print(adventures_of_tom_sawer)
print()

# task 02 ==
""" Замініть .... на пробіл
"""
print("# task 02")
# replace with spaces at the beginning and at the end ' .... '
# commented to solve task 03
#adventures_of_tom_sawer = adventures_of_tom_sawer.replace(" .... ", " ")
#print(adventures_of_tom_sawer)

# replace only '....'
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("....", " ")
print(adventures_of_tom_sawer)
print()

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("# task 03")
split_text = adventures_of_tom_sawer.split()
print("split text:", split_text)
adventures_of_tom_sawer = " ".join(split_text)
print("text with only one space:", adventures_of_tom_sawer)
print()

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("# task 04")
print("count of the letter 'h' in the text = ", adventures_of_tom_sawer.count("h"))
print()

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("# task 05")
count = 0

for word in adventures_of_tom_sawer.split():
    if word.istitle():
        count += 1
print("Number of words in the text begin with a capital letter =", count)
print()

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("# task 06")
print("count of Tom =", adventures_of_tom_sawer.count("Tom"))
print(adventures_of_tom_sawer)
print("second word Tom starts from =", adventures_of_tom_sawer.find("Tom", 1), "position")
print()

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("# task 07")
# version 1 with '' as additional item in the list
print("version 1")
adventures_of_tom_sawer_sentences = None
print("adventures_of_tom_sawer_sentences before split:", adventures_of_tom_sawer_sentences)
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split(".")
print("adventures_of_tom_sawer_sentences after split:", adventures_of_tom_sawer_sentences)
print("length adventures_of_tom_sawer_sentences =", len(adventures_of_tom_sawer_sentences))
print()

# version 2 without '' as additional item in the list
print("version 2")
adventures_of_tom_sawer_sentences_v2 = []
for sentence in adventures_of_tom_sawer.split("."):
    if sentence != '':
        adventures_of_tom_sawer_sentences_v2.append(sentence.strip())
print("adventures_of_tom_sawer_sentences after split:", adventures_of_tom_sawer_sentences_v2)
print("length adventures_of_tom_sawer_sentences =", len(adventures_of_tom_sawer_sentences_v2))
print()


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("# task 08")
print("4rd sentence:")
print(adventures_of_tom_sawer_sentences[3].lower().strip())
print()


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("# task 09")
for sentence in adventures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Sentence is found:", sentence)
        break
    print("Invalid sentence:", sentence)
print()

# re-check with another example for myself with 'continue'
# text_search = ["Alex text", "Ben text", "Mark text"]
# for sentence in text_search:
#     if sentence.strip().startswith("Ben"):
#         print("Sentence is found:", sentence)
#         continue
#     print("Invalid sentence:", sentence)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("# task 10")
# use adventures_of_tom_sawer_sentences_v2 here because adventures_of_tom_sawer_sentences - with '' as the last item
last_sentence = adventures_of_tom_sawer_sentences_v2[-1]
print("last sentence:", last_sentence)
print("count of words of last sentence:", len(last_sentence.split()))

#or
print("count of words of last sentence:", len(adventures_of_tom_sawer_sentences_v2[-1].split()))
print()
