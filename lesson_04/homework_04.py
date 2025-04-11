import re
adwentures_of_tom_sawer = """\
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
print(f"Original text: ",adwentures_of_tom_sawer)


##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f"Task 1: ",adwentures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f"Task 2: ",adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
words = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(words)
print(f"Task 3: ", adwentures_of_tom_sawer)
#adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)
#print(f"Task 3: ",adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_letter_count = adwentures_of_tom_sawer.count("h")
print(f"Task 4. Літера 'h' зустрічається {h_letter_count} разів ")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
number_title = 0
for letter in adwentures_of_tom_sawer:
    if letter.istitle():
        number_title += 1

print(f"Task 5. Кількість слів, що починаються з великої літери: {number_title} ")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_entry = adwentures_of_tom_sawer.find("Tom")
second_entry = adwentures_of_tom_sawer.find ("Tom", first_entry + 1)
print(f"Task 6. Позиція, на якій слово Tom зустрічається вдруге: {second_entry} ")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = re.split(r'[.]\s+', adwentures_of_tom_sawer)
print(f"Task 7.{adwentures_of_tom_sawer_sentences}")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentense_4 = adwentures_of_tom_sawer_sentences[3].lower()
print(f"Task 7. Четверте речення: {sentense_4}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentense in adwentures_of_tom_sawer_sentences:
    if sentense.startswith("By the time"):
        print("Так, є речення, що починається з 'By the time':")
        print(sentense)
        break


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_in_last_sentence = last_sentence.split()
word_count = len(words_in_last_sentence)

print(f"Кількість слів в останньому реченні: {word_count}")

print(f"----------------Текст, поділений на фізичні лінії: -------------")
for sentence in adwentures_of_tom_sawer_sentences:
    print(sentence + ".")