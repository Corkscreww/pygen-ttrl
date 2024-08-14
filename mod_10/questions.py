from sys import getsizeof
generator = (char.upper() for char in 'stepik')
print(getsizeof(generator))
next(generator)
next(generator)
next(generator)
print(list(generator))