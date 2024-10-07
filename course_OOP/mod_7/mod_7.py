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
