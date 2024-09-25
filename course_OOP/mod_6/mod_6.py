'''Модуль 6. Протоколы'''

'''Блок 6.1 Протокол итерируемых объектов и итераторов'''

'''№ 6.1.1 Класс Point'''

# class Point(object):
#     def __init__(self, x: int, y: int, z:int) -> None:
#         self.x, self.y, self.z = x, y, z

#     def __repr__(self) -> str:
#         return f'Point({self.x}, {self.y}, {self.z})'

#     def __iter__(self):
#         return iter((self.x, self.y, self.z))

#     def __next__(self):
#         return next(self.__iter__())
# points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
# print(points)

'''№ 6.1.2 Класс DevelopmentTeam'''

# class DevelopmentTeam(object):
#     def __init__(self):
#         self.senior = []
#         self.junior = []

#     def add_junior(self, *args):
#         for jun in args:
#             self.junior.append(jun)


#     def add_senior(self, *args):
#         for sen in args:
#             self.senior.append(sen)

#     def __iter__(self):
#         yield from ((name, 'junior') for name in self.junior)
#         yield from ((name, 'senior') for name in self.senior)

# pied_piper = DevelopmentTeam()

# pied_piper.add_senior('Richard', 'Gilfoyle', 'Dinesh', 'Erlich')
# pied_piper.add_junior('Jared', 'Big Head')

# print(*pied_piper, sep='\n')
# print(len(list(pied_piper)))

'''№ 6.1.3 Класс AttrsIterator'''

# class AttrsIterator(object):
#     def __init__(self, obj):
#         self.obj = iter(obj.__dict__.items())
#         self._count = 0

#     def __iter__(self):
#         return self.obj

#     def __next__(self):
#         return next(self.obj)
# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

# class Kemal:
#     def __init__(self):
#         self.family = 'cats'
#         self.breed = 'british'
#         self.master = 'Kemal'


# kemal = Kemal()
# attrs_iterator = AttrsIterator(kemal)

# print(next(attrs_iterator))
# print(next(attrs_iterator))
# print(next(attrs_iterator))

# '''№ 6.1.7 Класс LoopTracker 🌶️'''

# class LoopTracker(object):
#     def __init__(self, iterable):
#         if iterable:
#             self.fst = iterable[0]
#             self.iterable = iter(iterable)
#         self.count = 0
#         self.lst = 0
#         self.empty = False
#         self.empty_count = 0

#     def __iter__(self):
#         return self.iterable

#     def __next__(self):
#         try:
#             self.lst = next(self.iterable)
#             self.count += 1
#             return self.lst
#         except StopIteration:
#             self.empty_count += 1
#             self.empty = True
#             raise StopIneration

#     @property
#     def accesses(self):
#         return self.count

#     @property
#     def empty_accesses(self):
#         return self.empty_count

#     @property
#     def first(self):
#         return self.fst

#     @property
#     def last(self):
#         return self.lst

#     def is_empty(self):
#         return self.empty

# loop_tracker = LoopTracker([1, 2, 3])
# print(next(loop_tracker))
# print(loop_tracker.last)
# print(next(loop_tracker))
# print(loop_tracker.last)
# print(next(loop_tracker))
# print(loop_tracker.last)

'''№ 6.1.5 Класс RandomLooper'''

# class RandomLooper(object):
# self __init__(self, *args): pass

'''№ 6.2.3 Класс CyclicList'''

# from itertools import cycle

# class CyclicList(object):
#     def __init__(self, iterable):
#         self.iterable = list(iterable)
#         self._itr = cycle(iterable)

#     def _init_iter(self, iterable):
#         self._itr = cycle(iterable)

#     def append(self, object):
#         self.iterable.append(object)
#         self._init_iter(self.iterable)

#     def pop(self, index=None):
#         if index if None:
#             index = len(self.iterable) - 1
#         result = self.iterable.pop(index)
#         self._init_iter(self.iterable)
#         return result

#     def __len__(self):
#         return len(self.iterable)

#     def __getitem__(self, index):
#         return next(self._itr)


# cyclic_list = CyclicList([1, 2, 3])
# cyclic_list.append(4)
# print(cyclic_list.pop())
# print(len(cyclic_list))
# print(cyclic_list.pop(0))
# print(len(cyclic_list))

'''6.3.2 Функция non_closed_files()'''

# def non_closed_files(files):
#     result = []
#     for file in files:
#         if file.closed is False:
#             result.append(file)
#     return result

# with (
#     open('file1.txt', 'w', encoding='utf-8') as file1,
#     open('file2.txt', 'w', encoding='utf-8') as file2,
#     open('file3.txt', 'w', encoding='utf-8') as file3
# ):
#     file1.write('i am the first file')
#     file2.write('i am the second file')
#     file3.write('i am the third file')

# file1 = open('file1.txt', encoding='utf-8')
# file3 = open('file3.txt', encoding='utf-8')

# for file in non_closed_files([file1, file2, file3]):
#     print(file.read())

'''№ 6.5.4 Класс ReadableTextFile'''

# class ReadableTextFile:
#     def __init__(self, filename):
#         self.filename = filename

#     def __enter__(self):
#         self.file = open(self.filename, 'r', encoding='utf-8')
#         return (line.strip() for line in self.file)

#     def __exit__(self, *args, **kwargs):
#         self.file.close()

# with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
#     print('Только посмотрите!', file=file)
#     print('Как величаво она парит в воздухе', file=file)
#     print('Как орел', file=file)
#     print('На воздушном шаре', file=file)
# with ReadableTextFile('glados_quotes.txt') as file:
#     for line in file:
#         print(line)

'''№ 6.6.2 Контекстный менеджер reversed_print ??????????????????'''

# import sys
# from contextlib import contextmanager

# @contextmanager
# def reversed_print():
#     yield

'''№6.6.3 Контекстный менеджер safe_write ?????????????????'''

# from contextlib import contextmanager

# @contextmanager
# def safe_write(filename):
#     try:

#         with open(filename, encoding='utf-8') as file:
#             tmp = file.readlines()
#         file = open(filename, 'w', encoding='utf-8')
#         yield file
#         file.close()


#     except Exception as error:
#         print(f'Во время записи в файл было возбуждено исключение: '
#               f'{type(error)}')
#         file.writelines(tmp)

# with safe_write('undertale.txt') as file:
#     file.write('Тень от руин нависает над вами, наполняя вас решительностью')
# with open('undertale.txt') as file:
#     print(file.read())
