
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
# print(repr(book))


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

'''№ 5.3.3 Класс Month'''

from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month

    @property
    def dat(self):
        return (self.year, self.month)

    def __repr__(self):
        return f'Month({self.year}, {self.month})'

    def __str__(self) -> str:
        return f'{self.year}-{self.month}'

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Month):
            a = self.dat()
            b = value.dat()
            return
        if isinstance(value, tuple) and len(value) == 2:
            return self.dat() == value
        return NotImplemented

    def __lt__(self, value: object) -> bool:
        if isinstance(value, Month):
            if self.year < value.year:
                return True
            if self.year == value.year:
                return self.month < value.month
        if isinstance(value, tuple):
            new = Month(value)
            return self < new
        return NotImplemented

print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))