
'''№ 5.1.1 Класс Config'''

# class Config:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self) -> None:
#         self.program_name = 'GenerationPy'
#         self.environment = 'release'
#         self.loglevel = 'verbose'
#         self.version = '1.0.0'


# config = Config()
# print(config.program_name)
# print(config.environment)
# print(config.loglevel)
# print(config.version)

# config1 = Config()
# config2 = Config()
# config3 = Config()
# print(config1 is config2)
# print(config1 is config3)

'''№ 5.2.1 Класс Book'''

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def __str__(self):
#         return f'{self.title} ({self.author}, {self.year})'

#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', '{self.year}')"


# book = Book('Изучаем Python', 'Марк Лутц', 2021)
# print(book)
# print(repr(book)

'''№ 5.2.2 Класс Rectangle'''

# class Rectangle:
#     def __init__(self, length, width):
#         self.length, self.width = length, width

#     def __repr__(self):
#         return f'Rectangle({self.length}, {self.width})'

# rectangle1 = Rectangle(1, 2)
# rectangle2 = Rectangle(3, 4)
# print(rectangle1)
# print(repr(rectangle2))

'''№ 5.2.3 Класс Vector'''

# class Vector(object):
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'

#     def __str__(self):
#         return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

# vector = Vector(1, 2)
# print(str(vector))
# print(repr(vector))

'''№ 5.2.4 Класс IPAddress'''

# from functools import singledispatchmethod


# class IPAddress:
#     @singledispatchmethod
#     def __init__(self, address) -> None:
#        self.address = address

#     @__init__.register(list)
#     @__init__.register(tuple)
#     def _from_list(self, address):
#         self.address = '.'.join(map(str, address))

#     def __str__(self) -> str:
#         return f'{self.address}'

#     def __repr__(self) -> str:
#         return f"IPAddress('{self.address}')"


# ip = IPAddress((1, 1, 11, 11))
# print(str(ip))
# print(repr(ip))

'''№ 5.2.5 Класс PhoneNumber'''

# class PhoneNumber(object):
#     def __init__(self, phone_number):
#         self.phone_number = ''.join(phone_number.split())

#     def __repr__(self):
#         return f'PhoneNumber(\'{self.phone_number}\')'

#     def __str__(self):
#         present = (
#             '(' + self.phone_number[:3] + ') ' +
#             self.phone_number[3:6] + '-' + self.phone_number[6:]
#         )
#         return present


# phone1 = PhoneNumber('9173963385')
# phone2 = PhoneNumber('918 396 3389')
# phone3 = PhoneNumber('919 333 3344')
# print(phone1, phone2, phone3, sep=', ')
# print([phone1, phone2, phone3])

'''№ 5.2.6 Класс AnyClass'''


# class AnyClass:
#     def __init__(self, **kwargs) -> None:
#         self.__dict__.update(kwargs)

#     def __str__(self) -> str:
#         return 'AnyClass: ' + self._attrs()

#     def __repr__(self) -> str:
#         return 'AnyClass(' + self._attrs() + ')'

#     def _attrs(self):
#         return ', '.join(
#             f'{key}={repr(value)}' for key, value in self.__dict__.items()
#         )

# obj = AnyClass(attr1=10, attr2='beegeek', attr3=True,
# attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)
# print(str(obj))
# print(repr(obj))

'''№ 5.3.1 Класс Vector'''

# class Vector:
#     def __init__(self, x, y) -> None:
#        self.x = x
#        self.y = y

#     def __eq__(self, value: object) -> bool:
#         if isinstance(value, Vector):
#             return self.x == value.x and self.y == value.y
#         return (self.x, self.y) == (value[0], value[1]) and len(value) == 2

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"

# a = Vector(1, 2)
# pair1 = (1, 2)
# pair2 = (3, 4)
# pair3 = (5, 6, 7)
# pair4 = (1, 2, 3, 4)
# pair5 = (1, 4, 3, 2)
# print(a == pair1)
# print(a == pair2)
# print(a == pair3)
# print(a == pair4)
# print(a == pair5)

