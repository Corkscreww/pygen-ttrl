'''Модуль 6. Протоколы'''

'''Блок 6.1 Протокол итерируемых объектов и итераторов'''

'''№ 6.1.3 Класс AttrsIterator'''

# class AttrsIterator(object):
#     def __init__(self, obj):
#         self.obj = obj

#     def __iter__(self):
#         yield from ((attr, value) for attr, value in self.obj.__dict__.items())

# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

# user = User('Debbie', 'Harry', 77)
# attrsiterator = AttrsIterator(user)
# print(*attrsiterator)
