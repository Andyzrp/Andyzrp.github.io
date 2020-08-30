def exchange(a, b):
    a, b = b, a
    return a, b


if __name__ == '__main__':
    x = 10
    y = 20
    print(f'x = {x},y = {y}')
    x, y = exchange(x, y)
    print(f'x = {x},y = {y}')
