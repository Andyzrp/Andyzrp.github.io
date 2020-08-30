import random

i = random.randint(0, 10)
while True:
    s = int(input('请输入一个整数'))
    if s > i:
        print("你猜的太大了")
    elif s < i:
        print("你猜的太小了")
    else:
        print("你猜对了")
        break