'''№ 5.3.2 Класс Word'''

# from functools import total_ordering

# class Word(object):
#     def __init__(self, word):
#         self.word = word

#     def __repr__(self):
#         return f'Word(\'{self.word}\')'

#     def __str__(self):
#         return f'{self.word.capitalize()}'

#     @total_ordering
#     def __eq__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) == len(other.word)
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) < len(other.word)
#         return NotImplemented

#     def __le__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) <= len(other.word)
#         return NotImplemented

# words = [Word('python'), Word('bee'), Word('geek')]
# print(sorted(words))
# print(min(words))
# print(max(words))

'''№ 5.3.3 Класс Month '''

# from functools import total_ordering

# @total_ordering
# class Month:
#     def __init__(self, year, month) -> None:
#         self.year = year
#         self.month = month

#     @property
#     def dat(self):
#         return (self.year, self.month)

#     def __repr__(self):
#         return f'Month({self.year}, {self.month})'

#     def __str__(self) -> str:
#         return f'{self.year}-{self.month}'

#     def __eq__(self, value: object) -> bool:
#         if isinstance(value, Month):
#             a = self.dat
#             b = value.dat
#             return a == b
#         if isinstance(value, tuple) and len(value) == 2:
#             return self.dat() == value
#         return NotImplemented

#     def __lt__(self, value: object) -> bool:
#         if isinstance(value, Month):
#             if self.year < value.year:
#                 return True
#             if self.year == value.year:
#                 return self.month < value.month
#         if isinstance(value, tuple):
#             new = Month(value)
#             return self < new
#         return NotImplemented

# months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
# print(min(months))
# print(max(months))

'''№ 5.3.4 Класс Version'''

# from functools import total_ordering

# @total_ordering
# class Version(object):
#     def __init__(self, version):
#         self.version = version + '.0' * (2 - version.count('.'))

#     def __repr__(self):
#         return f'Version(\'{self.version}\')'

#     def __str__(self):
#         return self.version

#     def __eq__(self, other):
#         if isinstance(other, Version):
#             return self.version == other.version
#         return NotImplemented

#     def _neq_tuple(self, other):
#         for self_val, other_val in zip(
#             self.version.replace('.', ''), other.version.replace('.', '')
#         ):
#             if int(self_val) != int(other_val):
#                 # print(self_val, other_val)
#                 return int(self_val), int(other_val)

#     def __lt__(self, other):
#         if isinstance(other, Version):
#             return self._neq_tuple(other)[0] < self._neq_tuple(other)[1]
#         return NotImplementation

#     def __le__(self, other):
#         if isinstance(other, Version):
#             return self._neq_tuple(other)[0] <= self._neq_tuple(other)[1]
#         return NotImplementation

# versions = [Version('2'), Version('2.1'), Version('1.9.1')]
# print(sorted(versions))
# print(min(versions))
# print(max(versions))

'''№ 5.4.1 - Класс RevisibleString'''

# class ReversibleString:
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return self.string

#     def __neg__(self):
#         self.string = self.string[::-1]
#         return self

'''№ 5.4.2 Класс Money'''

# class Money:
#     def __init__(self, amount):
#         self.amount = amount

#     def __str__(self):
#         return f'{self.amount} руб.'

#     def __pos__(self):
#         return type(self)(abs(self.amount))

#     def __neg__(self):
#         return type(self)(-abs(self.amount))


