a = "cagy"
b = 3

print(''.join([chr(ord(i) + b if ord(i) + b <=
                   122 else ord(i) + b - 26) for i in a]))
