import random


def insertion_sort(seq):
    """ 每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素"""
    n = len(seq)
    for i in range(1, n):
        value = seq[i]    # 保存当前位置的值，因为转移的过程中它的位置可能被覆盖
        # 找到这个值的合适位置，使得前边的数组有序 [0,i] 有序
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]  # 如果前边的元素比它大，就让它一直前移
            pos -= 1
        seq[pos] = value    # 找到了合适的位置赋值就好
        print(f"第{i}轮：", seq)


seq = list(range(10))
random.shuffle(seq)
print("原 始：", seq)
insertion_sort(seq)
