
"""ДАТА-ВРЕМЯ
БЛОК 3.5 РЕШЕНИЕ ЗАДАЧ
№2"""
# from datetime import date, time, datetime, timedelta

# mes = 1
# year = 1
# dat = date(year, mes, 13)

# result = {i: 0 for i in range(7)}

# while year <= 9999:
#     result[dat.weekday()] += 1
#     mes += 1
#     try:
#         dat = date(year, mes, 13)
#     except ValueError:
#         mes = 1
#         year += 1
#         try: 
#             dat = date(year, mes, 13)
#         except ValueError:
#             for day in result:
#                 print(f'{day} : {result[day]}')

"""№3 снова не успел"""

# from datetime import datetime, time

# now_time = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# shed_st = {i: now_time.replace(hour=9, minute=0) for i in range(7)}
# shed_st[5] = now_time.replace(hour=10, minute=0)
# shed_st[6] = now_time.replace(hour=10, minute=0)
# shed_fin = {i: now_time.replace(hour=21, minute=0) for i in range(7)}
# shed_fin[5] = now_time.replace(hour=18, minute=0)
# shed_fin[6] = now_time.replace(hour=18, minute=0)

# day = now_time.weekday()

# if now_time < shed_st[day] or now_time > shed_fin[day]:
#     print('Магазин не работает')
# else:
#     print((shed_fin[day] - now_time).total_seconds() // 60)

"""№4 самое понятное условие"""

# from datetime import datetime, timedelta

# date_st, date_fin = datetime.strptime(input(), '%d.%m.%Y'), \
#                     datetime.strptime(input(), '%d.%m.%Y')

# dat = date_st
# td1 = timedelta(days=1)
# td3 = timedelta(days=3)

# while True:
#     if (dat.day + dat.month) % 2 == 1:
#         date_st = dat
#         break
#     else:
#         dat += td1

# while dat <= date_fin:
#     if dat.weekday() != 0 and dat.weekday() != 3:
#         print(dat.strftime('%d.%m.%Y'))
#     dat += td3

"""№5 сотрудники организации 😄"""

# from datetime import datetime

# spisok = []
# for _ in range(int(input())):
#     chel = input().split()
#     spisok.append(chel)

# max_date = datetime(2025, 1, 1)
# cnt = 0

# for i in range(len(spisok)):
#     dat = datetime.strptime(spisok[i][2], '%d.%m.%Y')
#     if dat < max_date:
#         max_date = dat
#         max_ind = i
#         cnt = 1
#     elif dat == max_date:
#         cnt += 1

# if cnt > 1:
#     print(max_date.strftime('%d.%m.%Y'), cnt)
# else:
#     print(max_date.strftime('%d.%m.%Y'), spisok[max_ind][0], spisok[max_ind][1])

"""№6 сотрудники организации 🙂"""

# from datetime import datetime

# with open('input.txt') as inp:
#     spisok = []
#     for chel in inp.readlines():
#         chel = chel.split()
#         spisok.append(chel)


# dati = {datetime.strptime(chel[2], '%d.%m.%Y'): 0 for chel in spisok}

# for i in range(len(spisok)):
#     dat = datetime.strptime(spisok[i][2], '%d.%m.%Y')
#     dati[dat] += 1
    
# dati = sorted(dati.items(), key=lambda x: x[1], reverse=True)

# pred_dat = dati[0][1]
# for dat in dati:
#     if pred_dat != dat[1]:
#         break
#     print(dat[0].strftime('%d.%m.%Y'))
#     pred_dat = dat[1]
    
"""№7 Сотрудники организации 😔"""

# from datetime import datetime

# with open('input.txt') as inp:
#     spisok = []
#     now_date = datetime.strptime(inp.readline().strip(), \
#                                  '%d.%m.%Y').replace(year=2024)
#     for chel in inp.readlines():
#         chel = chel.split()
#         spisok.append(chel)

# spisok = [(' '.join(chel[:2]), 
#            datetime.strptime(chel[2], '%d.%m.%Y').replace(year=2024))
#           for chel in spisok]

# spis_imen = []

# for chel in spisok:
#     day = (chel[1] - now_date).days
#     if day <= 7:
#         spis_imen.append(chel)

# if spis_imen:
#     print(min(spis_imen, key=lambda x: [1])[0])
# else:
#     print('Дни рождения не планируются')
# print()

"""№8 Fake News 🌶"""

# from datetime import datetime, timedelta

# def chose_plural(num, words):
#     last_dig = int(str(num)[-1])
#     if last_dig == 1:
#         return words[0]
#     elif 1 < last_dig < 5:
#         return words[1]
#     elif 10 < num < 20 or 4 < last_dig < 10 or last_dig == 0:
#         return words[2]


# release_date = datetime(2022, 11, 8, 12, 00)

# with open('input.txt') as inp:
#     now_date = datetime.strptime(inp.readline().strip(), \
#                                  '%d.%m.%Y %H:%M')

