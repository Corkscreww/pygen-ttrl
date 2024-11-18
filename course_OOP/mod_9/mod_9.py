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

# from re import fullmatch, search

# class Domain:
#     dom_pattern = r'[A-Za-z]+\.[A-Za-z]+'

#     def __init__(self, domain):
#         self.domain = self.find_pattern(self.dom_pattern, domain)

#     @classmethod
#     def from_url(cls, url):
#         dom_url = r'(http)|(https)\:\/\/'
#         return cls(Domain.find_pattern(dom_url + Domain.dom_pattern, url))

#     @classmethod
#     def from_email(cls, email):
#         # dom_email = r'[a-zA-Z]+\@' + Domain.dom_pattern
#         patt =  r'[a-zA-Z]+\@[A-Za-z]+\.[A-Za-z]+'

#         return cls(Domain.find_pattern(patt, email))

#     @staticmethod
#     def find_pattern(pattern, data):
#         domain = fullmatch(pattern, data)
#         if domain:
#             domain = search(Domain.dom_pattern, data)
#         else:
#             raise DomainException('Недопумтимый домен, url или email')
#         return domain

#     def __str__(self):
#         return f'{self.domain[0]}'


# class DomainException(Exception):
#     pass

# # domain1 = Domain('pygen.ru')
# domain2 = Domain.from_url('https://pygen.ru')
# # domain3 = Domain.from_email('support@pygen.ru')

# # print(domain1)
# print(domain2)
# # print(domain3)

'''№ 9.6 Класс HighScoreTable'''

# class HighScoreTable:
#     def __init__(self, scores_count):
#         self.scores_count = scores_count
#         self.scores = []

#     def update(self, score):
#         if len(self.scores) == self.scores_count:
#             if score > min(self.scores):
#                 self.scores.append(score)
#                 self.scores.sort(reverse=True)
#                 del self.scores[-1]
#         else:
#             self.scores.append(score)
#             self.scores.sort(reverse=True)

#     def reset(self):
#         self.scores = []


# high_score_table = HighScoreTable(20)

# print(high_score_table.scores)

