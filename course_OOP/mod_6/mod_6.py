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

'''№ 6.2.1 Класс ReversedSequence'''

# class ReversedSequence(object):
#     def __init__(self, sequence):
#         self.sequence = sequence
#         self._count = -1

#     def __len__(self):
#         return len(self.sequence)

#     def __getitem__(self, index):
#         return self.sequence[len(self.sequence) - index - 1]

    # def __iter__(self):
    #     yield from [
    #         self.sequence[num]
    #         for num in range(len(self.sequence) - 1, 0, -1)
    #     ]

#     def __contains__(self, elem):
#         return elem in self.sequence

# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = ReversedSequence(numbers)
# print(reversed_numbers[0])
# numbers.append(6)
# print(reversed_numbers[0])

'''№ 6.2.2 Класс SparseArray'''

# class SparseArray(object):
#     def __init__(self, default):
#         self.array = {}
#         self.default = default

#     def __len__(self):
#         return len(self.array)

#     def __getitem__(self, index):
#         if isinstance(index, int) and index in self.array:
#             return self.array[index]
#         else:
#             return self.default

#     def __setitem__(self, index, value):
#         self.array[index] = value

# array = SparseArray(None)
# array[0] = 'Timur'
# array[1] = 'Arthur'
# print(array[0])
# print(array[1])
# print(array[2])

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
#         if index is None:
#             index = len(self.iterable) - 1
#         result = self.iterable.pop(index)
#         self._init_iter(self.iterable)
#         return result

#     def __len__(self):
#         return len(self.iterable)

#     def __getitem__(self, index):
#         return next(self._itr)

# cyclic_list = CyclicList([1, 2, 3])

# for index, elem in enumerate(cyclic_list):
#     if index > 6:
#         break
#     print(elem, end=' ')

'''№ 6.2.4 Класс SequenceZip'''

# class SequenceZip(object):
#     def __init__(self, *args):
#         self.sequence = list(zip(*args))

#     def __len__(self):
#         return len(self.sequence)

#     def __iter__(self):
#         return iter(self.sequence)

#     def __getitem__(self, index):
#         return self.sequence[index]

# sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'],
# [1, 2, 3])
# print(len(sequencezip))
# print(sequencezip[1])
# print(sequencezip[2])

'''№ 6.2.5 Класс OrderedSet'''

# class OrderedSet(object):
#     def __init__(self, iterable=[]):
#        self._set = []
#        for el in iterable:
#            if el not in self._set:
#                self._set.append(el)

#     def add(self, value):
#         if value not in self._set:
#             self._set.append(value)

#     def discard(self, value):
#         if value in self._set:
#             self._set.remove(value)

#     def __len__(self):
#         return len(self._set)

#     def __iter__(self):
#         return iter(self._set)

#     def __contains__(self, value):
#         return value in self._set

#     def __eq__(self, other):
#         if isinstance(other, OrderedSet):
#             if len(self) == len(other):
#                 for i in range(len(self)):
#                     if self[i] != other[i]:
#                         return False
#                 return True

#         if isinstance(other, set):
#             if len(self) == len(other):
#                 for elem in self:
#                     if elem not in other:
#                         return False
#                 return True

#         return NotImplemented

# orderedset = OrderedSet()
# orderedset.add('green')
# orderedset.add('green')
# orderedset.add('blue')
# orderedset.add('red')
# print(*orderedset)
# orderedset.discard('blue')
# orderedset.discard('white')
# print(*orderedset)

'''№ 6.2.6 Класс AttrDict'''

# class AttrDict(object):
#     def __init__(self, data={}):
#         self.__dict__.update(data)

#     def __getitem__(self, key):
#         return self.__dict__[key]

#     def __setitem__(self, key, value):
#         self.__dict__[key] = value

#     def __len__(self):
#         return len(self.__dict__)

# attrdict = AttrDict()
# attrdict['school_name'] = 'BEEGEEK'
# print(attrdict['school_name'])
# print(attrdict.school_name)

'''№ 6.2.7 Класс PermaDict'''

# class PermaDict(object):
#     def __init__(self, data={}):
#         self._dict = {}
#         self._dict.update(data)

#     def keys(self):
#         return [self._dict.keys()]

#     def values(self):
#         return [self._dict.values()]

#     def items(self):
#         return [self._dict.items()]

#     def __len__(self):
#         return len(self._dict)

#     def __getitem__(self, key):
#         return self._dict[key]

#     def __setitem__(self, key, value):
#         if key not in self._dict:
#             self._dict[key] = value
#         else:
#             raise KeyError('Изменение значения по ключу невозможно')

#     def __delitem__(self, key):
#         del self._dict[key]

# permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})
# try:
#     permadict['name'] = 'Arthur'
# except KeyError as e:
#     print(e)

'''№ 6.2.8 Класс HistoryDict  🌶️'''

# class HistoryDict(object):
#     def __init__(self, data={}):
#         self._dict = {}
#         for el in data:
#             self._dict[el] = []
#             self._dict[el].append(data[el])

#     def keys(self):
#         return self._dict.keys()

#     def values(self):
#         return self._dict.values()

#     def items(self):
#         return self._dict.items()

#     def __len__(self):
#         return len(self._dict)

#     def history(self, key):
#         if key in self._dict:
#             return self._dict[key]
#         return []

#     def all_history(self):
#         return self._dict

#     def __getitem__(self, key=None):
#         if key is not None:
#             return self._dict.get(key)[-1]
#         else:
#             return self.keys()

#     def __setitem__(self, key, value):
#         if key not in self._dict:
#             self._dict[key] = []
#             self._dict[key].append(value)
#         else:
#             self._dict[key].append(value)

#     def __delitem__(self, key):
#         del self._dict[key]

# historydict = HistoryDict({'ducks': 99, 'cats': 1})
# historydict['dogs'] = 1
# print(len(historydict))
# del historydict['ducks']
# del historydict['cats']
# print(len(historydict))

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

