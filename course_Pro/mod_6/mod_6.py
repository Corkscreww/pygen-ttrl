"""МОДУЛЬ 6
Дополнительные типы коллекций
6.4 Тип данных namedtuple. Часть 2

№ 11"""

# from collections import namedtuple

# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

# podp = ('Gold', 'Silver', 'Bronze', 'Basic')
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

# users.sort(key=lambda x: x.email)

# for status in podp:
#     for name, surname, email, plan in filter(lambda x: x.plan == status, users):
#         print(name, surname)
#         print(f'  Email: {email}')
#         print(f'  Plan: {plan}')
#         print()
# pass

"""№ 12 Вы кто такие? Я вас не звал"""

# import csv
# from datetime import datetime
# from collections import namedtuple

# Friend = namedtuple('Friend', 'surname,name,meeting_date,meeting_time')

# with open('meetings.csv', encoding='UTF-8') as csv_input:
#     rows = csv.reader(csv_input)
#     friends = []
#     for row in rows:
#         friends.append(row)
#     del friends[0]

# friends = [Friend(*friend) for friend in friends]


# for friend in sorted(friends,
#     key=lambda x: datetime.strptime(x.meeting_date + x.meeting_time,
#                                     '%d.%m.%Y%H:%M')):
#     print(friend.surname, friend.name)

"""
6.5 Тип defaultdict
№19 """

# from collections import defaultdict

# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966),
#         ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964),
#         ('Tutorials', 832), ('Merch', 642), ('Books', 815),
#         ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880),
#         ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
#         ('Tutorials', 977), ('Books', 656)]

# prod = defaultdict(int)

# for product, price in data:
#     prod[product] += price

# for product in sorted(prod):
#     print(f'{product}: ${prod[product]}')

"""№ 20"""

# from collections import defaultdict

# staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'),
#          ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'),
#          ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
#          ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'),
#          ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'),
#          ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
#          ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'),
#          ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'),
#          ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
#          ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'),
#          ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'),
#          ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
#          ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'),
#          ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'),
#          ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
#          ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'),
#          ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'),
#          ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
#          ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'),
#          ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'),
#          ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
#          ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'),
#          ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'),
#          ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
#          ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

# info = defaultdict(int)
# for otdel, name in staff:
#     info[otdel] += 1

# for otdel in sorted(info):
#     print(f'{otdel}: {info[otdel]}')

"""№ 21"""

# from collections import defaultdict

# staff_broken = [
#     ('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'),
#     ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'),
#     ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
#     ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'),
#     ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'),
#     ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
#     ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'),
#     ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'),
#     ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
#     ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'),
#     ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'),
#     ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
#     ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'),
#     ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'),
#     ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
#     ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'),
#     ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'),
#     ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
#     ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'),
#     ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'),
#     ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
#     ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'),
#     ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'),
#     ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
#     ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'),
#     ('Sales', 'John White'), ('Sales', 'Marie Cooper'),
#     ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
#     ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'),
#     ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'),
#     ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
#     ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'),
#     ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'),
#     ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
#     ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'),
#     ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'),
#     ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
#     ('Accounting', 'Dale Houston')
#     ]

# info = defaultdict(list)

# for otdel, name in staff_broken:
#     info[otdel].append(name)

# for otdel in sorted(info):
#     print(f'{otdel}: ', end='')
#     print(*sorted(info[otdel]))

"""№ 22 Функция wins()"""

# from collections import defaultdict

# def wins(result):
#     res = defaultdict(set)
#     for winner, loser in result:
#         res[winner].add(loser)

#     return res

# result = wins([('Артур', 'Дима'), ('Дима', 'Элина'),
#                ('Артур', 'Тимур'), ('Тимур', 'Анри'),
#                ('Тимур', 'Элина'), ('Элина', 'Тимур'),
#                ('Элина', 'Артур'), ('Анри', 'Илья'),
#                ('Элина', 'Анри'), ('Анри', 'Герман')])

# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))

"""№ 23 Функция flip_dict()"""

# from collections import defaultdict

# def flip_dict(dict_of_lists):
#     result = defaultdict(list)
#     for key in dict_of_lists:
#         for value in dict_of_lists[key]:
#             result[value].append(key)
#     return result

# data = {6: [1, 2, 3], 88: [3, 4, 6], '99': ['a', 'f', '3', 1, 2, 3],
#         'a': [1, 2, 3]}

# print(flip_dict(data))

"""№ 24 Функция best_sender()"""

# from collections import defaultdict

# def best_sender(messages, senders):
#     best_senders = defaultdict(int)
#     for i in range(len(messages)):
#         sender = senders[i]
#         message = messages[i]
#         best_senders[sender] += len(message.split())
#         maximum = best_senders[max(best_senders,
#                                    key=lambda x: best_senders[x])]
#     pass
#     best = list(filter(lambda x: best_senders[x] == maximum, best_senders))
#     best.sort(reverse=True)
#     pass
#     return best[0]

# messages = ['hi', 'hello', 'how r u', 'i am okay', 'how r u', 'i am okay too thanks']
# senders = ['Anri', 'Dima', 'Anri', 'Dima', 'Dima', 'Anri']

