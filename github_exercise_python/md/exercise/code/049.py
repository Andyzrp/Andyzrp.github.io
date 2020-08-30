def MAXIMUM(x, y): return (x > y) * x + (x < y) * y


def MINIMUM(x, y): return (x > y) * y + (x < y) * x


a = 10
b = 20
print(f'The largar one is {MAXIMUM(a, b)}')
print(f'The lower one is {MINIMUM(a, b)}')
