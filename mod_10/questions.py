positive = (1, 2, 3)
negative = map(lambda x: -x, positive)
for a, b in zip(positive, negative):
    print(a + b)