# amounts = [0, -5983, 2205, 3997, 5343, 3346, -733, -2240, -1195, 9823, 8147, -3380, -4802, -8677, 9380, 2013, 8943, 664,
#            -3161, -8467, -5869, -9562, 9830, -8391, -5780, 4600, 5289, -8634, 7982, 1815, -7881, -8572, -1271, 2881,
#            -5134, 909, 6641, -480, -581, 7427, 8759, -775, 1363, 9616, -7803, 1412, -9517, -5564, 2177, -1062, 2116,
#            5309, 745, 134, 7804, 6195, -1529, -8924, 7449, 9926, -287, -5667, -1853, 924, -6439, 8176, -4671, 1309,
#            -9027, -3902, 801, 1353, 9358, -3359, -8740, 8195, -6026, -6302, -1786, 7933, 1529, -1244, 1110, -5619,
#            -4222, 5708, -7069, 4546, 3487, 6162, -5274, -4616, 676, 6636, -5461, -6940, -6921, -6026, -8602, -2027,
#            -8636]
# for amount in amounts:
#     money = Money(amount)
#     print('{}; {}'.format(+money, -money))

# # 0 руб.; 0 руб.
# # 5983 руб.; -5983 руб.
# # 2205 руб.; -2205 руб.
# # 3997 руб.; -3997 руб.
# # 5343 руб.; -5343 руб.
# # 3346 руб.; -3346 руб.
# # 733 руб.; -733 руб.
# # 2240 руб.; -2240 руб.
# # 1195 руб.; -1195 руб.
# # 9823 руб.; -9823 руб.
# # 8147 руб.; -8147 руб.
# # 3380 руб.; -3380 руб.
# # 4802 руб.; -4802 руб.
# # 8677 руб.; -8677 руб.
# # 9380 руб.; -9380 руб.
# # 2013 руб.; -2013 руб.
# # 8943 руб.; -8943 руб.
# # 664 руб.; -664 руб.
# # 3161 руб.; -3161 руб.
# # 8467 руб.; -8467 руб.
# # 5869 руб.; -5869 руб.
# # 9562 руб.; -9562 руб.
# # 9830 руб.; -9830 руб.
# # 8391 руб.; -8391 руб.
# # 5780 руб.; -5780 руб.
# # 4600 руб.; -4600 руб.
# # 5289 руб.; -5289 руб.
# # 8634 руб.; -8634 руб.
# # 7982 руб.; -7982 руб.
# # 1815 руб.; -1815 руб.
# # 7881 руб.; -7881 руб.
# # 8572 руб.; -8572 руб.
# # 1271 руб.; -1271 руб.
# # 2881 руб.; -2881 руб.
# # 5134 руб.; -5134 руб.
# # 909 руб.; -909 руб.
# # 6641 руб.; -6641 руб.
# # 480 руб.; -480 руб.
# # 581 руб.; -581 руб.
# # 7427 руб.; -7427 руб.
# # 8759 руб.; -8759 руб.
# # 775 руб.; -775 руб.
# # 1363 руб.; -1363 руб.
# # 9616 руб.; -9616 руб.
# # 7803 руб.; -7803 руб.
# # 1412 руб.; -1412 руб.
# # 9517 руб.; -9517 руб.
# # 5564 руб.; -5564 руб.
# # 2177 руб.; -2177 руб.
# # 1062 руб.; -1062 руб.
# # 2116 руб.; -2116 руб.
# # 5309 руб.; -5309 руб.
# # 745 руб.; -745 руб.
# # 134 руб.; -134 руб.
# # 7804 руб.; -7804 руб.
# # 6195 руб.; -6195 руб.
# # 1529 руб.; -1529 руб.
# # 8924 руб.; -8924 руб.
# # 7449 руб.; -7449 руб.
# # 9926 руб.; -9926 руб.
# # 287 руб.; -287 руб.
# # 5667 руб.; -5667 руб.
# # 1853 руб.; -1853 руб.
# # 924 руб.; -924 руб.
# # 6439 руб.; -6439 руб.
# # 8176 руб.; -8176 руб.
# # 4671 руб.; -4671 руб.
# # 1309 руб.; -1309 руб.
# # 9027 руб.; -9027 руб.
# # 3902 руб.; -3902 руб.
# # 801 руб.; -801 руб.
# # 1353 руб.; -1353 руб.
# # 9358 руб.; -9358 руб.
# # 3359 руб.; -3359 руб.
# # 8740 руб.; -8740 руб.
# # 8195 руб.; -8195 руб.
# # 6026 руб.; -6026 руб.
# # 6302 руб.; -6302 руб.
# # 1786 руб.; -1786 руб.
# # 7933 руб.; -7933 руб.
# # 1529 руб.; -1529 руб.
# # 1244 руб.; -1244 руб.
# # 1110 руб.; -1110 руб.
# # 5619 руб.; -5619 руб.
# # 4222 руб.; -4222 руб.
# # 5708 руб.; -5708 руб.
# # 7069 руб.; -7069 руб.
# # 4546 руб.; -4546 руб.
# # 3487 руб.; -3487 руб.
# # 6162 руб.; -6162 руб.
# # 5274 руб.; -5274 руб.
# # 4616 руб.; -4616 руб.
# # 676 руб.; -676 руб.
# # 6636 руб.; -6636 руб.
# # 5461 руб.; -5461 руб.
# # 6940 руб.; -6940 руб.
# # 6921 руб.; -6921 руб.
# # 6026 руб.; -6026 руб.
# # 8602 руб.; -8602 руб.
# # 2027 руб.; -2027 руб.
# # 8636 руб.; -8636 руб.