# scores = [74, 95, 57, 69, 26, 75, 34, 32, 78, 15, 42, 41, 62, 17, 31, 87, 90, 69, 47, 28, 26, 64, 71, 65, 41, 39, 59,
#           29, 83, 12, 11, 72, 51, 34, 50, 36, 29, 36, 70, 84, 52, 98, 46, 24, 85, 35, 98, 10, 64, 84, 99, 53, 47, 99,
#           41, 19, 67, 33, 36, 74, 20, 86, 91, 18, 55, 47, 71, 71, 82, 38, 32, 78, 51, 53, 46, 99, 44, 90, 59, 94, 75,
#           71, 39, 97, 67, 52, 90, 19, 26, 48, 22, 18, 21, 41, 97, 35, 78, 63, 50, 91, 19, 23, 77, 47, 26, 17, 16, 45,
#           93, 13, 22, 30, 78, 87, 42, 73, 26, 65, 55, 64, 54, 26, 67, 93, 88, 46, 14, 99, 41, 98, 71, 62, 75, 87, 93,
#           43, 47, 69, 65, 40, 33, 40, 32, 98, 31, 97, 21, 10, 75, 16, 97, 17, 31, 98, 60, 96, 90, 47, 91, 35, 15, 20,
#           59, 25, 87, 39, 51, 23, 81, 62, 94, 10, 74, 32, 14, 18, 11, 50, 25, 100, 26, 58, 62, 81, 80, 34, 77, 23, 60,
#           89, 74, 34, 12, 100, 77, 82, 34, 13, 43, 40, 66, 49, 29, 84, 62, 37, 51, 84, 93, 55, 67, 78, 17, 50, 70, 45,
#           69, 86, 97, 28, 14, 85, 40, 53, 45, 66, 93, 15, 10, 12, 61, 93, 76, 16, 93, 70, 89, 85, 44, 60, 74, 27, 41,
#           25, 18, 34, 98, 16, 88, 51, 91, 34, 14, 41, 53, 21, 62, 27, 54, 35, 37, 32, 96, 21, 78, 71, 58, 13, 75, 75,
#           44, 72, 99, 92, 20, 77, 83, 56, 59, 85, 73, 94, 63, 88, 56, 100, 52, 61, 34, 53, 33, 32, 45, 69, 88, 84, 82,
#           63, 35, 94, 20, 51, 94, 51, 69, 11, 22, 40, 79, 45, 82, 64, 84, 24, 50, 84, 46, 72, 36, 66, 58, 74, 13, 98,
#           46, 26, 79, 36, 64, 59, 98, 27, 73, 37, 48, 31, 67, 74, 17, 75, 17, 19, 35, 12, 93, 87, 21, 57, 36, 37, 39,
#           37, 69, 83, 81, 33, 42, 48, 44, 87, 48, 38, 50, 45, 94, 84, 83, 45, 12, 20, 29, 50, 27, 96, 45, 91, 18, 51,
#           13, 45, 25, 30, 85, 93, 71, 90, 84, 74, 88, 81, 96, 67, 25, 40, 68, 73, 80, 76, 15, 36, 49, 15, 68, 40, 86,
#           68, 73, 48, 38, 86, 23, 98, 79, 62, 84, 16, 14, 11, 74, 21, 77, 14, 73, 99, 21, 48, 83, 51, 53, 66, 55, 27,
#           14, 38, 47, 45, 88, 52, 43, 73, 56, 74, 45, 98, 65, 61, 37, 69, 87, 92, 57, 61, 13, 68, 94, 15, 88, 30, 26,
#           51, 99, 53, 19, 13, 20, 34, 67, 48, 94, 38, 95, 35, 78, 60, 13, 100, 26, 36, 20, 97, 64, 68, 62, 55, 51, 39,
#           55, 33, 70, 87, 17, 33, 32, 82, 50, 53, 43, 35, 38, 47, 10, 71, 12, 78, 87, 85, 13, 25, 66, 40, 22, 67, 63,
#           57, 72, 70, 89, 23, 92, 49, 29, 48, 91, 70, 39, 83, 20, 18, 78, 36, 53, 57, 78, 87, 68, 10, 12, 78, 22, 90,
#           82, 14, 67, 63, 21, 13, 66, 48, 77, 18, 39, 30, 84, 40, 78, 98, 15, 100, 49, 37, 75, 39, 69, 72, 75, 47, 79,
#           90, 95, 33, 89, 52, 33, 100, 66, 44, 46, 69, 54, 76, 81, 40, 30, 60, 92, 13, 92, 92, 54, 80, 53, 36, 99, 12,
#           30, 68, 64, 15, 85, 76, 81, 35, 27, 65, 64, 24, 69, 99, 99, 16, 29, 32, 73, 83, 26, 78, 13, 87, 39, 81, 13,
#           71, 60, 53, 34, 54, 59, 54, 58, 97, 12, 93, 92, 73, 37, 46, 67, 61, 48, 86, 27, 31, 44, 16, 16, 33, 52, 62,
#           43, 81, 69, 23, 13, 67, 17, 38, 69, 21, 28, 66, 55, 52, 99, 12, 17, 48, 75, 71, 36, 79, 71, 21, 70, 84, 34,
#           32, 99, 73, 87, 99, 34, 84, 93, 83, 16, 73, 53, 59, 67, 69, 46, 20, 13, 42, 58, 22, 17, 48, 95, 82, 11, 39,
#           41, 48, 65, 42, 54, 65, 42, 56, 93, 97, 33, 40, 72, 79, 43, 61, 48, 21, 37, 35, 50, 40, 32, 21, 56, 22, 46,
#           92, 12, 92, 15, 54, 90, 74, 88, 80, 30, 55, 56, 64, 33, 13, 37, 74, 96, 18, 14, 79, 69, 17, 46, 36, 68, 56,
#           90, 57, 50, 86, 81, 55, 60, 81, 28, 53, 97, 85, 85, 72, 59, 64, 20, 35, 86, 62, 55, 68, 18, 11, 17, 81, 43,
#           86, 78, 39, 48, 71, 45, 87, 30, 96, 91, 23, 13, 41, 79, 68, 41, 80, 35, 15, 99, 75, 86, 82, 68, 57, 56, 61,
#           32, 57, 24, 80, 88, 35, 99, 60, 49, 41, 10, 75, 46, 67, 80, 56, 53, 79, 30, 50, 21, 54, 44, 78, 47, 34, 77,
#           19, 47, 82, 32, 67, 82, 77, 34, 65, 65, 50, 83, 37, 12, 46, 73, 70, 22, 94, 33, 83, 31, 72, 52, 65, 13, 21,
#           29, 59, 52, 53, 89, 69, 38, 58, 29, 91, 56, 41, 53, 51, 76, 38, 93, 90, 22, 70, 68, 69, 38, 20, 22, 83, 31,
#           75, 68, 88, 80, 97, 88, 49, 14, 47, 99, 34, 67, 82, 99, 98, 19, 72, 26, 72, 82, 72, 32, 45, 46, 61, 99, 21,
#           51, 45, 14, 34, 99, 63, 57, 97, 78, 25, 17, 18, 33, 77, 31, 46, 85, 29, 94, 97, 100, 48, 64, 70, 44, 40, 100,
#           31, 25, 48, 11, 65, 85, 70, 77, 36, 99, 83, 70, 64, 99, 45, 92, 71, 29, 89, 36, 32, 26, 85, 54, 13, 75, 67,
#           64, 55, 44, 47, 78, 93, 49, 84, 35, 66, 11, 44, 40, 13, 75, 96, 31, 92, 10, 29, 62, 50, 46, 79, 100, 50, 91,
#           90]

