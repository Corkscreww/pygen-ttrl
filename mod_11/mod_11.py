"""Модуль 11. Регулярные выражения"""

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

import re

with open('13/7', encoding='UTF-8') as inp_file:
    data = inp_file.readlines()
    bg = 'beegeek'

pat3 = r'^beegeek.*beegeek$'
pat2 = r'(^beegeek.*)|(.*beegeek$)'
pat1 = r'beegeek'
ball = 0

for string in data:
    string = string.strip()
    bal3 = re.search(pat3, string)
    bal2 = re.search(pat2, string)
    bal1 = re.search(pat1, string)
    if bal3:
        ball += 3
    elif bal2:
        ball += 2
    elif bal1:
        ball += 1
    elif string == 'beegeek':
        ball += 2

print(ball)