'''№ 5.4.3 Класс Vector'''

# from math import sqrt


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self) -> str:
#         return f'Vector({self.x}, {self.y})'

#     def __str__(self) -> str:
#         return f'({self.x}, {self.y})'

#     def __pos__(self):
#         return Vector(self.x, self.y)

#     def __neg__(self):
#         return Vector(-self.x, -self.y)

#     def __abs__(self):
#         return sqrt(self.x ** 2 + self.y ** 2)


# vector = Vector(3, -4)
# print(+vector)
# print(-vector)
# print(abs(vector))

'''№ 5.4.4 Класс ColoredPoint'''

# class ColoredPoint:
#     def __init__(self, x, y, color=(0, 0, 0)):
#         self.x = x
#         self.y = y
#         self.color = color

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     def __repr__(self):
#         return f'{type(self)}({self.x}, {self.y}, {self.color})'

#     def __pos__(self):
#         return type(self)(self.x, self.y, self.color)

#     def __neg__(self):
#         return type(self)(-self.x, -self.y, self.color)

#     def __invert__(self):
#         return type(self)(
#             self.y, self.x, (255 - self.color[i] for i in range(3))
#         )


# point = ColoredPoint(0, 0, (0, 0, 0))

# print(f'{+point}; {-point}; {~point}')
# print(point.color)

# # (0, 0); (0, 0); (0, 0)
# # (0, 0, 0)


'''№ 5.4.5  Класс Matrix 🌶️🌶️'''


# class Matrix:
#     def __init__(self, rows, cols, value=0):
#         self.rows = rows
#         self.cols = cols
#         self.value = value
#         self.matrix = []
#         for _ in range(rows):
#             row = []
#             for __ in range(cols):
#                 row.append(value)
#             self.matrix.append(row)
#         # self.matrix = [
#         #     [self.value for _ in range(self.cols)] for __ in range(self.rows)
#         # ]

#     def __repr__(self) -> str:
#         return f'Matrix({self.rows}, {self.cols})'

#     def __str__(self) -> str:
#         max_len = 0
#         for row in self.matrix:
#             mx = max(row)
#             if max_len < len(str(mx)):
#                 max_len = len(str(mx))
#         result = ''
#         for row in self.matrix:
#             for el in row:
#                 result += str(el).rjust(max_len+1)
#             result += '\n'
#         return result[:-1]

#     def get_value(self, row, col):
#         return self.matrix[row][col]

#     def set_value(self, row, col, value):
#         pass
#         self.matrix[row][col] = value

#     def new_matrix(self, positive=True, trans=False, rnd=False, ndig=0):
#         if trans:
#             new_matr = Matrix(self.cols, self.rows)
#             for i in range(new_matr.rows):
#                 for j in range(new_matr.cols):
#                     new_matr.set_value(i, j, self.get_value(j, i))
#                     pass
#         else:
#             new_matr = Matrix(self.rows, self.cols)