# for score in scores:
#     high_score_table.update(score)

# print(high_score_table.scores)

'''№ 9.7 Класс Pagination'''

# class Pagination:
#     def __init__(self, data, limit):
#         self._data = data
#         self.limit = limit
#         self.current_page = 1
#         self.total_pages = (
#             lambda: len(self._data) // self.limit
#             if len(self._data) % self.limit == 0
#             else len(self._data) // self.limit + 1
#         )()

#     @staticmethod
#     def _limit_control(page, total_pages):
#         if page > total_pages:
#             return total_pages
#         elif page < 1:
#             return 1
#         else:
#             return page

#     def prev_page(self):
#         self.current_page = self._limit_control(
#             self.current_page - 1,
#             self.total_pages
#         )
#         return self

#     def next_page(self):
#         self.current_page = self._limit_control(
#             self.current_page + 1,
#             self.total_pages
#         )
#         return self

#     def first_page(self):
#         self.current_page = 1

#     def last_page(self):
#         self.current_page = self.total_pages

#     def go_to_page(self, page):
#         self.current_page = self._limit_control(page, self.total_pages)


#     def get_visible_items(self):
#         # # items_per_page = len(self._data) // self.limit
#         # # print(f'total pages = {self.total_pages}')
#         # # print(f'CP = {self.current_page}')
#         start_index = self.limit * (self.current_page - 1)
#         end_index = start_index + self.limit
#         # # print(f'start index = {start_index} end index = {end_index}')
#         if end_index > len(self._data):
#             end_index = len(self._data)
#         result = [self._data[i] for i in range(start_index, end_index)]
#         return result


# alphabet = list('abcdefghijklmnopqrstuvwxyz')
# pagination = Pagination(alphabet, 4)
# pages = [7, 3, 6, 1, 4, 2, 5]

# for page in pages:
#     pagination.go_to_page(page)
#     print(pagination.get_visible_items())

# # ['y', 'z']
# # ['i', 'j', 'k', 'l']
# # ['u', 'v', 'w', 'x']
# # ['a', 'b', 'c', 'd']
# # ['m', 'n', 'o', 'p']
# # ['e', 'f', 'g', 'h']
# # ['q', 'r', 's', 't']

'''№ 9.8 Класс Testpaper и Student'''

# class Testpaper:
#     def __init__(self, subject, correct_answers, pass_score):
#         self.subject = subject
#         self.correct_answers = correct_answers
#         self.pass_score = int(pass_score[:-1])

