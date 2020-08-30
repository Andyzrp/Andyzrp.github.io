import random


def bubble_sort(seq):  # O(n^2), n(n-1)/2 = 1/2(n^2 + n)
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
          # 这里之所以 n-1 还需要 减去 i 是因为每一轮冒泡最大的元素都会冒泡到最后，无需再比较
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
        # 我打印出来让你看清楚每一轮最高、次高、次次高...的小朋友会冒泡到右边
        print(f"第{i+1}轮：", seq)
    print("结 果：", seq)


# 注意 python3 返回迭代器，所以我都用 list 强转了，python2 range 返回的就是 list
seq = list(range(10))
# shuffle inplace 操作，打乱数组
random.shuffle(seq)
print("原 始：", seq)
bubble_sort(seq)