#             if positive:
#                 k = 1
#             else:
#                 k = -1

#             for i in range(len(self.matrix)):
#                 for j in range(len(self.matrix[0])):
#                     if rnd:
#                         new_matr.set_value(
#                             i, j, round(self.get_value(i, j), ndig)
#                         )
#                     else:
#                         new_matr.set_value(i, j, self.get_value(i, j) * k)

#         return new_matr

#     def __pos__(self):
#         return self.new_matrix()

#     def __neg__(self):
#         return self.new_matrix(positive=False)

#     def __invert__(self):
#         return self.new_matrix(trans=True)

#     def __round__(self, n=0):
#         return self.new_matrix(rnd=True, ndig=n)


# matrix = Matrix(2, 3, 1)

# plus_matrix = +matrix
# minus_matrix = -matrix
# invert_matrix = ~matrix

# print(plus_matrix.cols, plus_matrix.rows)
# print(minus_matrix.cols, minus_matrix.rows)
# print(invert_matrix.cols, invert_matrix.rows)

'''№ 5.5.1 Класс FoodInfo'''

# class FoodInfo:
#     def __init__(self, proteins, fats, carbohydrates):
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates

#     def __repr__(self):
#         return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'

#     def __add__(self, other):
#         if isinstance(other, int | float):
#             return FoodInfo(
#                 self.proteins + other,
#                 self.fats + other,
#                 self.carbohydrates + other
#             )
#         if isinstance(other, FoodInfo):
#             return FoodInfo(
#                 self.proteins + other.proteins,
#                 self.fats + other.fats,
#                 self.carbohydrates + other.carbohydrates
#             )
#         return NotImplemented

#     def __mul__(self, other):
#         if isinstance(other, int | float):
#             return FoodInfo(
#                 self.proteins * other,
#                 self.fats * other,
#                 self.carbohydrates * other
#             )
#         return NotImplemented

#     def __truediv__(self, other):
#         if isinstance(other, int | float):
#             return FoodInfo(
#                 self.proteins / other,
#                 self.fats / other,
#                 self.carbohydrates / other
#             )
#         return NotImplemented

#     def __floordiv__(self, other):
#         if isinstance(other, int | float):
#             return FoodInfo(
#                 self.proteins // other,
#                 self.fats // other,
#                 self.carbohydrates // other
#             )
#         return NotImplemented

# food1 = FoodInfo(10, 20, 30)
# food2 = FoodInfo(10, 10, 20)
# print(food1 + food2)
# print(food1 * 2)
# print(food1 / 2)
# print(food1 // 2)


# '''№ 5.5.3 Класс SuperString'''

# class SuperString:
#     def __init__(self, string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return f'{self.string}'

#     def __add__(self, other):
#         if isinstance(other, SuperString):
#             return self.string + other.string
#         return NotImplemented

#     def __mul__(self, other):
#         return SuperString(self.string * other)

#     def __rmul__(self, other):
#         return self * other

#     def __truediv__(self, other):
#         return SuperString(self.string[:len(self.string) // other])

#     def __lshift__(self, other):
#         if other < len(self.string):
#             return SuperString(self.string[:-other])
#         else:
#             return SuperString('')

#     def __rshift__(self, other):
#         if other < len(self.string):
#             return SuperString(self.string[other:])
#         return SuperString('')

# s = SuperString('beegeek')
# print(s << 4)
# print(s >> 3)

'''№ 5.6.1 Класс Calculator'''


# class Calculator:
#     def __init__(self) -> None:
#         pass

#     def __call__(self, a, b, operation):
#         operations = {
#             '+': lambda x,y: x+y,
#             '-': lambda x,y: x-y,
#             '*': lambda x,y: x*y,
#             '/': lambda x,y: x/y,
#         }
#         if b == 0:
#             raise ValueError('Деление на ноль невозможно')
#         if isinstance(a, float | int) and isinstance(b, float | int):
#             return operations[operation](a, b)