# print(best_sender(messages, senders))

"""
6.5 Тип данных OrderedDict
№ 20 Функция custom_sort()"""

# from collections import OrderedDict


# def custom_sort(ordered_dict, by_values=False):
#     if by_values:
#         sorted_items = sorted(
#             ordered_dict.items(), key=lambda x: x[1]
#         )
#     else:
#         sorted_items = sorted(
#             ordered_dict.items(), key=lambda x: x[0]
#         )
#     ordered_dict.clear()
#     for item in sorted_items:
#         ordered_dict[item[0]] = item[1]

#     ordered_dict['хуй'] = 88

# data1 = OrderedDict(e=11, b=22, a=99, g=33, c=33, d=33, h=99, f=77, i=88, k=44)
# custom_sort(data1, by_values=True)

# print(data1)

"""6.6 Тип данных Counter. Часть 1
№ 15 """


# from collections import Counter

# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

# file = files[0]
# tip_file = file[file.rfind('.') + 1:]

# files = list(map(lambda x: x[x.rfind('.') + 1:], files))
# counter_types = Counter(files)
# for filetype in sorted(counter_types):
#     print(f'{filetype}: {counter_types[filetype]}')

"""№ 16 Функция count_occurences()"""

# from collections import Counter

# def count_occurences(word, words):
#     words = words.lower().split()
#     cntr = Counter(words)
#     return cntr[word]

# word = 'Java'
# words = 'Python C++ C# JavaScript Go Assembler'
# print(count_occurences(word, words))

"""№ 17 Не поленимся и запишем"""

# from collections import Counter

# with open('input.txt') as inp_file:
#     stroka = inp_file.read()

# stroka = stroka.split(',')
# cntr = Counter(stroka)
# for prod in sorted(cntr):
#     print(f'{prod}: {cntr[prod]}')


"""№ 18 А сколько стоит курс?"""

# from collections import Counter

# with open('input.txt') as inp_file:
#     stroka = inp_file.read()

# stroka = stroka.replace(' ', '').split(',')
# cntr = Counter(stroka)
# for prod in sorted(cntr)
#     slovo = Counter(prod)
#     price = 0
#     for ch in slovo:
#         price += ord(ch) * slovo[ch]
#     print(f'{prod}: {price} UC x {cntr[prod]} = {cntr[prod] * price} UC')

"""№ 19 The Zen of Python"""

# from collections import Counter

# with open('pythonzen.txt') as inp_file:
#     text = []
#     for line in inp_file.readlines():
#         line = list(line.lower().strip())
#         for ch in line:
#             if ch.isalpha():
#                 text.append(ch)

# cntr = Counter(text)
# for ch in sorted(cntr):
#     print(f'{ch}: {cntr[ch]}')

"""6.8 Тип данных Counter. Часть 2
№ 12 В поисках слов 😇"""

# from collections import Counter

# with open('input.txt') as inp_file:
#     stroka = inp_file.read()

# stroka = stroka.lower().split()
# cntr = Counter(stroka)

# print(max(cntr, key=lambda x: cntr[x]))

"""№ 13 В поисках слов😋"""

# from collections import Counter

# with open('input.txt') as inp_file:
#     stroka = inp_file.read()

# stroka = stroka.lower().split()
# cntr = Counter(stroka)

# minimum = cntr[min(cntr, key=lambda x: cntr[x])]
# results = list(filter(lambda x: cntr[x] == minimum, cntr))

# print(*sorted(results), sep=', ')

"""№ 14 В поисках слов 🥳"""

# from collections import Counter

# with open('input.txt') as inp_file:
#     stroka = inp_file.read()

# stroka = stroka.lower().split()
# cntr = Counter(stroka)

# maximum = cntr[max(cntr, key=lambda x: cntr[x])]
# results = list(filter(lambda x: cntr[x] == maximum, cntr))

# print(max(results))

"""№ 15 Статистика длин слов"""

# from collections import Counter

# with open('input.txt') as inp_file:
#     stroka = inp_file.read()

# stroka = stroka.lower().split()
# cntr = Counter(stroka)

# result = Counter()
# for cnt in cntr:
#     kl = len(cnt)
#     val = cntr[cnt]
#     result.update({kl: val})

# for cnt in sorted(result, key=lambda x: result[x]):
#     print(f'Слов длины {cnt}: {result[cnt]}')

"""№ 16 Все еще достоин"""

# from collections import Counter

# with open('input.txt') as inp_file:
#     stroka = inp_file.readlines()
#     results = Counter()
#     for line in stroka:
#         name, ball = line.strip().split()
#         results.update({name: int(ball)})

# print(results.most_common()[-2][0])

"""№ 18 Here we go again"""

# from collections import Counter
# import csv

# with open('name_log.csv', encoding='UTF-8') as csv_input:
#     rows = csv.DictReader(csv_input)
#     cntr = Counter()
#     for user in rows:
#         cntr.update({user['email']:1})

# usr_list = list(cntr.most_common())
# usr_list.sort(key=lambda x: x[0])
# for mail, mount in sorted(usr_list, key=lambda x: x[1], reverse=True):
#     print(f'{mail}: {mount}')

