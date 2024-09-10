'''4.6.1 Класс Person'''

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     @property
#     def fullname(self):
#         return ' '.join([self.name, self.surname])

#     @fullname.setter
#     def fullname(self, new_name=None, new_surname=None):
#         if new_name:
#             self.name = new_name
#         if new_surname:
#             self.surname = new_surname

# person = Person('Mike', 'Pondsmith')
# print(person.name)
# print(person.surname)
# print(person.fullname)

'''4.6.3 Класс QuadraticPolynomial'''

# from math import sqrt

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     @property
#     def x1(self):
#         a, b, c = self.a, self.b, self.c
#         d = b ** 2 - 4 * a * c
#         if d:
#             return (-b - sqrt(d)) / 2 * a
#     @property
#     def x2(self):
#         a, b, c = self.a, self.b, self.c
#         d = b ** 2 - 4 * a * c
#         if d:
#             return (-b + sqrt(d)) / 2 * a

#     @property
#     def view(self):
#         a, b, c = self.a, self.b, self.c
#         return f'{a}x^2 + {b}x + {c}'

#     @property
#     def coefficients(self):
#         return (self.a, self.b, self.c)

#     @coefficients.setter
#     def coefficients(self, a=None, b=None, c=None):
#         if a:
#             self.a = a
#         if b:
#             self.b = b
#         if c:
#             self.c = c

# polynom = QuadraticPolynomial(1, 2, -3)
# print(polynom.view)
# print(polynom.coefficients)

'''4.7.4 Класс Pet'''

# class Pet:
#     pets = []
#     def __init__(self, name):
#         self.name = name
#         Pet.pets.append(self)

#     @classmethod
#     def first_pet(cls):
#         return cls.pets[0] if cls.pets[0] else None
#     @classmethod
#     def last_pet(cls):
#         return cls.pets[-1] if cls.pets[-1] else None

#     @classmethod
#     def num_of_pets(cls):
#         return len(cls.pets)

# pet1 = Pet('Ratchet')
# pet2 = Pet('Clank')
# pet3 = Pet('Rivet')
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())

# '''4.8.1 Класс Processor'''

# from functools import singledispatchmethod

# class Processor:
#     def __init__(self):
#         pass

#     @singledispatchmethod
#     def process(obj):
#         raise TypeError('Аргумент переданного типа не поддреживается')

#     # @staticmethod
#     @process.register
#     def p_fl(obj: int):
#         return obj * 2

#     # @staticmethod
#     @process.register
#     def p_fl(obj: float):
#         return obj * 2

#     # @staticmethod
#     @process.register
#     def p_str(obj: str):
#         return obj.upper()

#     @process.register
#     def p_tup(obj: tuple):
#         obj = list(obj)
#         obj.reverse()
#         obj = tuple(obj)
#         return obj

#     @process.register
#     def p_lis(obj: list):
#         obj.reverse()
#         return obj

# try:
#     Processor.process({1, 2, 3})
# except TypeError as e:
#     print(e)

'''№ 4.8.3 Класс Formatter'''

# from functools import singledispatchmethod

# class Formatter:
#     def __init__(self):
#         pass

#     @singledispatchmethod
#     @staticmethod
#     def format(obj):
#         raise TypeError('Аргумент переданного типа не поддреживается')

#     @format.register
#     def f_int(obj: int):
#         return f'Целое число: {obj}'

#     # @staticmethod
#     @format.register
#     def f_fl(obj: float):
#         return f'Вещественное число: {obj}'

#     # @staticmethod
#     @format.register
#     def f_dic(obj: dict):
#         return f'Пары словаря: {obj}'

#     @format.register
#     def f_tup(obj: tuple):
#         return f'Элементы кортежа: {obj}'
#     @format.register
#     def f_lis(obj: list):
#         return f'Элементы списка: {obj}'

# print(Formatter.format(1337))
# print(Formatter.format(20.77))
# print()
# print(Formatter.format([10, 20, 30, 40, 50]))
# print(Formatter.format(([1, 3], [2, 4, 6])))
# print()
# print(Formatter.format({'Cuphead': 1, 'Mugman': 3}))
# print(Formatter.format({1: 'one', 2: 'two'}))
# print(Formatter.format({1: True, 0: False}))
# print()
# try:
#     Formatter.format('All them years, Dutch, for this snake?')
# except TypeError as e:
#     print(e)

'''№ 4.8.4 Класс BirthInfo🌶️'''

# from functools import singledispatchmethod
# from datetime import date


# class BirthInfo:
#     @singledispatchmethod
#     def __init__(self, birth_date):
#         raise TypeError('Аргумент переданного типа не поддерживается')

#     @__init__.register(date)
#     def init_datetime(self, birth_date):
#         self.birth_date = birth_date

#     @__init__.register(str)
#     def init_str(self, birth_date):
#         self.birth_date = date.fromisoformat(birth_date)

#     @__init__.register(list)
#     @__init__.register(tuple)
#     def init_list_tuple(self, birth_date):
#         self.birth_date = date(*birth_date)

#     @property
#     def age(self):
#         return self.current_age(self.birth_date, date.today())

#     @staticmethod
#     def current_age(birth_date, today):
#         age = (today.year - birth_date.year) - 1
#         age += (today.month, today.day) >= (birth_date.month, birth_date.day)
#         return age

# from datetime import MAXYEAR

# birthday = date(2020, 9, 18)
# today = date.today()
# birthinfo = BirthInfo(birthday)
# true_age = BirthInfo.current_age(birthday, today)
# print(birthinfo.age == true_age)
