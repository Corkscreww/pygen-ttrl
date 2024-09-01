"""Модуль 10 Итераторы и генераторы"""

"""Блок 10.2 Итераторы. Часть 2"""

"""№ 20 Функция filterfalse()"""

# def filterfalse(predicate, iterable):
#     if predicate is not None:
#         func = lambda x: True if predicate(x) == False else False
#     else:
#         func = lambda x: True if not x else False
#     return filter(func, iterable)


# numbers = [1, 2, 3, 4, 5]
# print(*filterfalse(lambda x: x >= 3, numbers))

"""№ 21 Функция transpose()"""

# def transpose(matrix):
#     result = []
#     for stolb in zip(*matrix):
#         result.append([val for val in stolb])
#     return result

# matrix = [[1, 2, 3, 4, 5],
# [6, 7, 8, 9, 10]]
# for row in transpose(matrix):
#     print(row)

"""№ 22 Функция get_min_max()"""

# def get_min_max(data):
#     return (min(enumerate(data), key=lambda x: x[1])[0],
#             max(enumerate(data), key=lambda x: x[1])[0])

# data = [9]
# print(get_min_max(data))

"""№ 24 Функция strmap() ??????? хуй знает ваще чё такое"""
"""
# def starmap(func, iterable):
#     print(*iterable)
#     return list(map(func, iterable))

# pairs = [(1, 3), (2, 5), (6, 4)]

# print(*starmap(lambda a, b: a + b, pairs))

# def starmap(func, iterable):
#     print(*iterable)
#     return list(map(func, *iterable))

# points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
# for x, y, z in points:
#     print(x, y, z)
# print(starmap(lambda x, y, z: x * y * z, points))

"""
"""Блок 10.3 Итераторы. Часть 3"""

"""№ 14 Функция is_iterable()"""

# def is_iterable(obj):
#     return ('__iter__' in dir(obj))

# objects = [(1, 13), 7.0004, [1, 2, 3]]
# for obj in objects:
#     print(is_iterable(obj))

"""№ 15 is_iterator()"""

# def is_iterator(obj):
#     return (iter(obj) == obj)

# print(is_iterator([1, 2, 3, 4, 5]))

"""№ 16 Функция random_numbers()"""

# from random import choice
# def random_numbers(left, right):
#     def rand():
#         nonlocal right
#         if left == right:
#             right += 1
#         return choice(range(left, right))
#     return iter(rand, 'хуй')

# iterator = random_numbers(1, 1)
# print(next(iterator))
# print(next(iterator))

"""Блок 10.4. Итераторы. Часть 4 """

"""№ 7 Итератор Repeater"""

# class Repeater:
#     def __init__(self, obj):
#         self.obj = obj

#     def __iter__(self):
#         return self

#     def __next__(self):
#         return self.obj


# geek = Repeater('geek')
# print(next(geek))
# print(next(geek))
# print(next(geek))

"""№ 8 Итератор BoundedRepeater"""

# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.times -= 1
#         if self.times < 0:
#             raise StopIteration
#         else:
#             return self.obj

# geek = BoundedRepeater('geek', 3)
# print(next(geek))
# print(next(geek))
# print(next(geek))
# try:
#     print(next(geek))
# except StopIteration:
#     print('Error')

"""№ 9 Итератор Square"""

# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index += 1
#         if self.index > self.n:
#             raise StopIteration
#         else:
#             return pow(self.index, 2)

# squares = Square(10)
# print(list(squares))

"""№ 10 Итератор Fibonacci"""

# class Fibonacci:
#     def __init__(self):
#         self.n = 1
#         self.nn = 1
#         self.sled = 0
#         self.ind = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.ind < 3:
#             self.ind += 1
#             return self.n
#         else:
#             self.sled = self.n + self.nn
#             self.n, self.nn = self.nn, self.sled
#             return self.sled

# fibonacci = Fibonacci()
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))

"""№ 11 Итератор PowerOf"""

# class PowerOf:
#     def __init__(self, number):
#         self.number = number
#         self.power = -1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.power += 1
#         return pow(self.number, self.power)

# power_of_two = PowerOf(2)
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))

"""№ 12 Итератор DictItemsIterator"""

# class DictItemsIterator:
#     def __init__(self, data: dict):
#         self.data = data
#         self.keys = iter(data.keys())
#         self.key = 0
#         self.val = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         key = next(self.keys)
#         val = self.data[key]
#         return (key, val)


