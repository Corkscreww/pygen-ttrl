'''4.6.1 Класс Person'''

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     @property
#     def fullname(self):
#         return ' '.join([self.name, self.surname])

#     @fullname.setter
#     def fullname(self, new_name=None, new_surname=None):
#         if new_name:
#             self.name = new_name
#         if new_surname:
#             self.surname = new_surname

# person = Person('Mike', 'Pondsmith')
# print(person.name)
# print(person.surname)
# print(person.fullname)

'''4.6.3 Класс QuadraticPolynomial'''

# from math import sqrt

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     @property
#     def x1(self):
#         a, b, c = self.a, self.b, self.c
#         d = b ** 2 - 4 * a * c
#         if d:
#             return (-b - sqrt(d)) / 2 * a
#     @property
#     def x2(self):
#         a, b, c = self.a, self.b, self.c
#         d = b ** 2 - 4 * a * c
#         if d:
#             return (-b + sqrt(d)) / 2 * a

#     @property
#     def view(self):
#         a, b, c = self.a, self.b, self.c
#         return f'{a}x^2 + {b}x + {c}'

#     @property
#     def coefficients(self):
#         return (self.a, self.b, self.c)

#     @coefficients.setter
#     def coefficients(self, a=None, b=None, c=None):
#         if a:
#             self.a = a
#         if b:
#             self.b = b
#         if c:
#             self.c = c

# polynom = QuadraticPolynomial(1, 2, -3)
# print(polynom.view)
# print(polynom.coefficients)

'''4.7.4 Класс Pet'''

# class Pet:
#     pets = []
#     def __init__(self, name):
#         self.name = name
#         Pet.pets.append(self)

#     @classmethod
#     def first_pet(cls):
#         return cls.pets[0] if cls.pets[0] else None
#     @classmethod
#     def last_pet(cls):
#         return cls.pets[-1] if cls.pets[-1] else None

#     @classmethod
#     def num_of_pets(cls):
#         return len(cls.pets)

# pet1 = Pet('Ratchet')
# pet2 = Pet('Clank')
# pet3 = Pet('Rivet')
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())