# time_left = release_date - now_date

# if now_date > release_date:
#     print('Курс уже вышел!')
# else:
#     print('До выхода курса усталось: ', end='')
#     hrs = time_left.seconds // 3600
#     mins = (time_left.seconds - hrs * 3600) // 60
    
#     if time_left.days:
#         print(f"{time_left.days} "
#               f"{chose_plural(time_left.days, ('день', 'дня', 'дней'))}",
#               end='')
#         if hrs:
#             print(f" и {hrs} {chose_plural(hrs, ('час', 'часа', 'часов'))}")
#     else:
#         if hrs:
#             print(f"{hrs} {chose_plural(hrs, ('час', 'часа', 'часов'))}",
#                   end='')
#             if mins:
#                 print(f" и {mins} "
#                       f"{chose_plural(mins, ('минута', 'минуты', 'минут'))}")
#         else:
#             print(f"{mins} "
#                   f"{chose_plural(mins, ('минута', 'минуты', 'минут'))}")

"""БЛОК 3.6 Модуль time
№ 10 функция calculate_it"""

# import time


# def calculate_it(func, *args):
#     st_time = time.perf_counter()
#     result = func(*args)
#     return (result, time.perf_counter() - st_time)


# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c


# print(calculate_it(add, 1, 2, 3))

"""№ 11 функция get_the_fastest_func()"""

# import time

# def get_the_fastest_func(funcs, arg):
#     time_min = 0
#     for func in funcs:
#         st_time = time.perf_counter()
#         res = func(arg)
#         res_time = time.perf_counter() - st_time
#         if res_time < time_min:
#             time_min = res_time
#     return time_min

"""№ 12"""

# from math import factorial
# import time

# def factorial_recurrent(n):
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)

# def factorial_classic(n):
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# def calculate_it(func, *args):
#     st_time = time.perf_counter()
#     func(*args)
#     return time.perf_counter() - st_time


# functions = [factorial, factorial_classic, factorial_recurrent]
# times = {func: calculate_it(func, 900) for func in functions}

# print(f'{min(times, key=lambda x: times[x])} time = {min(times.values())}')

"""№ 13"""

# import time


# def for_and_append(arg):
#     result = []
#     for i in range(arg):
#         result.append(i + 1)
#     return result


# def list_comprehension(arg):
#     return [i + 1 for i in range(arg)]


# def calculate_it(func, *args):
#     st_time = time.perf_counter()
#     func(*args)
#     return time.perf_counter() - st_time


# def get_the_fastest_func(funcs, arg):
#     times = {func: calculate_it(func, arg) for func in funcs}
#     return f'{min(times, key=lambda x: times[x])} time = {min(times.values())}'


# print(get_the_fastest_func([for_and_append, list_comprehension], 10**7))

"""№ 14"""

# import time

# def calculate_it(func, *args):
#     st_time = time.perf_counter()
#     func(*args)
#     return time.perf_counter() - st_time


# def get_the_fastest_func(funcs, arg):
#     times = {func: calculate_it(func, arg) for func in funcs}
#     return f'{min(times, key=lambda x: times[x])} time = {min(times.values())}'

# def for_and_append(iterable):
#     result = []
#     for elem in iterable:
#         result.append(elem)
#     return result


# def list_comprehension(iterable):
#     return [elem for elem in iterable]


# def list_function(iterable):
#     return list(iterable)

# print(get_the_fastest_func([for_and_append, list_comprehension, 
#                             list_function], range(10**5)))

"""БЛОК 3.7 Модуль calendar
№ 7 Високосный год"""

# import calendar


# with open('input.txt') as inp:
#     years = [line.strip() for line in inp.readlines()]

# for god in years:
#     print(calendar.isleap(int(god)))

"""№ 8 Календарь на месяц"""

# import calendar

# with open('input.txt') as inp:
#     st = inp.readline()

# year, month = int(st.split()[0]), st.split()[1]

# mont = {
#     'Jan': 1,
#     'Feb': 2,
#     'Mar': 3,
#     'Apr': 4,
#     'May': 5,
#     'Jun': 6,
#     'Jul': 7,
#     'Aug': 8,
#     'Sep': 9,
#     'Oct': 10,
#     'Nov': 11,
#     'Dec': 12,
# }

# calendar.prmonth(year, mont[month])

"""№ 9 День недели"""

# import calendar
# from datetime import datetime

# with open('input.txt') as inp:
#     dat = datetime.strptime(inp.readline(), '%Y-%m-%d')

# print(calendar.day_name[calendar.weekday(dat.year, dat.month, dat.day)])

"""№ 10 Количество дней"""

# import calendar

# with open('input.txt') as inp:
#     st = inp.readline()

# year, month = int(st.split()[0]), int(st.split()[1])

# print(calendar.monthrange(year, month)[1])


"""№ 11 Количество дней"""

