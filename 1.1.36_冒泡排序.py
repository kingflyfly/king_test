a = [133,45,34,2]
# print(sorted(a))
print("原始序列:",a)
for j in range(0,len(a) -1 ):
    for i in range(len(a)-1-j):
        if a[i] > a[i + 1]:
            a[i],a[i + 1] = a[i + 1],a[i]
print("排序后序列：",a)