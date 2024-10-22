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

"""№ 8.6.2 Класс MusicAlbum"""

# from dataclasses import dataclass

# @dataclass(frozen=True)
# class MusicAlbum:
#     title: str
#     artist: str
#     genre: str
#     year: int

#     def __repr__(self):
#         return f"MusicAlbum(title='{self.title}', artist='{self.artist}')"

#     def __eq__(self, other):
#         return (
#             self.title == other.title and
#             self.artist == other.artist and
#             self.year == other.year
#         )

# musicalbum = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
# try:
#     musicalbum.genre = 'Post-punk, New Wave, Indie Rock'
# except:
#     print('Error')