# import calendar

# with open('input.txt') as inp:
#     st = inp.readline()

# year, month = int(st.split()[0]), st.split()[1]

# mont_dic = {mes[1]: mes[0] for mes in enumerate(calendar.month_name)}

# print(calendar.monthrange(year, mont_dic[month])[1])

"""№ 12 Функция get_days_in_month()"""

# from datetime import date
# import calendar

# def get_days_in_month(year, month):
#     mont_dic = {mes[1]: mes[0] for mes in enumerate(calendar.month_name)}
#     month_num = mont_dic[month]
#     return [date(year, month_num, i) for i in range(
#         1,
#         calendar.monthrange(year, month_num)[1] + 1
#     )]

# with open('input.txt') as inp:
#     st = inp.readline()

# year, month = int(st.split()[0]), st.split()[1]

# print(get_days_in_month(year, month))

"""№ 13 Функция get_all_mondays()"""

# from datetime import timedelta, date

# td = timedelta(days=7)

# with open('input.txt') as inp:
#     year = int(inp.readline())

# if calendar.monthrange(year, 1)[0] != 0:
#     day1 = 8 - calendar.monthrange(year, 1)[0]
# else:
#     day1 = 1
# dat = date(year, 1, day1)
# while dat.year == year:
#     print(dat, end=':::')
#     dat += td

"""№ 14 ТЧМ"""

# from datetime import date

# with open('input.txt') as inp:
#     year = int(inp.readline())

# mont = 1

# while mont < 13:
#     first_thu = calendar.monthrange(year, mont)[0]
#     if first_thu < 3:
#         chet = 1 + 3 - first_thu
#     elif first_thu > 3:
#         chet = 11 - first_thu
#     elif first_thu == 3:
#         chet = 1
#     chet += 14
#     dat = date(year, mont, chet)
#     print(dat, end=':::')
#     mont += 1

"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
МОДУЛЬ 4 РАБОТА С ФАЙЛАМИ
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

БЛОК 4.1 Потоковый воод stdin и вывод stdout

№ 10 Обратный порядок"""

# import sys

# data = [line.strip() for line in sys.stdin]

# for line in data:
#     sys.stdout.write(line[::-1] + '\n')


"""№ 11 Размах данных"""

# import sys
# from datetime import date, timedelta, datetime

# data = [datetime.strptime(line.strip(), '%Y-%m-%d') for line in sys.stdin]

# sys.stdout.write(str((max(data) - min(data)).days))

"""№ 12 Лемма о трёх носках"""

# import sys

# data = [int(line.strip()) for line in sys.stdin]

# if len(data) % 2 == 0:
#     if data[-1] % 2 == 0:
#         sys.stdout.write('Дима')
#     else:
#         sys.stdout.write('Анри')

# if len(data) % 2 == 1:
#     if data[-1] % 2 ==0:
#         sys.stdout.write('Анри')
#     else:
#         sys.stdout.write('Дима')    

"""№ 13 Урок статистики"""

# import sys

# data = sys.stdin.readlines()

# data = [int(line.strip()) for line in data]

# sys.stdout.write('Рост самого низкого ученика: ' + str(min(data)) + '\n')
# sys.stdout.write('Рост самого высокого ученика: ' + str(max(data)) + '\n')
# sys.stdout.write('Средний рост: ' + str(sum(data) / len(data)))

"""№ 14 Комментатор"""

# import sys
# data = [line.strip() for line in sys.stdin.readlines()]

# cnt = 0
# for line in data:
#     if line[0] == '#':
#         cnt += 1
# print(cnt)

"""№ 15 Без комментариев"""

# import sys
# data = sys.stdin.readlines()

# for line in data:
#     if line != '\n':
#         if line.strip()[0] != '#':
#             sys.stdout.write(line)
#     else:
#         sys.stdout.write(line)

"""№ 16 Панорамное агентство"""

# import sys

# data = [line.strip().split(' / ') for line in sys.stdin.readlines()]

# subj = data[-1][0]
# del data[-1]

# data.sort(key=lambda x: x[0])
# for line in sorted(data, key=lambda x: int(x[2].replace('.', ''))):
#     sub = line[1]
#     if sub == subj:
#         print(line[0])

"""№ 17 Это точно Python?"""

# import sys
# from datetime import datetime

# data = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin.readlines()]

# if len(set(data)) != len(data):
#     print('MIX')  
# elif data == sorted(data):
#     print('ASC')
# elif data == sorted(data, reverse=True):
#     print('DESC')
# else:
#     print('MIX')

"""№ 18 Гуру прогрессий"""

# import sys

# data = [int(line.strip()) for line in sys.stdin.readlines()]

# arif = True
# geom = True
# for i in range(2, len(data)):
#     a0, a1, a2 = data[i - 2:i + 1]
#     if a1 - a0 != a2 - a1:
#         arif = False
#     if a1 / a0 != a2 / a1:
#         geom = False
#     if not arif and not geom:
#         break

# if arif:
#     print('Арифметическая прогрессия')
# elif geom:
#     print('Геометрическая прогрессия')
# else:
#     print('Не прогрессия')

"""
БЛОК 4.2 Работа с csv файлами

