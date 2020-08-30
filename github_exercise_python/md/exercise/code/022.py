import itertools

first = ('a', 'b', 'c')
second = ('x', 'y', 'z')

check_list = [('a', 'x'), ('c', 'x'), ('c', 'z')]

for i in itertools.permutations(first, 3):
    f = lambda a, b: len([True for j in zip(a, b) if j not in check_list])
    if f(i, second) == 3:
        print(list(zip(i, second)))
