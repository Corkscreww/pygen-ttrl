"""МОДУЛЬ 9
БЛОК 9.3 Функции высшего порядка"""
"""№ 18 Функция verification()"""

# Цифры - 48 .. 57
# Загл лат буквы - 65 .. 90
# Строчные лат буквы - 97 .. 122

# def verification(login, password, success, failure):
#     result_lat = filter(lambda x: ord(x) in range(65, 91) or
#                         ord(x) in range(97, 123), password)
#     if not list(result_lat):
#         return failure(login, 'в пароле нет ни одной буквы')

#     result_zagl = filter(lambda x: ord(x) in range(65, 91), password)
#     if not list(result_zagl):
#         return failure(login, 'в пароле нет ни одной заглавной буквы')

#     result_str = filter(lambda x: ord(x) in range(97, 123), password)
#     if not list(result_str):
#         return failure(login, 'в пароле нет ни одной строчной буквы')

#     result_dig = filter(lambda x: ord(x) in range(48, 58), password)
#     if not list(result_dig):
#         return failure(login, 'в пароле нет ни одной цифры')

#     return success(login)


# def success(login):
#     print(f'Привет, {login}!')


# def failure(login, text):
#     print(f'{login}, попробуйте снова. Ошибка: {text}')


# verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)

"""Блок 9.4 Функции как объекты"""
"""№ 18 Функция remove_marks()"""

# def remove_marks(text, marks):
#     if remove_marks.__dict__.get('count'):
#         remove_marks.__dict__['count'] += 1
#     else:
#         remove_marks.__dict__['count'] = 1

#     for simv in marks:
#         text = text.replace(simv, '')
#     return text


# marks = '.,!?'
# text = 'Are you listening? Meet my family! There are my parents, my brother and me.'
# for mark in marks:
#     print(remove_marks(text, mark))

# print(remove_marks.count)

"""№ 16 Функция power()"""

# def power(degree):
#     def stepen(x):
#         return x ** degree
#     return stepen

# result = power(4)(2)
# print(result)

"""№ 17 Функция generator_square_polynom() """

# def generator_square_polynom(a, b, c):
#     k = 10
#     def generator(x):
#         return a * (x ** 2) + b * x + c
#     return generator

# f = generator_square_polynom(1, 2, 1)
# print(f(5))

"""№ 18 Функция sourcetemplate()"""

# def sourcetemplate(url):
#     def url_address(**kwargs):
#         result = url
#         if kwargs:
#             result += '?'
#             for arg in sorted(kwargs):
#                 result += str(arg) + '=' + str(kwargs[arg]) + '&'
#             result = result[:-1]
#         return result
#     return url_address

# url = 'https://beegeek.ru'
# load = sourcetemplate(url)
# print(load())

"""№ 19 Функция date_formatter()"""

# from datetime import date

# def date_formatter(country_code):
#     codes = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d',
#              'br': '%d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
#     def country_check(date):
#         return date.strftime(codes[country_code])
#     return country_check

# date_ru = date_formatter('us')
# today = date(2025, 1, 5)
# print(date_ru(today))

"""№ 20 Функция sort_priority()"""

# def sort_priority(values, group):
#     group = set(group)
#     new = set(values) - group
#     group = sorted(group)
#     new = sorted(new)
#     values.clear()
#     values[:] = group + new
#     pass

# numbers = [150, 200, 300, 1000, 50, 20000]
# sort_priority(numbers, [300, 100, 200])
# print(numbers)

"""Блок 9.6 Аннотации типов"""

"""№ 14 Функция get_digits()"""

# def get_digits(number: int | float) -> list:
#     return [int(dig) for dig in str(number).replace('.', '')]
# print(get_digits(13.909934))

"""№ 15 Функция top_grade()"""

# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, int]:
#     return {'name': grades['name'], 'top_grade': max(grades['grades'])}

# annotations = top_grade.__annotations__
# print(annotations['grades'])

"""№16 Функция  cyclic_shift()"""

# from collections import deque

# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     dq = deque(numbers, maxlen=len(numbers))
#     if step < 0:
#         for _ in range(step, 0):
#             dq.append(dq[0])
#     else:
#         for _ in range(step):
#             dq.appendleft(dq[-1])
#     numbers.clear()
#     numbers[:] = dq
#     numbers = list(dq)

# numbers = [234, 33, 4, 6, 2, 4, 75, 34, 1, 3, 6, 3, 3, 2, 54, 65, 7, 8, 9]
# cyclic_shift(numbers, -11)

# print(numbers)

"""№ 17 Функция matrix_to_dict()"""