# data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
# pairs = DictItemsIterator(data)
# print(*pairs)

"""№ 13 Итератор CardDeck"""

# class CardDeck:
#     def __init__(self):
#         self.mast = ['пик', "треф", 'бубен', 'червей']
#         self.kard = ['двойка', 'тройка', 'четверка', 'пятерка', 'шестерка',
#                      'семерка', 'восьмерка', 'девятка', 'десятка', 'валет',
#                      'дама', 'король', 'туз']
#         self.ind_k = -1
#         self.ind_m = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.ind_k += 1

#         if self.ind_k == 13:
#             self.ind_k = 0
#             self.ind_m += 1

#         if self.ind_m == 4:
#             raise StopIteration

#         return self.kard[self.ind_k] + ' ' + self.mast[self.ind_m]

# cards = list(CardDeck())
# print(cards[9])
# print(cards[23])
# print(cards[37])
# print(cards[51])

"""№ 14 Итератор Cycle"""

# class Cycle:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.iterator = iter(iterable)
#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             return next(self.iterator)
#         except StopIteration:
#             self.iterator = iter(self.iterable)
#             return next(self.iterator)


# cycle = Cycle(range(100_000_000))
# print(next(cycle))
# print(next(cycle))

"""№ 15 Итератор RandomNumbers"""

# from random import randint

# class RandomNumbers:
#     def __init__(self, left, right, n):
#         self.left = left
#         self.right = right
#         self.n = n

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.n == 0:
#             raise StopIteration
#         else:
#             return randint(self.left, self.right)

# iterator = RandomNumbers(1, 10, 2)
# print(next(iterator) in range(1, 11))
# print(next(iterator) in range(1, 11))

"""№ 16 Итератор Alphabet 🌶"""

# from random import randint

# class Alphabet:
#     def __init__(self, language):
#         self.language = language
#         self.lang = {'en': range(97, 123), 'ru': range(1072, 1104)}
#         self.current_index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         code = self.lang[self.language][self.current_index]
        #   self.current_index = (self.current_index +
        #                         1) % len(self.lang[self.language])
#         return chr(code)

# en_alpha = Alphabet('ru')
# letters = [next(en_alpha) for _ in range(33)]
# print(*letters)

"""№ 17 Итератор Xrange🌶️"""

# class Xrange:
#     def __init__(self, start, end, step=1):
#         self.start = start - step
#         self.end = end
#         self.step = step

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.start += self.step
#         if self.step > 0:
#             if self.start >= self.end:
#                 raise StopIteration
#             else:
#                 return self.start
#         else:
#             if self.start <= self.end and self.step < 0:
#                 raise StopIteration
#             else:
#                 return self.start

# xrange = Xrange(10, 1, -1)
# print(*xrange)

"""Блок 10.5 Генераторы. Часть 1"""

"""№ 15 Функция simple_sequence()"""

# def simple_sequence():
#     n = 1
#     while True:
#         for i in range(1, n + 1):
#             yield n
#         n += 1


# generator = simple_sequence()
# numbers = [next(generator) for _ in range(10)]
# print(*numbers)

"""№ 16 Функция alternating_sequence()"""

# def alternating_sequence(count=None):
#     n = 1
#     while True:
#         if count is not None:
#             if n == count + 1:
#                 break
#             else:
#                 yield n * (-1) ** (n % 2 + 1)
#                 n += 1
#         else:
#             yield n * (-1) ** (n % 2 + 1)
#             n += 1


# generator = alternating_sequence()
# print(next(generator))
# print(next(generator))

"""№ 17 Функция primes()"""

# def primes(left, right):
#     if left == 1:
#         left += 1
#     while left < right:
#         prost = True
#         for num in range(2, left):
#             if left % num == 0:
#                 prost = False
#                 break
#         if prost:
#             yield left
#         left += 1

# generator = primes(6, 36)
# print(next(generator))
# print(next(generator))

"""№ 18 Функция reverse()"""

# def reverse(sequence):
#     sequence = list(sequence)
#     sequence.reverse()
#     for n in sequence:
#         yield n

# generator = reverse(list('HFJDHFjd23423i942313223hfjhfdJSHFJD656754964HF'))

# print(type(generator))
# print(*generator)

"""№ 19 Функция dates()"""

# from datetime import date
# from datetime import timedelta

