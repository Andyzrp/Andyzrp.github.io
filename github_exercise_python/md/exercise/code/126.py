a = {1: 1, 2: 0, 3: 0}

for i in range(1, 22):
    print(f'{i} {sum(a.values())} {a}')
    tmp = a[3]
    a[3] += a[2]
    a[2] = a[1]
    a[1] = tmp