# class Student:
#     def __init__(self):
#         self.tests_taken = 'No tests taken'

#     def take_test(self, test, answers):
#         subject = test.subject
#         correct_answers = test.correct_answers
#         if type(self.tests_taken) == str:
#             self.tests_taken = {}
#         self.tests_taken.update(
#             {
#                 subject: Student._test_check(
#                     answers, correct_answers, test.pass_score
#                 )
#             }
#         )


#     def _test_check(answers, correct_answers, pass_score):
#         result_list = [
#                 answer == correct_answer
#                 for answer, correct_answer in zip(answers, correct_answers)
#             ]
#         # print(result_list)
#         result = sum(result_list)
#         # print(result)
#         result = round(result * 100 / len(answers))
#         if result >= pass_score:
#             return f'Passed! ({result}%)'
#         else:
#             return f'Failed! ({result}%)'


# papers = [
#     Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
#     Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
#     Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
#     Testpaper(
#         'Informatics',
#         ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
#          '18B', '19D', '20D'],
#         '90%'
#     )
# ]

# papers = [
#     Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
#     Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
#     Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
#     Testpaper(
#         'Informatics',
#         ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
#          '18B', '19D', '20D'],
#         '90%'
#     )
# ]

# student = Student()

# student.choices = [
#     ['1A', '2C', '3D', '4B', '5A'],
#     ['1C', '2A', '3D', '4A'],
#     ['1D', '2C', '3C', '4B', '5D', '6A', '7A'],
#     ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8B', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
#      '18B', '19D', '20D']
# ]

# for i in range(4):
#     student.take_test(papers[i], student.choices[i])

# print(student.tests_taken)

# # {'Maths': 'Passed! (80%)', 'Chemistry': 'Passed! (75%)', 'Computing': 'Passed! (86%)', 'Informatics': 'Passed! (95%)'}

'''№ 9.9 Класс TicTacToe'''

# from itertools import cycle

# class TicTacToe:
#     def __init__(self):
#         self.field = [[' ' for _ in range(3)] for _ in range(3)]
#         self.turn = cycle(['X', 'O'])
#         self.win = None

#     def mark(self, x, y):
#         # x_o = {'X': 'крестиком', 'O': 'ноликом'}
#         x -= 1
#         y -= 1
#         if self.win is None:
#             if self.field[x][y] == ' ':
#                 self.field[x][y] = next(self.turn)
#                 # print(
#                     # f'помечаем {x_o[self.field[x][y]]} клетку с координатами '
#                     # f'({x + 1}, {y + 1})'
#                 # )
#                 self._win_check()
#             else:
#                 print('Недоступная клетка')
#         else:
#             print('Игра окончена')

#     def _win_check(self):
#         field = self.field

#         for row in field:
#             if len(set(row)) == 1 and row[0] != ' ':
#                 print(set(row), ' строка')
#                 self.win = row[0]
#                 return None

#         for col in range(3):
#             if len(set([row[col] for row in field]))  == 1 and field[0][col] != ' ':
#                 print(set([row[col] for row in field]), 'колонка')
#                 self.win = field[0][col]
#                 return None

#         if len(set([field[x][x] for x in range(3)])) == 1 and field[0][0] != ' ':
#             print(set([field[x][x] for x in range(3)]), ' главная диагональ')
#             self.win = field[0][0]
#             return None

#         draw = True
#         for row in field:
#             if ' ' in field:
#                 draw = False
#                 print('govno')
#                 break
#         if draw:
#             self.win = 'ничья'

#         # if len(set([field[x][(-x-1)] for x in range(3))) == 1 and field[0][-1] != ' ':
#         #     self.win = field[0][-1]

#     def winner(self):
#         return self.win

#     def show(self):
#         for row in range(3):
#             print(f"{'|'.join(self.field[row])}\n-----")

# tictactoe = TicTacToe()

# tictactoe.mark(1, 1)
# tictactoe.mark(1, 3)
# tictactoe.mark(3, 1)
# tictactoe.mark(2, 1)

# print(tictactoe.winner())