№ 12 Скидки"""

# import csv

# with open('data.csv', encoding='utf-8') as csv_file:
#     rows = list(csv.reader(csv_file, delimiter=';'))
#     for row in rows[1:]:
#         name, old, new = row
#         if int(old) > int(new):
#             print(name)

"""№ 13 Средняя зарплата"""

# import csv

# with open('data.csv', encoding='utf-8') as csv_file:
#     rows = list(csv.reader(csv_file, delimiter=';'))

# rows = list(map(lambda x: [x[0], int(x[1])], rows[1:]))
# companys = set()

# for row in rows:
#     companys.add(row[0])

# comp_sum = dict.fromkeys(companys, 0)
# comp_kol = comp_sum.copy()

# for row in rows:
#     comp_sum[row[0]] += row[1]
#     comp_kol[row[0]] += 1

# for firm in comp_sum:
#     comp_sum[firm] = comp_sum[firm] / comp_kol[firm]

# for firm in sorted(comp_sum, key=lambda x: comp_sum[x]):
#     print(firm)
# print()

"""№ 14 функция csv_columns()"""

# import csv

# def csv_columns(file):
#     with open(file, encoding='utf-8') as csv_file:
#         rows = csv.DictReader(csv_file)
#         print()
#         for row in rows:
#             result = row.copy()
#             break
#         for key in result:
#             result[key] = []
#         for row in rows:
#             for key in row:
#                 result[key].append(row[key])
#         return result

# print(csv_columns('data.csv'))

"""№ 15 Популярные домены"""

# import csv


# with open('data.csv', encoding='utf-8') as csv_file:
#     rows = csv.DictReader(csv_file)
#     domain = {}
#     for row in rows:
#         dom = row['email'][row['email'].find('@') + 1:]
#         domain[dom] = domain.setdefault(dom, 0) + 1

# domain = {key: domain[key] for key in sorted(domain)}
# domain = [{'domain':key, 'count':domain[key]} for key in sorted(
#     domain,
#     key=lambda x:domain[x],
#     )]

# columns = ['domain', 'count']
# file = 'domain_usage.csv'
# with open(file, 'w') as out_file:
#     writer = csv.DictWriter(out_file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(domain)

"""№ 16 Wi-Fi Москвы"""

# import csv


# with open('wifi.csv', encoding='utf-8') as inp_file:
#     rows = csv.DictReader(inp_file, delimiter=';')
#     result = {}
#     for row in rows:
#         raion = row['district']
#         result[raion] = result.setdefault(raion, 0) + \
#             int(row['number_of_access_points'])

# result = {key: result[key] for key in sorted(result)}
# result = {key: result[key] for key in sorted(
#     result,
#     key=lambda x: result[x],
#     reverse=True,
# )}
# for rai, cnt in result.items():
#     print(f'{rai}: {cnt}')


"""№ 17 Последний день на Титанике"""

# import csv

# with open('titanic.csv', encoding='utf-8') as inp_file:
#     rows = csv.DictReader(inp_file, delimiter=';')
#     man, woman = [], []
#     for row in rows:
#         surv = int(row['survived'])
#         age = float(row['age'])
#         sex = row['sex']
#         name = row['name']
#         if surv == 1 and age < 18:
#             if sex == 'male':
#                 man.append(name)
#             else:
#                 woman.append(name)
# print(*man, sep='\n')
# print(*woman, sep='\n')


"""№ 18 Лог-файл"""


# from datetime import datetime
# import csv

# columns = ['username', 'email', 'dtime']
# inp = 'name_log.csv'
# out = 'new_name_log.csv'
# result = []

# with open(inp, encoding='utf-8') as inp_file:
#     rows = csv.DictReader(inp_file)
#     emails = set()
    
#     for row in rows:
#         emails.add(row['email'])
#     result = []
    
#     result = {}
#     for mail in emails:
#         result[mail] = {'username': '', 'dtime': datetime(1, 1, 1)}

#     inp_file.seek(0)
#     rows = csv.DictReader(inp_file)
#     for row in rows:
#         name = row['username']
#         email = row['email']
#         dtim = row['dtime']
#         dtime = datetime.strptime(dtim, '%d/%m/%Y %H:%M')
#         if dtime > result[email]['dtime']:
#             result[email]['username'] = name
#             result[email]['dtime'] = dtime
# result_list = []     
# for mail in result:
#     write_dic = {}
#     write_dic['username'] = result[mail]['username']
#     write_dic['dtime'] = result[mail]['dtime'].strftime('%d/%m/%Y %H:%M')
#     write_dic['email'] = mail
#     result_list.append(write_dic)

# result_list.sort(key=lambda x: x['email'])
# with open(out, 'w', encoding='utf-8') as out_file:
#     writer = csv.DictWriter(out_file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(result_list)

# print()


"""№ 19 Сортировка по столбцу 🌶️"""


# import csv

# with open('deniro.csv') as inp_file:
#     rows = csv.reader(inp_file)
#     result = []
#     for row in rows:
#         result.append(list(row))

# stolb = int(input())
# result.sort(key=lambda x: x[stolb - 1])
# for st in result:
#     print(*st, sep=',')
# print()


"""№ 20 Проще, чем кажется 🌶️"""

# import csv

# def condense_csv(filename, id_name):
#     outfile = 'condensed.csv'
#     with open(filename, encoding='utf-8') as inp_file:
#         rows = csv.reader(inp_file)
#         result = {}
#         props = []
#         for row in rows:
#             new_dict = {row[1]: row[2]}
#             result.setdefault(row[0], {})
#             if result[row[0]]:
#                 result[row[0]].update(new_dict)
#             else:
#                 result[row[0]] = new_dict
#             props.append(row[1])
#             pass
#         print()
    
#     columns = [id_name] + props[:len(props) // len(result)]
#     with open(outfile, 'w', encoding='utf-8') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(columns)
#         for obj in result:
#             row = [obj]
#             for prop in result[obj]:
#                 row.append(result[obj][prop])
#             writer.writerow(row)
#     return None

# infile = 'data.csv'

# print(condense_csv(infile, id_name='ID'))


"""№ 21 Возрастание классов 🌶️"""

# import csv

# with open('student_counts.csv') as inp_file:
#     rows = csv.reader(inp_file)
#     classes = {}
#     for row in rows:
#         gg = row[1:]
#         for klass in gg:
#             classes.setdefault(klass, {})
#         break
        
# with open('student_counts.csv') as inp_file:   
#     rows = csv.DictReader(inp_file)
#     for row in rows:
#         for klass in row:
#             if klass in classes:
#                 classes[klass].update({row['year']: row[klass]})

# classes = {klass: classes[klass] for klass in sorted(
#     classes, key=lambda x: x[-1]
# )}
# classes = {klass: classes[klass] for klass in sorted(
#     classes, key=lambda x: int(x[:2]) if x[:2].isalnum() else int(x[0])
# )}


# res_write_list = [{'year': str(year)} for year in range(2000, 2022)]

# for i in range(len(res_write_list)):
#     for klass in classes:
#         year = str(i + 2000)
#         dic_to_update = {klass: classes[klass][year]}
#         res_write_list[i].update(dic_to_update)

# columns = []
# for column in res_write_list[0]:
#     columns.append(column)

# with open('sorted_students_counts.csv', 'w', encoding='utf-8') as out_csv:
#     writer = csv.DictWriter(out_csv, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(res_write_list)


"""№ 22 Голодный студент 🌶️"""

# import csv

# with open('prices.csv', encoding='utf=8') as inp_csv:
#     rows = csv.DictReader(inp_csv, delimiter=';')
#     min_price = 1_000_000_000
#     min_price_products = {}
#     for row in rows:
#         for product in row:
#             price = row[product]
#             if not price.isdigit():
#                 magaz = price
#                 continue
#             else: 
#                 price = int(price)
#                 if price < min_price:
#                     min_price = price
#                     min_price_products.clear()
#                     min_price_products.update({product: magaz})
#                 elif price == min_price:
#                     min_price_products.update({product: magaz})

# if len(min_price_products) > 1:
#     # leks = list(map(lambda x: (ord(ch) for ch in x), min_price_products))
#     min_po_imeni_prod = list(filter(
#         lambda x: x == min(min_price_products), min_price_products))
#     if len(min_po_imeni_prod) == 1:
#         print(f'{min_po_imeni_prod[0]}: '
#               f'{min_price_products[min_po_imeni_prod[0]]}')


"""
БЛОК 4.3 Работа с json-файлами. Часть-2

