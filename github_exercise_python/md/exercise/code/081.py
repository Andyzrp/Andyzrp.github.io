a = 809
for i in range(10, 100):
    b = i * a
    if 1000 <= b <= 10000 and 8 * i < 100 <= 9 * i:
        print(b, ' = 800 * ', i, ' + 9 * ', i)
