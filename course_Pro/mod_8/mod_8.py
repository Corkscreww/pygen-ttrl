"""Блок 8. Рекурсия"""

"""Модуль 8.2
№ 5 Подозрительно просто"""

# def traffic(n):
#     def park(cnt):
#         if cnt > 0:
#             print('Не парковаться')
#             park(cnt - 1)

#     park(n)

# traffic(5)

"""№ 6 Подозрительно просто 🤐"""

# def sto(n):
#     def prnt(num):
#         if num <= n:
#             print(num)
#             prnt(num + 1)
#     prnt(1)

# sto(5)

"""№ 7"""

# import random

# numbers = [random.randint(-1000, 1000) for _ in range(100)]

# def vivod(nmbrs):
#     def prnt(num):
#         if num < len(nmbrs):
#             print(f'Элемент {num}: {nmbrs[num]}')
#             prnt(num + 1)
#     prnt(0)

# vivod(numbers)

"""№ 8 Обратный порядок"""

# with open('input.txt', encoding='UTF-8') as input_file:
#     numbers = [int(n.strip()) for n in input_file.readlines()]

# def obr(nums):
#     def prnt(num):
#         if num > -1 - len(nums):
#             print(nums[num])
#             prnt(num - 1)
#     prnt(-1)

# obr(numbers)

"""№ 9 Функция triangle() 😥"""

# def triangle(h):
#     def prnt(num):
#        if num > 0:
#            print('*' * num)
#            prnt(num - 1)
#     prnt(h)

# triangle(4)

"""№ 10 Функция triangle() 😰"""

# def triangle(h):
#     def prnt(num):
#        if num <= h:
#            print('*' * num)
#            prnt(num + 1)
#     prnt(1)

# triangle(4)


"""№ 11 Песочные часы"""

# def sand_clock(h):
#     def prnt(n):
#         if n > 0:
#             print(f'{" " * 2 * (h - n)} {str(h - n + 1) * n * 4}')
#             prnt(n - 1)
#             if n > 1:
#                 print(f'{" " * 2 * (h - n)} {str(h - n + 1) * n * 4}')
#     prnt(h)

# sand_clock(4)

"""№ 12 Фкнкция print_digits()"""

# def print_digits(number):
#     def prnt(n):
#         if n != 0:
#             print(n % 10)
#             prnt(n // 10)
#     prnt(number)

# print_digits(7)

"""№ 13 Фукнкция print_digits"""

# def print_digits(number):
#     def prnt(n, razr):
#         if n != 0:
#             r = 10 ** razr
#             print(n // r)
#             prnt(n % r, razr - 1)
#     prnt(number, len(str(number)) - 1)

# print_digits(2077)

"""Модуль 8.3 Решение задач на рекурсию
№ 6 Количество цифр"""

# def dig_num(num):
#     if num == 0:
#         return 0
#     else:
#         return 1 + dig_num(num // 10)

# print(dig_num(40))

"""№ 7 Сумма цифр"""

# def dig_num(num):
#     if num == 0:
#         return 0
#     else:
#         return num % 10 + dig_num(num // 10)

# print(dig_num(666))

"""№ 8 Функция number_of_frogs()"""

# def number_of_frogs(year):
#     if year == 1:
#         return 77
#     else:
#         return 3 * (number_of_frogs(year - 1) - 30)

# print(number_of_frogs(2))

"""№ 9 Функция range_sum()"""

# def range_sum(numbers, start, end):
#     if end != start:
#         return numbers[end] + range_sum(numbers, start, end - 1)
#     else:
#         return numbers[start]

"""№ 10 Обычное возведение в степень"""

# def get_pow(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * get_pow(a, n - 1)

# print(get_pow(2, 10))

"""№ 11 Быстрое возведение в степень   --   НЕ РЕШИЛ"""

# def get_fast_pow(a, n):
#     if n == 1:
#         return a
#     else:
#         if n % 2 == 0:
#             return get_fast_pow(get_fast_pow(a, 2), n // 2)
#         else:
#             return a * get_fast_pow(a, n - 1)

# print(get_fast_pow(2, 10))

"""№ 12 Функция recursive_sum()"""

# def recursive_sum(a, b):
#     if b == -a:
#         return 0
#     else:
#         return 1 + recursive_sum(a, b - 1)

# print(recursive_sum(99, 0))

"""№ 13 Функция is_power()"""

# def is_power(number):
#     if number == 1:
#         return True
#     elif number % 2 == 0:
#         return is_power(number // 2)
#     else:
#         return False

# print(is_power(513))

"""№ 14 Функция tribonacci()"""

# def tribonacci(n):
#     d = {1: 1, 2: 1, 3: 1}
#     result = d.get(n)
#     if result is None:
#         result = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
#         d[n] = result
#     return result

# print(tribonacci(4))

"""№ 15 Функция is_palindrome()"""

# def is_palindrome(string):
#     if string == '' or len(string) == 1:
#         return True
#     if string[0] == string[-1]:
#         is_palindrome(string[1: -1])
#     else:
#         return False
#     return True

# print(is_palindrome('122333221'))

"""№ 16 Функция to_binary"""

# def to_binary(number):
#     def prnt(n):
#         if n == 0 or n == 1:
#             print(n, end='')
#         else:
#             prnt(n // 2)
#             print(n % 2, end='')
#     prnt(number)
#     return ''

# print(to_binary(532))

"""№ 17 Без циклов"""

# def without_loops(num):
#     print(num)
#     def prnt(n):
#         if n <= 0:
#             pass
#         else:
#             print(n - 5)
#             prnt(n - 5)
#             print(n)
#     prnt(num)

# without_loops(73)

"""Блок 8.4"""
"""№ 4 Функция recursive_sum()"""

# def recursive_sum(nested_lists):
#     total = 0
#     for item in nested_lists:
#         if isinstance(item, list):
#             total += recursive_sum(item)
#         else:
#             total += item
#     return total


# my_list = [[12], [13], [53], [632], [6], [2342341]]
# print(recursive_sum(my_list))

"""№ 5 Функция linear()"""

# def linear(nested_lists):
#     total = []
#     for item in nested_lists:
#         if isinstance(item, list):
#             total.extend(linear(item))
#         else:
#             total.append(item)
#     return total


# my_list = [[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]]
# print(linear(my_list))

"""№ 6 Функция get_value()"""

# def get_value(nested_dict, key):
#     result = nested_dict.get(key)
#     if result is not None:
#         return result
#     else:
#         for kl, value in nested_dict.items():
#             if isinstance(value, dict):
#                 result = get_value(value, key)
#                 if result is not None:
#                     return result

# data = {'a': 11, 'b': {'c': 34, 'd': 2224, 'e': {'f': 5133, 'g': 609}}}

# print(get_value(data, 'a'))

"""№ 7 Функция get_all_values()"""

# def get_all_values(nested_dicts, key):
#     result = set()
#     rez = nested_dicts.get(key)
#     result.add(rez)
#     for kl, value in nested_dicts.items():
#         if isinstance(value, dict):
#             rez = get_all_values(value, key)
#             result.union(rez)
#             if rez is not None:
#                 return result

#     return result

# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur':
# {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_values(my_dict, 'top_grade')
# print(*sorted(result))

print(int(2.7))
print(round(2.7))