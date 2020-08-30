def main():
    # 输入待验证的偶数
    N = int(input("请输入待验证的偶数："))
    while N < 3 or N % 2 == 1:
        print("输入的数不符合要求")
        N = int(input("请输入待验证的偶数n（n>2）："))
    # 生成素数表
    Prime = set()
    for i in range(2, N + 1):
        Prime.add(i)
    for i in range(2, N + 1):
        if i in Prime:
            for k in range(2 * i, N + 1, i):
                if k in Prime:
                    Prime.remove(k)
    # 验证该偶数能否分解为两个素数之和
    for e in Prime:
        f = N - e
        if f >= e and f in Prime:
            print(N, '=', e, '+', f)


main()
