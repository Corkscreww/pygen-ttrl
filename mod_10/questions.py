from itertools import tee
numbers = [1, 2, 3, 4, 5]
iter1, iter2 = tee(numbers)
numbers[1] = 20
print(next(iter1), next(iter2))
print(next(iter1), next(iter2))