# 自幂数
start = 0
end = 0
digit = 0
m = 0
n = int(input('请选择自幂数的位数【1，2，3，4，5，6】:'))
while 0 < n < 7:
    start = pow(10, n - 1)
    end = pow(10, n) - 1
    print(n, '位数的自幂数有:')
    for k in range(start, end + 1):
        m = k
        total = 0
        while m != 0:
            digit = m % 10
            total += pow(digit, n)
            m = m // 10
        if total == k:
            print(str(k), end=' ')
    n = int(input('\n 请选择自幂数的位数【1，2，3，4，5，6】:'))
else:
    print('输入位数不在范围内,程序结束。')
