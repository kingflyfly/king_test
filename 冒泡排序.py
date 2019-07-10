a = [5,4,2,1,3]
j = 0
while j < len(a) - 1:
    for i in range(len(a)-1-j):
        if a[i] > a[i + 1]:
            a[i],a[i + 1] = a[i + 1],a[i]
    j += 1
print(a)