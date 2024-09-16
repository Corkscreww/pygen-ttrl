"""Модуль 11. Регулярные выражения"""


kk('Hello gnvno!')
A = 1
B = 10

whil A (*values: object, sep: Optional[str]=..., Op)


"""Блок 11.1 Регулярные выражения. Часть 1"""

# frm6_1 = r'7(-\d{3}){2}(-\d{2}){2}'
# frm6_2 = r'8(-\d{3})(-\d{4}){2}'

# regrex_21 = r'beegeek'
# regrex_22 = r'...\....'
# regrex_23 = r'1\d\d'
# regrex_24 = r'\d{3}-\d{3}-\d{4}'

"""Блок 11.2 Регулярные выражения. Часть 2"""

# regrex_16 = r'[a-zA-z]\d{4}'
# regrex_17 = r'[a-z]\d[a-z][A-Z]{2}'
# regrex_18 = r'\d[aeiouy][^b^c^D^F]\S[^A^E^I^O^U^Y][^;]'
# regrex_19 = r'[123][012][12x][03aA][xsu][.,]'
# regrex_20 = r'+7'   # ?????
# regrex_22 = r''  #??????

"""Блок 11.3 Регулярные выражения. Часть 3"""

# regrex_17 = r'[A-Z]{5}\d{4}[A-Z]'
# regrex_18 = r'<!--*?-->'
# regrex_19 = r'[A-Z]{,3}\d{2,8}[A-Z]{3}'
# regrex_20 = r'[A-Z]{1,2}\d[\d|A-Z]'

"""Блок 11.4 Регулярные выражения. Часть 4"""

# regrex_10 = r'[aA]n?'
# regrex_11 = r'\W[A-Z]\W'
# regrex_12 = r'\W[A-Z]*?\W'
# regrex_13 = r'\n*(*)*\n'
# regrex_14 = r'\n\d{2,}[a-z]*[A-Z]*'
# regrex_15 = r'\n[A-Za-z]s\n'
# regrex_16 = r'[(A-Za-z)|(24680)]{40}[(13579)|\s]'
# regrex_17 = r'\n((Mr.)|(Mrs.)|(Ms.)|(Dr.)|(Er.))[A-Za-z]{1,}'
# regrex_18 = r'\n\d{1,2}[A-Za-z]{3,}[.]{1,3}'

"""Блок 11.5 Регулярные выражения. Часть 5"""

# rezrex_5 = '\d{5}(-\d{4})?'
# rezrex_6 = '(\(\d{3}\)|\d{3})(\s|-)\d{3}-\d{4}'
# rezrex_7 = '(bee).*'
# rezrex_12 = '([A-Za-z])\w[A-Z]'

""" Блок 11.6 Модуль re. Часть 1"""

"""№ 9 Телефонные номера"""

# import re

# with open('9/6', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# for number in data:
#     pattern = (r'(?P<area_code>[0-9]{1,3})(?P<sep>[ -])'
#                r'(?P<city_code>[0-9]{1,3})(?P=sep)(?P<number>[0-9]{4,10})')
#     match = re.match(pattern, number.strip())
#     if match:
#         print(f'Код страны: {match.group("area_code")}, Код города: '
#               f'{match.group("city_code")}, Номер: {match.group("number")}')

"""№ 10 Онлайн-школа BEEGEEK"""

# import re

# with open('10/6', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# for number in data:
#     pattern = r'_[0-9]+[A-Za-z]*_?'
#     match = re.fullmatch(pattern, number.strip())
#     print(bool(match))

"""№ 11 Одинаковые слоги"""

# import re

# with open('11/6', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# for number in data:
#     pattern = r'(?P<slog>.*)(?P=slog)'
#     match = re.fullmatch(pattern, number.strip())
#     if match:
#         print(match.group())

"""№ 12 Beegeek"""

# import re

# with open('12/5', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()
#     patbee = r'(bee)'
#     patgeek = r'\bgeek\b'
#     bee, geek = 0, 0

