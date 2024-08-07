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