# calculator = Calculator()
# try:
#     print(calculator(10, 0, '/'))
# except ValueError as e:
#     print(e)

'''№ 5.7.2 класс Temperature'''

# class Temperature:
#     def __init__(self, temperature):
#         self.temperature_c = temperature
#         self.temperature_f = self.to_fahrenheit()

#     def to_fahrenheit(self):
#         return (self.temperature_c * 9 + 160) / 5

#     @classmethod
#     def from_fahrenheit(cls, temperature):
#         temperature = 5 * (temperature - 32) / 9
#         return cls(temperature)

#     def __str__(self):
#         return f'{round(self.temperature_c, 2)}°C'

#     def __bool__(self):
#         return self.temperature_c > 0

#     def __int__(self):
#         return int(self.temperature_c)

#     def __float__(self):
#         return self.temperature_c


# t = Temperature.from_fahrenheit(41)
# print(t)
# print(int(t))
# print(float(t))
# print(t.to_fahrenheit())

'''№ 5.8.5 Класс AttrsNumberObject'''

# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#         object.__setattr__(self, 'attrs_num', len(self.__dict__) + 1)

#     def __setattr__(self, attr, value):
#         self.__dict__['attrs_num'] += 1
#         object.__setattr__(self, attr, value)

#     def __delattr__(self, name):

#         self.__dict__['attrs_num'] -= 1
#         object.__delattr__(self, name)

# music_group = AttrsNumberObject(name='Alexandra Savior',


# genre='dream pop')
# print(music_group.attrs_num)
# del music_group.genre
# print(music_group.attrs_num)

'''№ 5.8.7 Класс Const'''

# class Const:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)

#     def __setattr__(self, attr, value):
#         if attr in self.__dict__:
#             raise AttributeError('Изменение значения аттрибута невозможно')
#         else:
#             object.__setattr__(self, attr, value)

#     def __delattr__(self, attr):
#         raise AttributeError('Удаление атрибута невозможно')


# videogame = Const(name='The Last of Us')
# try:
#     del videogame.name
# except AttributeError as e:
#     print(e)

'''№ 5.9.1 Функция limited_hash🌶️  '''
# from itertools import cycle

# def limited_hash(left, right, hash_function=hash):
#     def hashing(obj):
#         hash_val = hash_function(obj)
#         hash_iter = cycle(range(0, right - left + 1))
#         if hash_val > right:
#             for _ in range(hash_val - right - 1):
#                 next(hash_iter)
#             return left + next(hash_iter)
#         elif hash_val < left:
#             for _ in range(left - hash_val - 1):
#                 next(hash_iter)
#             return right - next(hash_iter)
#         else:
#             return hash_val
#     return hashing

# hash_function = limited_hash(10, 15)
# print(hash_function(9))
# print(hash_function(8))
# print(hash_function(4))
# print(hash_function(3))
# print(hash_function(2))

'''№ 5.10.1 Класс ColoredPoint'''

# class ColoredPoint:
#     def __init__(self, iks, ygryk, tsvet):
#         self.iks = iks
#         self.ygryk = ygryk
#         self.tsvet = tsvet

#     @property
#     def x(self):
#         return self.iks

#     @property
#     def y(self):
#         return self.ygryk


#     @property
#     def color(self):
#         return self.tsvet

#     def __repr__(self):
#         return f'ColoredPoint({self.iks}, {self.ygryk}, {self.tsvet})'

#     def __eq__(self, other):
#         if isinstance(other, ColoredPoint):
#             return (
#                 self.iks == other.iks and
#                 self.ygryk == other.ygryk and
#                 self.tsvet == other.tsvet
#             )
#         return NotImplemented

#     def __hash__(self):
#         return hash(self._fields)

#     @property
#     def _fields(self):
#         return self.iks, self.ygryk, self.tsvet



# point1 = ColoredPoint(1, 1, 1)
# point2 = ColoredPoint(1, 1, 1)

# print(point1 == point2)
# print(hash(point1))
# print(hash(point2))