# for string in data:
#     string = string.strip()
#     match = re.search(patbee, string)
#     if match:
#         if re.search(patbee, string[match.end():]):
#             bee +=1
#     if re.search(patgeek, string):
#         geek +=1

# print(bee, geek, sep='\n')

"""№ 13 Популярность"""

# import re

# with open('13/7', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()
#     bg = 'beegeek'

# pat3 = r'^beegeek.*beegeek$'
# pat2 = r'(^beegeek.*)|(.*beegeek$)'
# pat1 = r'beegeek'
# ball = 0

# for string in data:
#     string = string.strip()
#     bal3 = re.search(pat3, string)
#     bal2 = re.search(pat2, string)
#     bal1 = re.search(pat1, string)
#     if bal3:
#         ball += 3
#     elif bal2:
#         ball += 2
#     elif bal1:
#         ball += 1
#     elif string == 'beegeek':
#         ball += 2

# print(ball)

"""№ 19 Уважение"""

# import re
# from re import IGNORECASE, MULTILINE

# text = 'здравствуйте, вы не заняты?'

# pattern = r'^Здравствуйте|^Добрый день|^Доброе утро|^Добрый вечер'
# if re.search(pattern, text, flags=IGNORECASE | MULTILINE):
#     print(True)
# else:
#     print(False)

"""№ 20 Социальные сети"""

# import re
# from re import IGNORECASE

# with open('20/4', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# cnt = 0
# for string in data:
#     string = string.strip()
#     if re.search(r'beegeek', string, flags=IGNORECASE):
#         cnt += 1

# print(cnt)

"""Блок 11.2 Модуль re часть 2"""

"""№ 11 Подслова"""

# import re

# with open('211/1', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# cnt = 0

# text = data[0].strip()
# word = data[1].strip()
# words = re.findall(rf'\w({word})\w', text)

# print(len(words))

"""№ 12 Слова"""

# import re

# with open('212/5', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# cnt = 0

# text = data[0].strip()
# word = data[1].strip()
# words = re.findall(rf'(\W({word})\W)|(^{word}\W)|(\W{word}$)', text)

# print(len(words))

"""№ 13 Одинаковые и разные"""

# import re
# from re import IGNORECASE

# with open('213/1', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# cnt = 0

# word = data[0].strip()[:-2] + '[sz]e'
# text = data[1].strip()

# words = re.findall(rf'\b{word}\b', text,
#                    flags=IGNORECASE)

# print(len(words))

"""№ 14 Одинаковые и разные"""

# import re
# from re import IGNORECASE

# with open('214/3', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# cnt = 0

# word = data[0].strip()[:-2] + 'u?r'
# text = data[1].strip()

# words = re.findall(rf'\b{word}\b', text,
#                    flags=IGNORECASE)

# print(len(words))

"""№ 15 Функция abbreviate()"""

# import re

# def abbreviate(phrase):
#     pattern = r'\b.|[A-Z]'
#     words = re.findall(pattern, phrase)
#     result = ''
#     for word in words:
#         if word.strip():
#             result += word[0].upper()
#     return result

# print(abbreviate('javaScript object notation'))
# print(abbreviate('frequently asked questions'))
# print(abbreviate('JS game sec'))
# print(abbreviate('gaveOver GameStarted happyEnd happyend'))

"""№ 16 HTML"""

# import re
# from re import IGNORECASE

# with open('216/5', encoding='UTF-8') as inp_file:
#     data = inp_file.readlines()

# pattern = r'href="(.*)">(.*)</a>'

# for string in data:
#     htm = re.search(pattern, string)

#     if htm:
#         print(htm.group(1), end=', ')
#         print(htm.group(2))

"""№ 17 HTML           НА ПОТОМ"""

# import re
# from re import IGNORECASE

# with open('217/1', encoding='UTF-8') as inp_file:
#     data = inp_file.read()

# tag = r'<(?P<tag>\w+)'
# propert = f'(?P<prop>\w+)='
# tag_pro = r'<(?P<tag>.\w+) (?P<prop>\w+)='
# res = re.findall(tag, data)
# rezp = re.findall(propert, data)
# rezall = re.findall(tag_pro, data)
# m_tag = re.search(tag, data)
# m_prop = re.search(propert, data)
# m_all = re.search(tag_pro, data)


