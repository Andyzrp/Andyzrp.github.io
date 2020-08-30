count = 0
tlag = False
h = [0.9, 1.2, 1.22, 1.1, 1.6, 0.99]

for i in range(0, len(h)-1):
    if tlag == False and h[i] < h[i+1]:
        tlag = True
        continue

    if tlag == True and h[i] > h[i+1]:
        count += 1
        tlag = False
        continue
print(count)
