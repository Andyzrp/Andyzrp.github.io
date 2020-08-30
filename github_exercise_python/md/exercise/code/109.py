import random

n = 0
while n < 10:
    x = random.randint(10, 99)  # 获得一个两位的随机整数
    # 判断x是否为素数
    a = 2
    while a < x - 1:
        if x % a == 0:  # 若余数为0，说明x不是素数，结束当前循环
            break
        a += 1
    else:
        print(x)  # 若正常结束循环时，说明x是素数，输出
        n += 1  # 累计素数个数