№ 1"""

# import json

# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi',
#              'Kazakhstan': 'Nur-Sultan', 'Mali': 'Bamako',
#              'Colombia': 'Bogota', 'Finland': 'Helsinki',
#              'Costa Rica': 'San Jose', 'Cuba': 'Havana', 'France': 'Paris',
#              'Gabon': 'Libreville', 'Liberia': 'Monrovia', 'Angola': 'Luanda',
#              'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
# cntrs_json = json.dumps(countries,
#                         indent=3,
#                         sort_keys=True,
#                         separators=(',', ' - ')) 
# print(cntrs_json)

"""№ 2"""

# import json

# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }


# data_json = json.dumps(words, skipkeys=True)
# print(data_json)

"""№ 3"""

# import json

# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "gaolkeeper": "M. Neuer",
#          "league_position": 1}

# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "gaolkeeper": "M. Ter Stegen",
#          "league_position": 7}

# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "gaolkeeper": "D. De Gea",
#          "league_position": 8}

# cntrs_json = json.dumps([club1, club2, club3], indent=3)
# print(cntrs_json)

""""№ 4"""

# import json

# specs = {
#          'Модель': 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }

# specs_json = json.dumps(specs, indent=3, ensure_ascii=False)

# print(specs_json)

"""№ 5 Функция is_correct_json()"""

