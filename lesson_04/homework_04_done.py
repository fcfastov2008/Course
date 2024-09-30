from itertools import count
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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

new_adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f'Текст де замінено кінець абзацу на пробіл : \n{new_adwentures_of_tom_sawer} ')

print('-----------------------------------------')

# task 02 ==
""" Замініть .... на пробіл
"""

print(f'Текст де замінено .... на пробіл : \n{new_adwentures_of_tom_sawer.replace("...."," ")}')

print('-----------------------------------------')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

print(f'Текст в якому не більше одного пробілу між словами:\n{ ' '.join(new_adwentures_of_tom_sawer.split())}')

print('-----------------------------------------')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(f'Кількість разів коли в тексті зустрічається літера "n" : {adwentures_of_tom_sawer.count('n')}')

print('-----------------------------------------')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
my_words = adwentures_of_tom_sawer.split()
words_count = 0
for word in my_words:
    if len(word) > 0 and word[0].isupper():
        words_count += 1
print(f'Кількість слів у тексті які починається з Великої літери: {words_count}')

print('-----------------------------------------')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# Розбиваємо текст на слова
adwentures_of_tom_sawer.split()
search_words = "Tom"
search_word_index = adwentures_of_tom_sawer.find(search_words)
result_first = adwentures_of_tom_sawer[search_word_index + len(search_words):]
result_second = result_first.find(search_words)
print(f"Слово 'Tom' зустрічається вдруге на позиції: {result_second}")

print('-----------------------------------------')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
if len(adwentures_of_tom_sawer_sentences) >= 4:
    sentence_fourth =adwentures_of_tom_sawer_sentences[3].lower()
    print(f"Четверте речення в нижньому регістрі: \n{sentence_fourth}")

print('-----------------------------------------')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
list_my_sentence = adwentures_of_tom_sawer.split('.')
for sentence in list_my_sentence :
    if sentence.strip().startswith ("By the time"):
        print("Є речення яке починається з 'By the time'")

print('-----------------------------------------')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1]
number_words = len(last_sentence.split())
print(f"Кількість слів в останньому реченні: {number_words}")

print('-----------------------------------------')