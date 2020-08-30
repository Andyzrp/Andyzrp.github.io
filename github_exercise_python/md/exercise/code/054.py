a = int(input('input a number:'))
b = a >> 4
c = ~(~0 << 4)
d = b & c
print(f'{a:o}\t{b:o}')
