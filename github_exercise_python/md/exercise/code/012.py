from math import sqrt

h = 0
leap = 1

for m in range(101, 201):
    k = int(sqrt(m + 1))
    for i in range(2, k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print(m)
        h += 1
    leap = 1

print(f'共计有 {h} 个')
