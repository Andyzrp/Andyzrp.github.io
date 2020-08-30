n = 1
while n <= 7:
    a = int(input('input a number:'))
    while a < 1 or a > 50:
        a = int(input('input a number:'))
    print(a * '*')
    n += 1