# def matrix_to_dict(matrix: list[list[int]]) -> dict[int, list[int | float]]:
#     return {n + 1: [num for num in matrix[n]] for n in range(len(matrix))}

# matrix = [[5.1, 6, 7.94]]
# print(matrix_to_dict(matrix))

"""Блок 9.7 Декораторы. Часть 1"""

"""№ 19 Декоратор sandwich"""

# def sandwich(func):
#     def wrapper(*args, **kwargs):
#         print('---- Верхний ломтик хлеба ----')
#         func(*args, **kwargs)
#         print('---- Нижний ломтик хлеба ----')
#     return wrapper

# @sandwich
# def add_ingredients(ingredients):
#     for ing in ingredients:
#         spaces = ' ' * ((30 - len(ing)) // 2)
#         print(spaces + ing)

# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

"""№ 20 Новый print"""

# from builtins import print as base_print

# def uper(func):
#     def wrapper(*args, sep=' ', end='\n'):
#         result = ''
#         for text in args:
#             result += str(text).upper() + str(sep).upper()
#         result = result[:-len(sep)]
#         #result += str(end).upper()
#         func(result, end=str(end).upper())
#     return wrapper

# @uper
# def print(*args, sep=' ', end='\n'):
#     base_print(*args, sep=sep, end=end)

# print('aaa', 'bbb', 'CCC', sep='xxx', end='stepik')
# print('aaa', 'bbb', 'CCC', sep='--', end='python')
# print('aaa', 'bbb', 'CCC', sep='qqq', end='!')

"""# 21 Декоратор do_twice"""

# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, *kwargs)
#         func(*args, *kwargs)
#         return func(*args, *kwargs)
#     return wrapper

# @do_twice
# def beegeek():
#     return 'beegeek'

# print(beegeek())

"""№ 22 Декоратор reverse_args"""

# def reverse_args(func):
#     def wrapper(*args, **kwargs):
#         args = list(args)
#         args.reverse()
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper

# @reverse_args
# def operation(a, b):
#     return a // b

# try:
#     print(operation(0, 70))
# except ZeroDivisionError:
#     print('ZeroDivisionError')

"""№ 23 Декоратор exception_decorator"""

# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return (func(*args, **kwargs), 'Функция выполнилась без ошибок')
#         except:
#             return (None, 'При вызове функции произошла ошибка')
#     return wrapper

# @exception_decorator
# def f(x, y):
#     return x * y

# print(f('stepik', 10))

"""№ 24 Декоратор takes_positive"""

# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         usl = len(list(filter(lambda x: isinstance(x, int), args)))
#         if usl != len(args):
#             raise TypeError
#         usl = len(list(filter(lambda x: x < 1, args)))
#         if usl:
#             raise ValueError
#         func(*args, **kwargs)
#         return func(*args, *kwargs)
#     return wrapper

# @takes_positive
# def positive_sum(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())

# try:
#     print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep='40'))
# except Exception as err:
#     print(type(err))

"""БЛОК 9.8 Декораторы. Часть 2"""

""" Шаблон декоратора

import functools

def (func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

"""
"""№ 9 Декоратор square"""

# import functools

# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) ** 2
#     return wrapper

# @square
# def add(a, b):
#     '''прекрасная функция'''
#     return a + b
# print(add(1, 1))
# print(add.__name__)
# print(add.__doc__)

"""№ 10 Декоратор returns_string"""

# import functools

# def returns_string(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if not isinstance(func(*args, **kwargs), str):
#             raise TypeError
#         return func(*args, **kwargs)
#     return wrapper

# @returns_string
# def add(a, b):
#     return a + b

# try:
#     print(add(3, 7))
# except TypeError as e:
#     print(type(e))

"""№ 11 Декоратор trace"""

# import functools

# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         name = func.__name__
#         arg = tuple([arg for arg in args])
#         value = func(*args, **kwargs)
#         kwarg = {kwarg: kwargs[kwarg] for kwarg in kwargs}
#         print(f'TRACE: вызов {name}() с аргументами: {arg}, {kwarg}')
#         print(f'TRACE: возвращаемое значение {name}(): {value}')
#         return func(*args, **kwargs)
#     return wrapper

# @trace
# def func(nums, degree=3):
#     '''прекрасная функция'''
#     return list(i**degree for i in nums)

# print(func.__name__)
# print(func.__doc__)
# func([1, 2, 3, 4, 5, 6], degree = 5)

"""
Шаблон декоратора с аргументами

import functools

def ():
    def (func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return
"""

"""№ 17 Декоратор prefix"""

# def prefix(string, to_the_end=False):
#     def add_prefix(func):
#         def wrapper(*args, **kwargs):
#             if to_the_end:
#                 return func(*args, **kwargs) + string
#             else:
#                 return string + func(*args, **kwargs)
#         return wrapper
#     return add_prefix

