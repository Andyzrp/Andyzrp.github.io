L = [0, 1, 2, 3, 4]
L.sort()

if len(L) % 2 == 0:
    print((float((L[int(len(L)/2)])+float(L[(int(len(L)/2-1))])))/2)
else:
    print(L[int(len(L)/2)])