# import json

# def is_correct_json(string):
#     try:
#         json_data = json.dumps(string)
#     except:
#         return False
#     return True

# data1 = {(1, 1): 1}
# data2 = {1: 1}

# print(is_correct_json(data1), is_correct_json(data2))

"""№ 6 Элементы JSON"""

# import json, sys

# for line in sys.stdin:
#     deserialiser = json.loads(line)
#     for key, value in deserialiser.items():
#         if type(value) == list:
#             print(f'{key}: {", ".join(value)}')
#         else:
#             print(f'{key}: {value}')

"""№ 7 Разные типы"""

"""
Узнать рабочую директорию, и вывести её на экран

import os

cwd = os.getcwd()
files = os.listdir(cwd)
print('!!!')
print('Files in %r: %s' % (cwd, files))

"""

# import json


# def stroka(val):
#     return val + '!'


# def numb(val):
#     return val + 1


# def bul(val):
#     return not val


# def spisok(val):
#     return val + val


# def slovar(val):
#     val.update({'newkey': None})
#     return val


# functional_dictionary = {
#     str: stroka,
#     int: numb,
#     bool: bul,
#     list: spisok,
#     dict: slovar,
# }


# with open('data.json') as json_in:
#     json_data = json.load(json_in)
#     result = []
#     for element in json_data:
#         if element != None:
#             result.append(functional_dictionary[type(element)](element))

# with open('updated_data.json', 'w', encoding='UTF-8') as out_json:
#     json.dump(result, out_json, indent=2)


"""№ 8 Объединение объектов"""

# import json

# with open('data1.json') as file1, open('data2.json') as file2:
#     data1, data2 = json.load(file1), json.load(file2)
#     result = {key: value for key, value in data1.items()}
#     result.update({key: value for key, value in data2.items()})

# with open('data_merge.json', 'w', encoding='UTF-8') as out_json:
#     json.dump(result, out_json, indent=3)


"""№ 9 Восстановление недостающих ключей"""

# import json

# key_list = ['age', 'country', 'phone', 'family_status', 'email',
#             'name', 'children', 'university']

# with open('people.json') as inp_json:
#     json_data = json.load(inp_json)
#     for element in json_data:
#         for key in key_list:
#             element.setdefault(key, None)

# with open('updated_people.json', 'w', encoding='UTF-8') as out_json:
#     json.dump(json_data, out_json, indent=3)


"""№ 10 Я исповедую Python, а ты?"""


# import json

# religions = {}
# with open('countries.json') as inp_json:
#     json_data = json.load(inp_json)
#     for element in json_data:
#         religion = element['religion']
#         country = element['country']
#         religions.setdefault(religion, [])
#         religions[religion].append(country)


# with open('religion.json', 'w', encoding='UTF-8') as out_json:
#     json.dump(religions, out_json, indent=3)


"""№ 11 Спортивные площадки"""

# import json, csv

# with open('playgrounds.csv') as inp_csv:
#     csv_data = csv.DictReader(inp_csv, delimiter=';')
#     addresses = {}
#     for element in csv_data:
#         district = element['District']
#         area = element['AdmArea']
#         address = element['Address']
#         addresses.setdefault(area, {})
#         addresses[area].setdefault(district, [])
#         addresses[area][district].append(address)

# with open('addresses.json', 'w', encoding='UTF-8') as out_json:
#     json.dump(addresses, out_json, indent=3, ensure_ascii=False)


"""№ 12 Студенты курса"""

# import json, csv

# with open('students.json') as inp_json:
#     json_data = json.load(inp_json)
#     data = list(filter(
#         lambda x: x['age'] > 17 and x['progress'] > 74, json_data
#         ))

# csv_data = [{'name': student['name'], 'phone': student['phone']} 
#             for student in data]

# csv_data.sort(key=lambda x: x['name'])
# csv_header = ['name', 'phone']
# with open('data.csv', 'w', encoding='UTF-8') as out_csv:
#     writer = csv.DictWriter(out_csv, fieldnames=csv_header)
#     writer.writeheader()
#     writer.writerows(csv_data)

"""№ 13 Бассейны"""

# import json
# from datetime import datetime, time

# with open('pools.json') as inp_json:
#     json_data = json.load(inp_json)
#     whs = 'WorkingHoursSummer'
#     pn = 'Понедельник'

