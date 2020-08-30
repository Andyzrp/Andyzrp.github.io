f1 = 1
f2 = 1
for i in range(1, 22):
    print(f'{f1:>12}\t{f2:>12}', end='\t')
    if (i % 3) == 0:
        print()
    f1 = f1 + f2
    f2 = f1 + f2
