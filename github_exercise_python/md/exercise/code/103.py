from collections import Counter

li = [1, 2, 3, 1, 1, 2, 3, 1, 2, 5, 6, 4, 1, 2, 4, 5, 6]
N = 5

li_counts = Counter(li)

top_three = li_counts.most_common(N)
print(top_three)
