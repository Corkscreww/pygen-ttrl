'''МОДУЛЬ 7. НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ'''

'''7.1 Наследование'''

'''№ 7.1.4 Классы User и PremiumUser'''

# class User(object):
#     def __init__(self, name):
#         self.name = name

#     def skip_ads(self):
#         return False


# class PremiumUser(User):
#     def skip_ads(self):
#         return True

# user = User('Arthur')
# premium_user = PremiumUser('Arthur')
# print(user.skip_ads())
# print(premium_user.skip_ads())

'''№ 7.2.3 Классы Triangle и EquilateralTriangle'''


# class Triangle:
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c

#     def perimeter(self):
#         return self.a + self.b + self.c

# class EquilateralTriangle(Triangle):
#     def __init__(self, side):
#         super().__init__(side, side, side)

# triangle1 = Triangle(3, 4, 5)
# triangle2 = EquilateralTriangle(3)
# print(triangle1.perimeter())
# print(triangle2.perimeter())

'''№ 7.2.4 Класс Counter и DoubleCounter'''

# class Counter:
#     def __init__(self, start=0):
#         self.value = start

#     def inc(self, value=1):
#         self.value += value

#     def dec(self, value=1):
#         if self.value - value > 0:
#             self.value -= value
#         else:
#             self.value = 0

# class DoubledCounter(Counter):
#     def inc(self, value=1):
#         self.value += value * 2


#     def dec(self, value=1):
#         if self.value - value * 2 > 0:
#             self.value -= value * 2
#         else:
#             self.value = 0

# counter = DoubledCounter(20)
# print(counter.value)
# counter.inc()
# counter.inc(5)
# print(counter.value)
# counter.dec()
# counter.dec(10)
# print(counter.value)
# counter.dec(10)
# print(counter.value)

'''№ 7.3.3 Класс FuzzyStrung'''

# from functools import total_ordering

# @total_ordering
# class FuzzyString(str):
#     def __init__(self, string):
#         self.string = string.lower()

#     def __ne__(self, other):
#         if isinstance(other, FuzzyString):
#             return self.string != other.string
#         elif isinstance(other, str):
#             return self.string != other.lower()
#         return NotImplemented

#     def __eq__(self, other):
#         if isinstance(other, FuzzyString):
#             return self.string == other.string
#         elif isinstance(other, str):
#             return self.string == other.lower()
#         return NotImplemented

#     def __gt__(self, other):
#         if isinstance(other, FuzzyString):
#             return self.string > other.string
#         elif isinstance(other, str):
#             return self.string > other.lower()
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, FuzzyString):
#             return self.string < other.string
#         elif isinstance(other, str):
#             return self.string < other.lower()
#         return NotImplemented

#     def __le__(self, other):
#         if isinstance(other, FuzzyString):
#             return self.string <= other.string
#         elif isinstance(other, str):
#             return self.string <= other.lower()
#         return NotImplemented

#     def __contains__(self, other):
#         if isinstance(other, FuzzyString):
#             return self.string in other.string
#         elif isinstance(other, str):
#             return self.string in other.lower()
#         return NotImplemented



# s = FuzzyString('BeeGeek')

# print(s != 'BEEGEEK')
# print(s == 'BEEGEEK')
# print(s != 'beegeek')
# print(s == 'beegeek')
# print(s >= 'BEEGEEK')
# print(s <= 'BEEGEEK')
# print(s > 'BEEGEEK')
# print(s < 'BEEGEEK')

'''№ 7.4.5 Класс NumberList'''

from collections import UserList

class NumberList(UserList):
    def __init__(self, iterable=[]):
        UserList.__init__(iterable)
        for el in iterable:
            if isinstance(el, (int, float)):
                self.data.append(el)
            else:
                raise TypeError(
                    'Элементами экземпляра класса могут быть только числа'
                )

    def __add__(self, other):
        if all(map(lambda x: isinstance(x, (int, float)), other)):
            self.data += other
        else:
            raise TypeError(
                'Элементами экземпляра класса могут быть только числа'
            )

    def __append__(self, value):
        if isinstance(value, (int, float)):
            self.data.append(value)
        else:
            raise TypeError(
                'Элементами экземпляра класса могут быть только числа'
            )

    def __setitem__(self, index, value):
        if isinstance(value, (int, float)):
            self.data[index] = value
        else:
            raise TypeError(
                'Элементами экземпляра класса могут быть только числа'
            )

numberlist = NumberList([1, 2])
numberlist.append(3)
numberlist.extend([4, 5])
numberlist.insert(0, 0)
print(numberlist)


'''№ 7.5.4 Функции is_iterator() и is_iterable() '''


# from collections.abc import Iterable, Iterator

# def is_iterable(obj):
#     return isinstance(obj, Iterable)

# def is_iterator(obj):
#     return isinstance(obj, Iterator)

# print(is_iterator(123))
# print(is_iterator([1, 2, 3]))
# print(is_iterator((1, 2, 3)))
# print(is_iterator('123'))
# print(is_iterator(iter('123')))
# print(is_iterator(map(int, '123')))

'''№ 7.5.5 Класс CustomRange'''

# from collections.abc import Collection
# class CustomRange(Collection):
#     def __init__(self, *args):
#         self.seq = []
#         for arg in args:
#             if isinstance(arg, int):
#                 self.seq.append(arg)
#             if isinstance(arg, str):
#                 arg = arg.split('-')
#                 self.seq.extend(
#                     num for num in range(int(arg[0]), int(arg[1]) + 1)
#                 )

#     def __contains__(self, other):
#         return other in self.seq

#     def __len__(self):
#         return len(self.seq)

#     def __iter__(self):
#         return iter(self.seq)

#     def __reversed__(self):
#         yield from (
#             self.seq[index] for index in range(-1, -1 - len(self.seq), -1))

#     def __getitem__(self, index):
#         return self.seq[index]

# customrange = CustomRange()
# print(len(customrange))
# print(*customrange)
# print(*reversed(customrange))
