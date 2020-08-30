A = [23, 25, 44, 66, 45, 334, 556]

L = [A[i]-A[i-1] for i in range(len(A)-1, 0, -1)]

print(L)