"""№ 19 Функция scrabble()"""

# from collections import Counter


# def scrabble(symbols, word):
#     symbols = Counter(symbols.lower())
#     word = Counter(word.lower())
#     return word <= symbols


# print(scrabble('b1e2e3g4e___e___k', 'BeegeeK'))

"""№ 20 Функция print_bar_chart()"""

# from collections import Counter

# def print_bar_chart(data, mark):
#     cntr = Counter()
#     if type(data) == str:
#         for ch in data:
#             cntr.update({ch: 1})
#         for sym, amount in cntr.most_common():
#             print(f'{sym} |{mark * amount}')
#     if type(data) == list:
#         for stroka in data:
#             cntr.update({stroka: 1})
#         max_len = len(max(cntr, key=lambda x: len(x)))
#         for stroka, amount in cntr.most_common():
#             vst = stroka + ' ' * (max_len - len(stroka))
#             posl = mark * amount
#             print(f'{vst} |{posl}')


# my_list = ['арбуз', 'черешня', 'клубника', 'арбуз', 'банан', 'Малина', 'малина', 'арбуз', 'арбуз', 'Клубника', 'Банан', 'Малина', 'Черешня', 'Вишня', 'Малина', 'малина', 'Малина', 'Клубника', 'Вишня', 'Клубника']

# print_bar_chart(my_list, '@')

"""№ 21 Бесплатные курсы берут свое 😢"""

# from collections import Counter
# import csv, json

# cntr = Counter()
# for i in range(1, 5):
#     filename = f'quarter{i}.csv'
#     with open(filename, encoding='UTF-8') as csv_input:
#         rows = list(csv.reader(csv_input))
#         del rows[0]
#         for row in rows:
#             upd_dict = {
#                 row[0]: sum(
#                     [int(amount) for amount in row[1:]]
#                 )
#             }
#             cntr.update(upd_dict)

# with open('prices.json', encoding='UTF-8') as json_input:
#     json_data = json.load(json_input)
#     summa = 0
#     for product in cntr:
#         summa += cntr[product] * json_data[product]
#         pass

# print(summa)

"""Блок 6.9 Тип данных ChainMap. Часть 1
№ 22 Зоопарк"""

# import json
# from collections import ChainMap

# with open('zoo.json') as json_input:
#     animals = list(json.load(json_input))

# anim_map = ChainMap(*animals)
# print(sum(anim_map.values()))

"""№ 23 Булочный магнат"""

# from collections import ChainMap, Counter

# bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
# meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
# sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15,
#          'чили': 15}
# vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
# toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

# with open('input.txt') as inp_file:
#     zakaz = inp_file.read().split(',')
# pass
# zakaz = Counter(zakaz)
# menu = ChainMap(bread, meat, sauce, vegetables, toppings)

# summ = 0
# for ingred in zakaz:
#     summ += menu[ingred] * zakaz[ingred]

# max_len_ingr = len(max(zakaz, key=lambda x: len(x)))
# max_len_amount = len(str(zakaz[max(zakaz, key=lambda x: len(str(zakaz[x])))]))

# for punkt in zakaz:
#     print(f'{punkt}{" "  * (max_len_ingr - len(punkt))}'
#           f' x {zakaz[punkt]}')

# max_len_check = max_len_ingr + max_len_amount + 3
# len_itog = 7 + len(str(summ))
# if max_len_check > len_itog:
#     print('-' * (max_len_ingr + max_len_amount + 3))
# else:
#     print('-' * len_itog)
# print(f'ИТОГ: {summ}р')

"""Блок 6.10 Тип данных ChainMap. Часть 2
№ 13 Функция get_all_values()"""

# from collections import ChainMap

# def get_all_values(chainmap, key):
#     result = set()
#     for diction in chainmap.maps:
#         if key in diction:
#             result.add(diction[key])
#     return result

# chainmap = ChainMap({'name': 'Anri', 'city': 'Moscow'}, {'name': 'Arthur', 'city': 'Moscow'}, {'name': 'Timur', 'age': 29, 'city': 'Moscow'})

# result = get_all_values(chainmap, 'city')

# print(*sorted(result))

"""№ 14 Функция deep_update()"""

# from collections import ChainMap

# def deep_update(chainmap, key, value):
#     avial = False
#     for diction in chainmap.maps:
#         if key in diction:
#             avial = True
#             diction[key] = value
#     if not avial:
#         chainmap.update({key: value})

# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur', 'age': 29}, {'name': 'Anri', 'age': 20}, {'name': 'Dima', 'age': 20})
# deep_update(chainmap, 'age', 29)

# print(chainmap)

"""№ 15 Функция get_value()"""

# from collections import ChainMap

# def get_value(chainmap, key, from_left=True):
#     maps = chainmap.maps

#     if not from_left:
#         maps.reverse()

#     for diction in maps:
#         if key in diction:
#             return diction[key]

# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

# print(get_value(chainmap, 'age'))