# def dates(start, count=None):
#     td = timedelta(days=1)
#     while True:
#         if count is not None:
#                 if count == 0:
#                      break
#                 else:
#                      yield start
#                      start += td
#                      count -= 1
#         else:
#              yield start
#              start += td

# generator = dates(date(2022, 3, 8), 5)
# for n in generator:
#      print(n, end=' ')

"""№ 20 Функция card_deck()"""

# def card_deck(suit):
#     dostoinstvo = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
#                    'валет', 'дама', 'король', 'туз']
#     masti = ['пик', 'треф', 'бубен', 'червей']
#     while True:
#         for mast in masti:
#             if mast == suit:
#                 continue
#             else:
#                 for dost in dostoinstvo:
#                     yield dost + ' ' + mast

# generator = card_deck('треф')
# cards = [next(generator) for _ in range(40)]
# print(*cards)

"""№ 25 Функция matrix_by_elem()"""

# def matrix_by_elem(matrix):
#     for stroka in matrix:
#         yield from stroka

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# print(*matrix_by_elem(matrix))

"""№ 26 Функция palindromes()"""

# def palindromes():
#     n = 1
#     while True:
#         if str(n) == str(n)[::-1]:
#             yield n
#             n += 1

# generator = palindromes()
# numbers = [next(generator) for _ in range(30)]
# print(*numbers)

"""№ 27 Функция flatten()"""

# def flatten(nested_list):
#     for elem in nested_list:
#         b = type(elem)
#         if b == int:
#             yield elem
#         elif b == list:
#             yield from flatten(elem)

# generator = flatten([1, 2, 3, 4, 5, 6, 7])
# print(*generator)

"""Блок 10.6 Генераторы. Часть 2"""

"""№ 15 Функция cubes_of_odds()"""

# def cubes_of_odds(iterable):
#     yield from (num ** 3 for num in iterable if num % 2 == 1)

# evens = [2, 4, 6, 8, 10]
# print(list(cubes_of_odds(evens)))

"""№ 16 Функция is_prime()"""

# def is_prime(number):
#     if number == 1:
#         return False
#     return all(number % num != 0
#                for num in range(2, number))

# print(is_prime(1))

"""№ 17 Функция count_iterable()"""

# def count_iterable(iterable):
#     return len(list(iterable))

# data = tuple(range(432, 3845, 17))
# print(count_iterable(data))

"""№ 18 Функция all_together()"""

# def all_together(*args):
#     for arg in args:
#         yield from (arg)

# objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]
# print(*all_together(*objects))

"""№ 19 Функция interleave()"""

# def interleave(*args):
#     for arg in zip(*args):
#         yield from (arg)

# numbers = [1, 2, 3]
# squares = [1, 4, 9]
# qubes = [1, 8, 27]
# print(*interleave(numbers, squares, qubes))

"""БЛОК 10.7 Генераторы. Часть 3"""

"""№ 6 Функция parse_ranges()"""

# def parse_ranges(inp):
#     ranges = inp.split(',')
#     grani = (rang.split('-') for rang in ranges)
#     ranges = (range(int(a), int(b) + 1) for a, b in grani)
#     for rang in ranges:
#         yield from rang

# print(*parse_ranges('1-10,2-10'))

"""№ 7 Функция filter_names()"""

# def filter_names(names, ignore_char, max_names):
#     name_list = (
#         name for name in names
#         if name[0].lower() != ignore_char.lower() and
#         name.isalpha()
#         )
#     if max_names > len(names):
#         yield from name_list
#     else:
#         for _ in range(max_names):
#             yield next(name_list)

# data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German',
# 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']
# print(*filter_names(data, 'A', 100))

"""№ 8 Инвестиции"""

# with open('data.csv', encoding='UTF-8') as inp_csv:
#     data = (line.strip().split(',') for line in inp_csv)
#     next(data)
#     summ = sum(int(line[1]) for line in data if line[2] == 'a')
# print(summ)

"""№ 9 Функция years_days()"""

# from datetime import date, timedelta

# def years_days(year):
#     td = timedelta(days=1)
#     dat = date(year, 1, 1)
#     while dat.year == year:
#         yield dat
#         dat += td

# dates = years_days(1900)

# print(*dates)

"""№ 10 Функция nonempty_lines()"""

