''' МОДУЛЬ 8. ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ'''

'''8.1 Слоты, аттрибут __slots__'''

'''№ 8.1.1 Класс shape'''

# class Shape:
#     __slots__ = ('name', 'color', 'area')

#     def __init__(self, name, color, area):
#         self.name, self.color, self.area = name, color, area

#     def __str__(self):
#         return f'{self.color} {self.name} ({self.area})'

#     def __eq__(self, other):
#         return self.area == other.area
    
#     def __lt__(self, other):
#         return self.area < other.area

# print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))
# print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))
