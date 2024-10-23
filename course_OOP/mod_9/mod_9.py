"""Модуль 9. Задачи на проектирование классов """

"""№ 9.1 Функция anything()"""

# class AlwaysEqual:
#     def __eq__(self, other):
#         return True
#     def __ne__(self, other):
#         return True
#     def __lt__(self, other):
#         return True
#     def __gt__(self, other):
#         return True
#     def __le__(self, other):
#         return True
#     def __ge__(self, other):
#         return True

# def anything():
#     return AlwaysEqual()

# import math, re
# print(anything() != [])
# print(anything() < 'World')
# print(anything() > 81)
# print(anything() >= re)
# print(anything() <= math)
# print(anything() == ord)

"""№ 9.2 Класс Vector"""

# from math import sqrt

# class Vector:
#     def __init__(self, x, y, z, l=0):
#         self.x, self.y, self.z, self.l = x, y, z, l

#     def __str__(self):
#         return f'({self.x}, {self.y}, {self.z}, {self.l})'

#     def __add__(self, other):
#         if self.l != other.l:
#             raise ValueError('Векторы должны иметь равную длину')
#         if isinstance(other, Vector):
#             return Vector(
#                 self.x + other.x,
#                 self.y + other.y,
#                 self.z + other.z,
#                 self.l + other.l
#             )
#         return NotImplemented

#     def __sub__(self, other):
#         if self.l != other.l:
#             raise ValueError('Векторы должны иметь равную длину')
#         if isinstance(other, Vector):
#             return Vector(
#                 self.x - other.x,
#                 self.y - other.y,
#                 self.z - other.z,
#                 self.l - other.l
#             )
#         return NotImplemented

#     def __mul__(self, other):
#         if self.l != other.l:
#             raise ValueError('Векторы должны иметь равную длину')
#         if isinstance(other, Vector):
#             return Vector(
#                 self.x * other.x,
#                 self.y * other.y,
#                 self.z * other.z,
#                 self.l * other.l
#             )
#         return NotImplemented

#     def norm(self):
#         return sqrt(
#             self.x ** 2 +
#             self.y ** 2 +
#             self.z ** 2 +
#             self.l ** 2
#         )

# vector1 = Vector(1, 2, 3)
# vector2 = Vector(3, 4, 5)
# vector3 = Vector(5, 6, 7, 8)

# print(vector1 + vector2)
# print(vector1 - vector2)
# print(vector1 * vector2)
# print(vector3.norm())

"""№ 9.3 Класс CaesarCipher"""

# class CaesarCipher:
#     def __init__(self, shift):
#         self.shift = shift

#     def encode(self, word):
#         result = []
#         for let in word:
#             if 65 <= ord(let) <= 90:
#                 code = ord(let) + self.shift
#                 if code > 90:
#                     new_let = chr(64 + (code - 90))
#                 else:
#                     new_let = chr(code)

#             elif 97 <= ord(let) <= 122:
#                 code = ord(let) + self.shift
#                 if code > 122:
#                     new_let = chr(96 + (code - 122))
#                 else:
#                     new_let = chr(code)

#             else:
#                 new_let = let

#             result.append(new_let)
#         return ''.join(result)

#     def decode(self, word):
#         result = []
#         for let in word:
#             if 65 <= ord(let) <= 90:
#                 code = ord(let) - self.shift
#                 if code < 65:
#                     new_let = chr(91 - (65 - code))
#                 else:
#                     new_let = chr(code)

#             elif 97 <= ord(let) <= 122:
#                 code = ord(let) - self.shift
#                 if code < 97:
#                     new_let = chr(123 - (98 - code))
#                 else:
#                     new_let = chr(code)

#             else:
#                 new_let = let

#             result.append(new_let)
#         return ''.join(result)

# cipher = CaesarCipher(5)
# print(cipher.encode('Beegeek'))
# print(cipher.decode('Gjjljjp'))

# print(cipher.encode('Биgeek123'))
# print(cipher.decode('Биljjp123'))

"""№ 9.4 Классы ArithmeticProgression и GeometricProgression"""

# class ArithmeticProgression:
#     def __init__(self, fst, step):
#         self.fst, self.step = fst, step
#         self.val = self.fst - self.step

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.val += self.step
#         return self.val

# class GeometricProgression:
#     def __init__(self, fst, step):
#         self.fst, self.step = fst, step
#         self.val = self.fst / self.step

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.val *= self.step
#         return int(self.val)

# progression = GeometricProgression(100, 10)
# count = 0

# for item in progression:
#     if count == 20:
#         break
#     count += 1
#     print(item, end=' ')

"""№9.5 Классы Domain и DomainException"""

class Domain:
    def __init__(self, data):
        self._data = data

    def from_url(self, url):
        pass

    def from_email(self, email):
        pass

    def __str__(self):
        return f''


class DomainException:
    pass
