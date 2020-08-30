fp = open('test1.txt', encoding='utf8')
a = fp.read()
fp.close()

fp = open('test2.txt', encoding='utf8')
b = fp.read()
fp.close()

fp = open('test3.txt', 'w', encoding='utf8')
l = list(a + b)
l.sort()
s = ''
s = s.join(l)
fp.write(s)
fp.close()
