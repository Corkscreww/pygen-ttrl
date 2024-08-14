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

def interleave(*args):
    for arg in zip(*args):
        yield from (arg)

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]
print(*interleave(numbers, squares, qubes))