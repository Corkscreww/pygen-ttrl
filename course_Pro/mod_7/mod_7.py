"""Блок 7.2 Обработка исключений

Дерево встроенных исключений

BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
    +-- StopAsyncIteration
    +-- ArithmeticError
    |    +-- FloatingPointError
    |    +-- OverflowError
    |    +-- ZeroDivisionError
    +-- AssertionError
    +-- AttributeError
    +-- BufferError
    +-- EOFError
    +-- ImportError
    +-- ModuleNotFoundError
    +-- LookupError
    |    +-- IndexError
    |    +-- KeyError
    +-- MemoryError
    +-- NameError
    |    +-- UnboundLocalError
    +-- OSError
    |    +-- BlockingIOError
    |    +-- ChildProcessError
    |    +-- ConnectionError
    |    |    +-- BrokenPipeError
    |    |    +-- ConnectionAbortedError
    |    |    +-- ConnectionRefusedError
    |    |    +-- ConnectionResetError
    |    +-- FileExistsError
    |    +-- FileNotFoundError
    |    +-- InterruptedError
    |    +-- IsADirectoryError
    |    +-- NotADirectoryError
    |    +-- PermissionError
    |    +-- ProcessLookupError
    |    +-- TimeoutError
    +-- ReferenceError
    +-- RuntimeError
    |    +-- NotImplementedError
    |    +-- RecursionError
    +-- SyntaxError
    |    +-- IndentationError
    |        +-- TabError
    +-- SystemError
    +-- TypeError
    +-- ValueError
    |    +-- UnicodeError
    |        +-- UnicodeDecodeError
    |        +-- UnicodeEncodeError
    |        +-- UnicodeTranslateError
    +-- Warning
        +-- DeprecationWarning
        +-- PendingDeprecationWarning
        +-- RuntimeWarning
        +-- SyntaxWarning
        +-- UserWarning
        +-- FutureWarning
        +-- ImportWarning
        +-- UnicodeWarning
        +-- BytesWarning
        +-- ResourceWarning
"""


"""№ 23 Only Numbers"""

# with open('input.txt') as input_data:
#     data = input_data.readlines()

# not_num = 0
# sum = 0
# for num in data:
#     try:
#         sum += int(num.strip())
#     except ValueError:
#         try:
#             sum += float(num.strip())
#         except:
#             not_num += 1

# print(sum)
# print(not_num)

"""Блок 7.3 Обработка исключений
№ 20 Январь, февраль..."""

# import calendar

# with open('input.txt') as input_data:
#     data = input_data.read().strip()

# try:
#     k = 5 / int(data)
#     print(calendar.month_name[int(data)])
# except (IndexError, ZeroDivisionError):
#     print('Введено число из недопустимого диапазона')
# except (TypeError, ValueError):
#     print('Введенно некорректное значение')

"""№ 21 Функция add_to_list_in_dict()"""

# def add_to_list_in_dict(data, key, element):
#     try:
#         data[key].append(element)
#     except KeyError:
#         data[key] = [element]

# data = {'a': [1, 2, 3]}

# add_to_list_in_dict(data, 'a', 1)
# add_to_list_in_dict(data, 'a', 3)
# add_to_list_in_dict(data, 'b', False)

# print(data)

"""№ 22 readme.txt"""

# with open('input.txt') as input_data:
#     data = input_data.read().strip()

# try:
#     with open(data, encoding='UTF-8') as file:
#         print(*file.readlines())
# except FileNotFoundError:
#     print('Файл не найден')

"""Блок 7.4 Обработка исключений"""
"""№ 18 Функция get_weekday()"""

# import locale, calendar

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# def get_weekday(number):
#     try:
#         if type(number) == int and number not in range(1, 8):
#             raise ValueError
#         return calendar.day_name[number - 1]

#     except (TypeError, AttributeError):
#         raise TypeError('Аргумент не является целым числом')
#         pass
#     except (IndexError, ValueError):
#         raise ValueError(('Аргумент не принадлежит требуемому диапазону'))
#         pass

# try:
#     print(get_weekday(-5))
# except ValueError as err:
#     print(err)
#     print(type(err))

"""№ 19 Функция get_id()"""

# def get_id(names, name):
#     try:
#         if type(name) != str:
#             raise TypeError
#         if name[0].islower() or not name[1:].islower() or not name.isalpha():
#             raise ValueError
#         names.append(name)
#         return len(names)
#     except TypeError:
#         raise TypeError('Имя не является строкой')
#     except ValueError:
#         raise ValueError('Имя не является корректным')

# names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
# name = ['Roman']

# try:
#     print(get_id(names, name))
# except TypeError as e:
#     print(e)

"""№20 Десериализация"""

# import json

# # filename = 'numbers.json'
# # filename = 'countries.json'
# filename = 'stores.json'

# try:
#     with open(filename, encoding='UTF-8') as json_input:
#         json_data = json.load(json_input)
#         print(json_data)
# except FileNotFoundError:
#     print('Файл не найден')
# except json.decoder.JSONDecodeError:
#     print('Ошибка десериализации')

"""№ 8 Функция is_good_password()"""

# class LetterError(Exception):
#     pass


# class LengthError(Exception):
#     pass


# class DigitError(Exception):
#     pass


# def is_good_password(string):
#     try:
#         if len(string) < 9:
#             raise LengthError
#         letters = (any(ch.isalpha() for ch in string) and
#                    not string.islower() and
#                    not string.isupper())
#         if not letters:
#             raise LetterError
#         digits = any(ch.isdigit() for ch in string)
#         if not digits:
#             raise DigitError
#     except:
#         raise


# try:
#     print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf'))
# except Exception as err:
#     print(type(err))