#     pools = list(filter(
#         lambda x: x[whs].get(pn) and
#         time(hour=datetime.strptime(
#             x[whs][pn][:5], '%H:%M').hour) <= time(hour=10) and
#         time(hour=datetime.strptime(
#             x[whs][pn][6:], '%H:%M').hour) >= time(hour=12), json_data)
#     )

# ds = 'DimensionsSummer'
# ln = 'Length'
# wh = 'Width'

# pools = list(filter(
#     lambda x: x[ds][ln] == max(pools, key=lambda x: x[ds][ln])[ds][ln],
#     pools
# ))

# if len(pools) > 1:
#     pools = list(filter(
#         lambda x: x[ds][wh] == max(pools, key=lambda x: x[ds][wh])[ds][wh],
#         pools))

# for pool in pools:
#     print(f'{pool[ds][ln]}x{pool[ds][wh]}')
#     print(f'{pool["Address"]}')


"""№ 14 Результаты экзамена 🌶"""

# import json, csv
# from datetime import datetime, timedelta

# with open('exam_results.csv') as inp_csv:
#     csv_data = csv.DictReader(inp_csv)
#     exam_results = [result for result in csv_data]
#     students_set = set()

# for element in exam_results:
#     students_set.add((element['name'], element['surname']))
    
# nm = 'name'
# sn = 'surname'
# sc = 'score'
# dt = 'date_and_time'
# em = 'email'
# best_scores = []
# for name, surname in students_set:
#     student_results = list(filter(
#         lambda x: x[nm] == name and x[sn] == surname, exam_results))
#     student_results = list(filter(
#         lambda x: x[sc] == max(student_results, key=lambda x: x[sc])[sc],
#         student_results))
#     if len(student_results) > 1:
#         dtmax = datetime.strptime(
#             max(student_results, 
#                 key=lambda x: datetime.strptime(x[dt], '%Y-%m-%d %H:%M:%S')
#             )[dt], '%Y-%m-%d %H:%M:%S'
#         )
#         student_results = list(filter(
#             lambda x: datetime.strptime(x[dt], '%Y-%m-%d %H:%M:%S') >=
#             dtmax - timedelta(hours=1), student_results
#         ))
#     best_scores.append(student_results[0])
# pass
# best_scores.sort(key=lambda x: x[em])

# with open('best_scores.json', 'w', encoding='UTF-8') as out_json:
#     json.dump(best_scores, out_json, indent=3)

"""№ 15 Общественное питание 😥"""

# import json

# with open('food_services.json') as inp_json:
#     json_data = json.load(inp_json)
#     json_data = [service for service in json_data]

# distr_count = {}
# for service in json_data:
#     distr_count.setdefault(service['District'], 0)
#     distr_count[service['District']] += 1
# distr_count = sorted(distr_count.items(),
#                      key=lambda x: x[1], reverse=True)

# kafe = {}
# for service in json_data:
#     kafe.setdefault(service['Name'], 0)
#     kafe[service['Name']] += 1
# kafe = sorted(kafe.items(),
#                      key=lambda x: x[1], reverse=True)


# print(f'{distr_count[0][0]}: {distr_count[0][1]}')
# print(f'{kafe[0][0]}: {kafe[0][1]}')

"""№ 16 Общественное питание 😰"""

# import json

# with open('food_services.json') as inp_json:
#     json_data = json.load(inp_json)
#     json_data = [service for service in json_data]

# types = {}
# for service in json_data:
#     tip = service['TypeObject']
#     if tip not in types:
#         types.setdefault(tip, None) 
#         maximum = max(
#             json_data,
#             key=lambda x: x['SeatsCount'] if x['TypeObject'] ==
#             tip else 0
#         )
#         types[tip] = (maximum['Name'], maximum['SeatsCount'])

# for tips in sorted(types):
#     pass
#     print(f'{tips}: {types[tips][0]}, {types[tips][1]}')
# pass

"""
БЛОК 4.4 Работа с zip-файлами

№ 14 """

# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     cnt = 0
#     info = zip_file.infolist()
#     for file in info:
#         if not file.is_dir():
#             cnt += 1
# print(cnt)


"""№ 15 Объем файлов"""

# from zipfile import ZipFile
# from functools import reduce
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     cnt_comp, cnt_not_comp = 0, 0
#     # for file in info:
#     #     cnt_comp += file.compress_size
#     #     cnt_not_comp += file.file_size
#     cnt_comp = reduce(lambda x, y: x + y.compress_size, info, 0)
#     cnt_not_comp = reduce(lambda x, y: x + y.file_size, info, 0)
# print(f'Объем исходных файлов: {cnt_not_comp} байт(а)')
# print(f'Объем сжатых файлов: {cnt_comp} байт(а)')


"""№ 16 Наилучший показатель"""

# from zipfile import ZipFile
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     best = 1
#     for file in info:
#         if not file.is_dir():
#             koef = file.compress_size / file.file_size
#             if koef < best:
#                 best = koef
#                 best_file = file
# best_file = best_file.filename
# print(best_file[best_file.rindex('/') + 1:])


