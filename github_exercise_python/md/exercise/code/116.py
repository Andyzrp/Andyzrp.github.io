def Hanoi(n, ch1, ch2, ch3):
    if n == 1:
        print(ch1, '->', ch3)
    else:
        Hanoi(n - 1, ch1, ch3, ch2)
        print(ch1, '->', ch3)
        Hanoi(n - 1, ch2, ch1, ch3)


N = int(input("请输入盘子的数量："))
Hanoi(N, 'A', 'B', 'C')
10