# def nonempty_lines(file):
#     with open(file, encoding='UTF-8') as inp_file:
#         lines = (line.strip() for line in inp_file if line.strip() != '')
#         for line in lines:
#             if len(line) > 25:
#                 yield '...'
#             else:
#                 yield line

# lines = nonempty_lines('file1.txt')
# print(next(lines))
# print(next(lines))
# print(next(lines))

"""№ 11 Функция txt_to_dict()"""

# def txt_to_dict():
#     with open('planets.txt', encoding='UTF-8') as inp_file:
#         element = []
#         elements = []
#         for line in inp_file:
#             line = line.strip().split()
#             if line != []:
#                 element.append((line[0], line[2]))
#             else:
#                 yield dict(element)
#                 elements.append(dict(element))
#                 element = []
#         yield dict(element)

# planets = txt_to_dict()

# print(*planets)

"""№ 19 Функция unique()"""

# def unique(iterable):
#     it_set = set()
#     for el in iterable:
#         if el not in it_set:
#             yield el
#             it_set.add(el)


# iterator = iter('111222333')
# uniques = unique(iterator)
# print(next(uniques))
# print(next(uniques))
# print(next(uniques))

"""№ 20 Функция stop_on()"""

# def stop_on(iterable, obj):
#     try:
#         iterable = iter(iterable)
#         el = next(iterable)
#         while el != obj:
#             yield el
#             el = next(iterable)
#     except StopIteration:
#         pass

# iterator = iter('beegeek')
# print(*stop_on(iterator, 'a'))

"""№ 21 Функция with_previous()"""

# def with_previous(iterable):
#     iterable = list(iterable)
#     iter2 = iter(iterable)
#     iterable = iter(iterable)
#     yield (next(iterable), None)
#     yield from ((el1, next(iter2)) for el1 in iterable)

# numbers = [1, 2, 3, 4, 5]
# print(*with_previous(numbers))

"""№ 22 Функция pairwise()"""

# def pairwise(iterable):
#     it = list(iterable)
#     iter2 = iter(it)
#     iterable = iter(it)
#     next(iter2)
#     for el1 in iterable:
#         try:
#             yield (el1, next(iter2))
#         except StopIteration:
#             yield (it[-1], None)



# iterator = iter('stepik')
# print(*pairwise(iterator))

"""№ 23 Функция around()"""

# def around(iterable):
#     it = list(iterable)
#     iter_prev = iter(it)
#     iter_post = iter(it)
#     iterable = iter(it)
#     next(iter_post)
#     yield (None, next(iterable), next(iter_post))
#     for el in iterable:
#         try:
#             yield (next(iter_prev), el, next(iter_post))
#         except StopIteration:
#             yield(it[-2], it[-1], None)

# numbers = [1, 2, 3, 4, 5]
# print(*around(numbers))

"""БЛОК 10.8 itertools. Часть 1."""

"""№ 15 tabulate()"""

# from itertools import count

# def tabulate(func):
#     yield from (func(arg) for arg in count(1))

# func = lambda x: x + 10
# values = tabulate(func)
# print(next(values))
# print(next(values))
# print(next(values))

"""№ 16 Функция factorials()"""

# from itertools import accumulate
# from math import factorial
# import operator

# def factorials(n):
#     yield from accumulate(range(1, n + 1), func=operator.mul)

# numbers = factorials(2)
# print(next(numbers))
# print(next(numbers))

"""№ 17 Функция alnum_sequence()     - НЕ РЕШИЛ"""

# from itertools import starmap, cycle

# def alnum_sequence():
#     numbers = cycle([range(1, 27)])
#     letters = cycle(([chr(num + 64) for num in range(1, 27)]))
#     yield next(numbers)
    # yield next(letters)
#     cycle_iter = cycle([0, 1])
#     print(next(cycle_iter), next(cycle_iter), next(cycle_iter), next(cycle_iter),
# next(cycle_iter))

# alnum = alnum_sequence()
# # print(next(alnum))
# print(*(next(alnum) for _ in range(2)))
# pass

"""№ 18 Функция roundrobin()    - НЕ РЕШИЛ"""

# from itertools import starmap

# def roundrobin(*args):
#     for n in zip(args):
#         print(n)

# print(*roundrobin('abc', 'd', 'ef'))

"""БЛОК 10.9 Модуль itertools. Часть 2"""

"""№ 12 Функция drop_while_negative()"""

# from itertools import dropwhile

