def p_even(n):
    i = 0
    s = 0.0
    for i in range(2, n + 1, 2):
        s += 1 / i
    return s


def p_odd(n):
    s = 0.0
    for i in range(1, n + 1, 2):
        s += 1 / i
    return s


if __name__ == '__main__':
    n = int(input('input a number:'))
    if n % 2 == 0:
        sum = p_even(n)
    else:
        sum = p_odd(n)
    print(sum)
