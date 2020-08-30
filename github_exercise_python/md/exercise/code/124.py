import random


def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        # 我们假设当前下标的元素是最小的
        min_idx = i
        for j in range(i+1, n):
            # 从 i 的后边开始找到最小的元素，得到它的下标
            if seq[j] < seq[min_idx]:
                # 一个 j 循环下来之后就找到了最小的元素它的下标
                min_idx = j
        if min_idx != i:
            # swap
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
        print(f"第{i+1}轮：", seq)

    print("结 果：", seq)


seq = list(range(10))
random.shuffle(seq)
print("原 始：", seq)
select_sort(seq)
