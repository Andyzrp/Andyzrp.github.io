string = input('please input a string:')
with open('test.txt', 'w', encoding='utf8') as f:
    f.write(string)