# tictactoe.mark(3, 2)
# tictactoe.mark(3, 3)
# tictactoe.mark(1, 2)
# tictactoe.mark(2, 2)
# tictactoe.mark(2, 3)

# print(tictactoe.winner())
# tictactoe.show()
# tictactoe.mark(2, 2)
# print(tictactoe.winner())

# # None
# # Ничья
# # X|X|O
# # -----
# # O|O|X
# # -----
# # X|X|O
# # Игра окончена
# # Ничья

'''№ 9.10 Классы Game и Cell'''

# from random import randint as rand

# class Game:
#     def __init__(self, rows, cols, mines):
#         self.rows = rows
#         self.cols = cols
#         self.mines = mines
#         self.board = [
#             [Cell(row, col)
#              for col in range(self.cols)] for row in range(self.rows)
#         ]
#         self._mines_fill(self.mines)
#         self._get_neighbours(self.board)

#     def _mines_fill(self, mines):
#         mines_count = 0
#         while mines_count < mines:
#             mine_row = rand(0, self.rows - 1)
#             mine_col = rand(0, self.cols - 1)
#             cell = self.board[mine_row][mine_col].mine
#             if not cell:
#                 self.board[mine_row][mine_col].mine = True
#                 mines_count += 1
#                 # print(f'Мина № {mines_count}')
#                 # print(f'mine_row = {mine_row}, mine_col = {mine_col}')

#     def _get_neighbours(self, board):
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 count = 0
#                 for i,j in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
#                     if 0 <= row + i < self.rows and 0 <= col + j < self.cols and board[row + i][col + j].mine:
#                         count += 1
#                 self.board[row][col].neighbours = count




#     def board_print(self):
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 if self.board[i][j].mine:
#                     print(1, end=' ')
#                 else:
#                     print('0', end=' ')
#             print()

# class Cell:
#     def __init__(self, row, col, mine=False, neighbours=0):
#         self.row = row
#         self.col = col
#         self.mine = mine
#         self.neighbours = neighbours

'''№ 9.11 Класс Curencu'''

# class Currency:
#     CONVERTATION = {
#         'RUB-USD': 81.818182,
#         'RUB-EUR': 90,
#         'USD-EUR': 1.1,
#         'USD-RUB': 0.012222,
#         'EUR-RUB': 0.011111,
#         'EUR-USD': 0.909091,
#     }

#     def __init__(self, amount, cur):
#         self.amount = amount
#         self.cur = cur

#     def change_to(self, new):
#         if self.cur != new:
#             cur_pair = f'{self.cur}-{new}'
#             self.amount /= self.CONVERTATION[cur_pair]
#             self.amount = round(self.amount, 1)
#             self.cur = new

#     def __str__(self):
#         return f'{self.amount} {self.cur}'

#     def __add__(self, other):
#         new = type(self)(other.amount, other.cur)
#         new.change_to(self.cur)
#         new.amount += self.amount
#         return new

#     def __sub__(self, other):
#         new = type(self)(other.amount, other.cur)
#         new.change_to(self.cur)
#         new.amount -= self.amount
#         return new


#     def __mul__(self, other):
#         new = type(self)(other.amount, other.cur)
#         new.change_to(self.cur)
#         new.amount *= self.amount
#         return new

#     def __truediv__(self, other):
#         new = type(self)(other.amount, other.cur)
#         new.change_to(self.cur)
#         new.amount /= self.amount
#         return new

# money_r = Currency(20, 'RUB')
# money_e = Currency(20, 'EUR')
# money_d = Currency(20, 'USD')

# print(money_r, money_e, money_d, sep=' | ')
# print(money_r)
# money_r.change_to('USD')
# print(money_r)

# print(Currency(5, 'EUR') + Currency(5, 'EUR'))# 10 EUR
# print(Currency(5, 'EUR') + Currency(11, 'USD'))# 15.0 EUR
# print(Currency(5, 'RUB') + Currency(11, 'USD'))# 905.0 RUB
# print(Currency(5, 'USD') * Currency(5, 'EUR'))# 27.5 USD

'''№ 9.12 Класс Selfie'''

# class Selfie:
#     pass