# def drop_while_negative(iterable):
#     yield from (dropwhile(lambda x: x < 0, iterable))

# numbers = [-3, -2, -1, 0, 1, 2, 3]
# print(*drop_while_negative(numbers))

"""№ 13 Функция drop_this()"""

# from itertools import dropwhile

# def drop_this(iterable, obj):
#     yield from(dropwhile(lambda x: x == obj, iterable))

# numbers = [0, 0, 0, 1, 2, 3]
# print(*drop_this(numbers, 0))

"""№ 14 Функция first_true()"""

# from itertools import dropwhile, compress

# def first_true(iterable, predicate):
#     if predicate is None:
#         predicate = bool
#     return list(dropwhile(lambda x: not predicate(x), iterable))[0]

# numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
# print(first_true(numbers, None))

"""№ 15 Функция take()"""

# from itertools import compress

# def take(iterable, n):
#     sel = (True for _ in range(n))
#     yield from (compress(iterable, sel))

# iterator = iter('beegeek')
# print(*take(iterator, 1))

"""№ 16 Функция take_nth()"""

# from itertools import islice

# def take_nth(iterable, n):
#     try:
#         return next(islice(iterable, n - 1, n))
#     except StopIteration:
#         pass

# iterator = iter('beegeek')

# iterator = iter('beegeek')

# print(take_nth(iterator, 7))

"""№ 17 Функция first_largest()"""

# from itertools import takewhile

# def first_largest(iterable, number):
#     kk = enumerate(list(takewhile(lambda x: x < number, iterable)))
#     res = 0
#     check = False
#     for ind, val in kk:
#         if val < number:
#             check = True
#         res = ind
#     if res != 0:
#         res += 1
#     if check:
#         return res
#     else:
#         return -1

# iterator = iter([-400, -100, -102, -334, -5])

# print(first_largest(iterator, -6))

"""Блок 10.10 Модуль itertools. Часть 3"""

"""№ 13 Функция sum_of_digits()"""

# from functools import reduce
# from itertools import accumulate, starmap

# def sum_of_digits(iterable):
#     return reduce(
#         lambda x, y: int(x) + int(y),
#         reduce(lambda x,y: str(x) + str(y), iterable)
#     )

# print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

"""№ 14 Функция is_rising()"""

# from itertools import pairwise, starmap

# def is_rising(iterable):
#     return all(starmap(lambda x, y: x < y, pairwise(iterable)))

# iterator = iter(list(range(100, 200)))
# print(is_rising(iterator))

"""№ 15 Функция max_pair()"""

# from itertools import starmap, pairwise

# def max_pair(iterable):
#     return max(starmap(lambda x,y: x + y, pairwise(iterable)))

# iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
# print(max_pair(iterator))

"""№ 16 Функция ncycles()"""

# from itertools import tee, starmap, repeat

# def ncycles(iterable, times):
#     for it in tee(iterable, times):
#         yield from (it)

# iterator = iter([1])
# print(*ncycles(iterator, 10))

"""№ 17 Функция grouper()"""

# def grouper(iterable, n):
#     try:
#         iterable = iter(iterable)
#         while True:
#             tup = []
#             for i in range(n):
#                 tup.append(next(iterable))
#             yield tuple(tup)
#     except StopIteration:
#         if tup:
#             for _ in range(n - len(tup)):
#                 tup.append(None)
#             yield tuple(tup)



# iterator = iter([1, 2, 3])
# print(*grouper(iterator, 5))

"""БЛОК 10.11 Модуль itertools часть 4"""

"""№ 10 """

# from collections import namedtuple
# from itertools import groupby

# Person = namedtuple('Person', ['name', 'age', 'height'])

# persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
#            Person('Mark', 71, 172), Person('Alex', 45, 193),
#            Person('Jeff', 63, 193), Person('Ryan', 41, 184),
#            Person('Ariana', 28, 158), Person('Liam', 69, 193)]

# persons.sort(key=lambda x: x.height)
# groups = groupby(persons, lambda x: x.height)

# for rost, group in groups:
#     print(f'{rost}: ', end='')
#     spisok = ''
#     for person in sorted(list(group)):
#         spisok += person.name + ', '
#     print(spisok[:len(spisok) - 2])

"""№ 11"""

# from collections import namedtuple
# from itertools import groupby, starmap

# Student = namedtuple('Student', ['surname', 'name', 'grade'])