# print(m_tag.group(1))
# print(m_prop.group(1))
# pass

"""Блок 11.8 Модуль re Часть 3"""

"""№ 9 Функция normalize_jpeg()"""

# import re
# from re import sub

# def normalize_jpeg(filename):
#     return sub(r'.\w{3,4}$', r'.jpg', filename)

# print(normalize_jpeg('windows11.jpg'))

"""№ 10 Функция normalize_whitespace()"""

# from re import sub

# def normalize_whitespace(string):
#     return sub(r' {2,}', r' ', string)

# print(normalize_whitespace('Тут Тут н е т л и шних пробелов       !'))

"""№ 11 Ключевые слова"""

# import keyword
# from re import sub, IGNORECASE

# text = 'True and False - that is the question'

# for word in keyword.kwlist:
#     text = sub(rf'\b{word}\b', r'<kw>', text, flags=IGNORECASE)

# print(text)

"""№ 12 Первые буквы"""

# from re import sub

# text = 'Hi, everyone. Lets start a lesson!'

# print(sub(r'\b(\w)(\w)', r'\2\1', text))

"""№ 13 Умножение строк   ПОТОМ"""

# from re import sub
# import re

# text = '0(s)he0(be)lie0(ve)d'
# pattern = r'(\d+)(\(.*\))'

# def multiply_words(match):
#     n = int(match.group(1))
#     word = match.group(2)
#     return word * n

# n = re.findall(pattern, text)

# print(sub(pattern, multiply_words, text))

"""№ 14 Повторяющиеся слова   ПОТОМ"""

# from re import sub

# text = 'beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik'
# pattern = r'(\.w).*(\1)+'

# print(sub(pattern, r'\1', text))

"""№ 15 Комментарии 🌶️🌶️    ПОТОМ"""

# from re import sub
# import re

# pattern_one_string = r'(\n *)?(#+ .*\n)'
# pattern_end_string = r'(\n.*)?(  # .*)$'
# pattern_multistring = r'\n( *)""".*?"""\n'

# with open('315/1', encoding='UTF-8') as inp_file:
#     data = inp_file.read()

# one = re.findall(pattern_one_string, data, flags=re.M)
# end1 = re.findall(pattern_end_string, data, flags=re.M)

# multi1 = re.findall(pattern_multistring, data)#, flags=re.S)
# multi2 = re.search(pattern_multistring, data)#, flags=re.S)

# data = sub(pattern_one_string, r'\n', data, flags=re.M)
# data = sub(pattern_end_string, '', data, flags=re.M)
# data = sub(pattern_multistring, r'\n', data, flags=re.S)


# print(data)

"""БЛОК 11.9 Модуль re. Часть 4"""

"""№ 10 Точка с запятой"""

# import re

# with open('410/14', encoding='UTF-8') as inp_file:
#     data = inp_file.read()

# pattern = r'\s*[.,;]\s*'

# print(*re.split(pattern, data))

"""№ 11 Логическое выражение"""

# import re

# with open('411/15', encoding='UTF-8') as inp_file:
#     data = inp_file.read()

# pattern = r'\s*\|\s*|\s*\&\s*|\s*and\s*|\s*or\s*'

# print(*re.split(pattern, data), sep=', ')

"""№ 12 Функция multiple_split()"""

# import re

# def multiple_split(string, delimiters):
#     pattern = '|'.join(map(re.escape, delimiters))
#     pass
#     return re.split(pattern, string)

# print(multiple_split('There"was/a"small/boy"of/Quebec', ['/', '"']))

"""№ 19 Сумма чисел"""

# import re

# with open('419/15', encoding='UTF-8') as inp_file:
#     st, en = map(int, inp_file.readline().split())
#     data = inp_file.readline()

# pattern = re.compile(r'\D?(\d+)\D?')
# result = sum(map(int, pattern.findall(data, st, en)))

# print(result)
