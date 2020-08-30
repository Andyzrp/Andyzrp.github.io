a = int(input("请输入一个数字:"))
x = str(a)
flag = True

for i in range(len(x) // 2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print(f"{a} 是一个回文数!")
else:
    print(f"{a} 不是一个回文数!")
