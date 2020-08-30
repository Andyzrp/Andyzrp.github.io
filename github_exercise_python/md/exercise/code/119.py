from math import *

a = float(input("请输入斜边 1 的长度"))  # 输入实数
b = float(input("请输入斜边 2 的长度"))  # 输入实数
c = a * a + b * b  # 计算,得到的是斜边的平方
c = sqrt(c)  # 开方，得到的是斜边长
print("斜边长为:", c)  # 显示，一项是字符串，一项是 c 表示的斜边长
