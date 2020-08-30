a = ['a', 'b', 'c', 'd', 'a', 'c']
b = [(x, y) for x, y in enumerate(a) if a.count(y) > 1]
print(b)
