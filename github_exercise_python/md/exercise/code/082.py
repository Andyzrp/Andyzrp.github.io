n = 0
p = input('input a octal number:')
for i in range(len(p)):
    n = n * 8 + ord(p[i]) - ord('0')
print(n)