"""№ 17 Избранные"""

# from zipfile import ZipFile
# from datetime import datetime
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     files = {file.filename: file.date_time for file in info}

# izb_dt = datetime(2021, 11, 30, 14, 22)
# files = list(filter(lambda x: datetime(*files[x]) > izb_dt and
#                     x[x.rfind('/') + 1:], files))
# files = list(map(lambda x: x[x.rfind('/') + 1:], files))
# files.sort()
# print(*files, sep='\n')

"""№ 18 Форматированный вывод"""

# from zipfile import ZipFile
# from datetime import datetime
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     files = {file.filename[file.filename.rfind('/') + 1:]:
#              {
#                  'date': datetime(*file.date_time),
#                  'size': file.file_size,
#                  'comp_size': file.compress_size
#              } for file in info if not file.is_dir()}

# for file in sorted(files):
#     print(f'{file}\n'
#           f'  Дата модификации файла: '
#           f'{files[file]["date"].strftime("%Y-%M-%d %H:%M:%S")}\n'
#           f'  Объем исходного файла: {files[file]["size"]}\n'
#           f'  Объем сжатого файла: {files[file]["comp_size"]}\n')


"""№ 19"""

# from zipfile import ZipFile

# file_names = ['clue_exam_results.txt', 'clue_hungry_student.txt', 
#               'clue_students.txt', 'people.json', 'deniro.csv',
#               'playgrounds.csv', 'salary_data.csv',
#               'sorted_students_counts.csv', 'population.txt',
#               'data_merge.json']

# with ZipFile('files.zip', 'w') as zip_file:
#     for file in file_names:
#         zip_file.write(file)


"""№ 20 """

# from zipfile import ZipFile
# from os import path

# file_names = ['clue_exam_results.txt', 'clue_hungry_student.txt', 
#               'clue_students.txt', 'people.json', 'deniro.csv',
#               'playgrounds.csv', 'salary_data.csv',
#               'input.txt', 'population.txt',
#               'data_merge.json']

# with ZipFile('files.zip', 'a') as zip_file:
#     for file in filter(lambda x: path.getsize(x) < 386, file_names):
#         zip_file.write(file)


"""№ 21 Функция extract_this()"""

# from zipfile import ZipFile

# def extract_this(zip_name, *args):
#     with ZipFile(zip_name) as zip_file:
#         if args:
#             for file in args:
#                 zip_file.extract(file)
#         else:
#             zip_file.extractall()

"""№ 22 Шахматы были лучше 🌶️"""

# from zipfile import ZipFile
# import json


# def is_correct_json(string):
#     try:
#         json_data = json.loads(string)
#     except:
#         return False
#     return True


# with ZipFile('data.zip', 'a') as zip_file:
#     filenames = zip_file.namelist()
#     arsenal = []
#     for file in filenames:
#         if '.json' in file:
#             with zip_file.open(file) as json_file:
#                 try:
#                     json_data = json_file.read().decode('UTF-8')
#                     if is_correct_json(json_data):
#                         json_data = json.loads(json_data)
#                         print(f'{file} - корректный json файл')
#                         print(json_data)
#                         if json_data['team'] == 'Arsenal':
#                             arsenal.append([
#                                 json_data['first_name'], json_data['last_name']
#                             ])
#                     pass
            
#                 except:
#                     print(f'{file} - случилось какое то гавно')
# arsenal.sort(key=lambda x: x[1])
# arsenal.sort(key=lambda x: x[0])
# for name in arsenal:
#     print(name[0], name[1])

"""№ 23 Структура архива 🌶️🌶"""

# from zipfile import ZipFile

# with ZipFile('desktop.zip') as zip_file:
#     info = zip_file.infolist()
#     for file in info:
#         filepath = ''
#         name = file.filename
#         if file.is_dir():
#             indent = '  ' * (name.count('/') - 1)
#             name = name[name[:-2].rfind('/') + 1: -1]
#             print(indent + name)
#         else:
#             indent = '  ' * (name.count('/'))
#             name = name[name.rfind('/') + 1:]
#             sizes = {1: 'B', 2: 'KB', 3: 'MB', 4: 'GB'}
#             size = file.file_size
#             cnt = 1
#             while size // 1024:
#                 cnt += 1
#                 size /= 1024
#             size = ' ' + str(int(round(size, 0))) + ' ' + sizes[cnt]
#             print(indent + name + size)

"""№ 12 """

# import pickle

# dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 
#         'Balou': 10, 'Laika': 15}

# with open('dogs.pkl', mode='wb') as file:
#     pickle.dump(dogs, file)

"""№ 14 Ты не пройдешь"""

import pickle

def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as bin_file:
        for obj in objects:
            if type(obj) == typename:
                pickle.dumps(obj)

"""№ 15 Контрольная сумма"""