# students = [Student('Гагиев', 'Александр', 10),
#             Student('Дедегкаев', 'Илья', 11),
#             Student('Кодзаев', 'Георгий', 10),
#             Student('Набокова', 'Алиса', 11),
#             Student('Кораев', 'Артур', 10),
#             Student('Шилин', 'Александр', 11),
#             Student('Уртаева', 'Илина', 11),
#             Student('Салбиев', 'Максим', 10),
#             Student('Капустин', 'Илья', 11),
#             Student('Гудцев', 'Таймураз', 11),
#             Student('Перчиков', 'Максим', 10),
#             Student('Чен', 'Илья', 11),
#             Student('Елькина', 'Мария', 11),
#             Student('Макоев', 'Руслан', 11),
#             Student('Албегов', 'Хетаг', 11),
#             Student('Щербак', 'Илья', 10),
#             Student('Идрисов', 'Баграт', 11),
#             Student('Гапбаев', 'Герман', 10),
#             Student('Цивинская', 'Анна', 10),
#             Student('Туткевич', 'Юрий', 11),
#             Student('Мусиков', 'Андраник', 11),
#             Student('Гадзиев', 'Георгий', 11),
#             Student('Белов', 'Юрий', 11),
#             Student('Акоева', 'Диана', 11),
#             Student('Денисов', 'Илья', 11),
#             Student('Букулова', 'Диана', 10),
#             Student('Акоева', 'Лера', 11)]

# groups = groupby(sorted(students, key=lambda x: x.name), key=lambda x: x.name)
# mx = starmap(lambda x, y: (x, len(list(y))), groups)

# print(max(mx, key=lambda x: (x[1]))[0])

"""№ 12 Группы слов"""

# from itertools import groupby

# with open('349/7', encoding='UTF-8') as file:
#     words = next(file).split()

# groups = groupby(sorted(words, key=lambda x: len(x)), key=lambda x: len(x))

# for leng, words in groups:
#     print(leng, '->', *words)

"""№ 13 Нет дел"""

# from itertools import groupby

# tasks = [('Отдых', 'поспать днем', 3),
#         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
#         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
#         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
#         ('Отдых', 'погулять вечером', 4),
#         ('Курс по ооп', 'обсудить темы', 1),
#         ('Урок по groupby', 'добавить задачи на программирование', 3),
#         ('Урок по groupby', 'написать конспект', 1),
#         ('Отдых', 'погулять днем', 2),
#         ('Урок по groupby', 'добавить тестовые задачи', 2),
#         ('Уборка', 'убраться в ванной', 2),
#         ('Уборка', 'убраться в комнате', 1),
#         ('Уборка', 'убраться на кухне', 3),
#         ('Отдых', 'погулять утром', 1),
#         ('Курс по ооп', 'обсудить задачи', 2)]

# tasks.sort(key=lambda x: x[0])
# tasks = groupby(tasks, key=lambda x: x[0])
# for delo, acts in tasks:
#     print(delo + ':')
#     for act in sorted(list(acts), key=lambda x: x[2]):
#         print(f'    {act[2]}. {act[1]}')

"""№ 14 Функция group_anagrams()"""

# from itertools import groupby

# def group_anagrams(words):
#     words.sort(key=lambda x: sorted(list(x)))
#     words = groupby(words, key=lambda x: sorted(list(x)))
#     result = []
#     for anogr, wrds in words:
#         result.append(tuple([word for word in wrds]))
#     return result

# groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

# print(*groups)

"""№ 15 Функция ranges()"""

# from itertools import groupby, pairwise

# def ranges(numbers):
#     pairs = pairwise(numbers)
#     numbers = groupby(pairs, key=lambda x: x[0] == x[1] - 1)
#     result = []
#     pred = False
#     buf = None
#     for gr, nm in numbers:
#         diap = list(nm)
#         if gr:
#             if buf and not pred and diap[0][0] != buf:
#                 result.append((buf, buf))
#             pass
#             result.append((diap[0][0], diap[-1][-1]))
#             pred = True
#             pass
#         else:
#             for dp in diap:
#                 if not pred:
#                     result.append((dp[0], dp[0]))
#             pred = False
#             buf = diap[0][1]

#     if not gr:
#         result.append((dp[1], dp[1]))

#     return result
# numbers = list(range(10, 21)) + [30] + list(range(35, 101)) + list(range(1000, 1001))

# print(ranges(numbers))