# @prefix('$$$', to_the_end=True)
# def get_bonus():
#     return '2000'
# print(get_bonus())

"""№ 18 Декоратор make_html """

# import functools

# def make_html(tag):
#     def add_tag(func):
#         @functools.wraps(func)
#         def wrapper(txt):
#             new_tag = f'<{tag}>'
#             return new_tag + func(txt) + new_tag[:1] + '/' + new_tag[1:]
#         return wrapper
#     return add_tag

# @make_html('del')
# def get_text(text):
#     return text
# print(get_text('Python'))

"""№ 19 Декоратор repeat"""

# import functools


# def repeat(times):
#     def loop_times(func):
#         @functools.wraps(func)
#         def wrapper():
#             for _ in range(times):
#                 func()
#         return wrapper
#     return loop_times

# @repeat(4)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
# print(say_beegeek.__name__)
# print(say_beegeek.__doc__)

"""№ 20 Декоратор strip_range"""

# import functools

# def strip_range(start, end, char='.'):
#     def replace(func):
#         @functools.wraps(func)
#         def wrapper():
#             value = func()
#             ln = len(value)
#             value = value[:start] + (end - start) * char + value[end:]
#             return value[:ln]
#         return wrapper
#     return replace

# @strip_range(3, 20, '_')
# def beegeek():
#     return 'beegeek'
# print(beegeek())

"""№ 21 Декоратор returns"""

# import functools

# def returns(datatype):
#     def proverka(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if not isinstance(func(*args, **kwargs), datatype):
#                 raise TypeError
#             return func(*args, **kwargs)
#         return wrapper
#     return proverka

# @returns(list)
# def append_this(li, elem):
#     '''append_this docs'''
#     return li + [elem]
# print(append_this.__name__)
# print(append_this.__doc__)
# print(append_this([1, 2, 3], elem=4))

"""№ 22 Декоратор takes"""

# import functools

# def takes(*types):
#     def proverka(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for arg in args:
#                 if type(arg) not in types:
#                     raise TypeError
#             return func(*args, **kwargs)
#         return wrapper
#     return proverka

# @takes(list, bool, float, int)
# def repeat_string(string, times):
#     return string * times
# try:
#     print(repeat_string('bee', 4))
# except TypeError as e:
#     print(type(e))

"""№ 23 Декоратор add_attrs    --   НЕ ПОЛУЧИЛОСЬ"""

# import functools

# def add_attrs(**kwargs):
#     def add(func):
#         @functools.wraps(func)
#         def wrapper():
#             print(func.__dict__)
#             for kwarg in kwargs:
#                 setattr(func, kwarg, kwargs[kwarg])
#             print(func.__dict__)
#             return func()
#         return wrapper
#     return add

# @add_attrs(attr1='bee', attr2='geek')
# def beegeek():
#     return 'beegeek'


# print(beegeek())
# print(beegeek.attr1)

"""№ 24 Декоратор ignore_exception   --  ТОЖЕ НАДО РАЗОБРАТЬСЯ"""

# import functools, sys

# def ignore_exception(*args):
#     def ignore(func):
#         @functools.wraps(func)
#         def wrapper(*a, **k):
#             try:
#                 result = func(*a, **k)
#                 return result
#             except Exception as err:
#                 for arg in args:
#                     b = arg is err
#                     if arg == err:
#                         raise err('fsdafasdf')
#         return wrapper
#     return ignore

# @ignore_exception(ZeroDivisionError, TypeError, ValueError)
# def f(x):
#     return 1 / x
# f(0)

"""№ 25 Декоратор retry"""

"""Блок 9.9 Модуль functools"""

"""№ 11 Две функции"""

# from functools import partial

# def send_email(name, email_address, text):
#     pass

# to_Timur = partial(
#     send_email, 'Timur', 'timyrik20@begeek.ru'
# )

# send_an_invitation = partial(
#     send_email, '', '', text='Школа BEEGEEK приглашает Вас на новый курс по пр'
#     'ограммированию на языке Python. тутут....'
# )

# to_Timur(text='fsdafsa')
# b = send_an_invitation.keywords
# print(b)

from functools import lru_cache

@lru_cache
def word_mod(word):
    result = ''
    for ch in sorted(word):
        result += ch
    return result

with open('input.txt', encoding='UTF-8') as input_file:
    data = [st.strip() for st in input_file.readlines()]

for word in data:
    print(word_mod(word))

print(word_mod.cache_info().hits)
print(word_mod.cache_info().misses)
print(word_mod.cache_info().currsize)