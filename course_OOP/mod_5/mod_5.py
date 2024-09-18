
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

# '''№ 5.1.1 Класс Book'''

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


'''№ 5.1.4 Класс IPAddress'''

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

'''№ 5.3.3 Класс Month  ???????????????? ошибка с tuple'''

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
#             a = self.dat()
#             b = value.dat()
#             return
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

# print(Month(1999, 12) == Month(1999, 12))
# print(Month(1999, 12) < Month(2000, 1))
# print(Month(1999, 12) > Month(2000, 1))
# print(Month(1999, 12) <= Month(1999, 12))
# print(Month(1999, 12) >= Month(2000, 1))

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

'''№ 5.9.1 Функция limited_hash''' 🌶️

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
