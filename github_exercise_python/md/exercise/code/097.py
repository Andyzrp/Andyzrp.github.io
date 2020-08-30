filename = input('输入文件名:')
ch = input('输入字符串:')

with open(filename, "w", encoding="utf8") as f:
    while ch != '#':
        f.write(ch)
