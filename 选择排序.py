# 选择排序
test_list = [5,4,2,9,3,6]
i = 0
while i < len(test_list) - 1:
    minIndex = i
    j = i + 1
    while j < len(test_list):
        if test_list[j] < test_list[minIndex]:
            minIndex = j
        j += 1
    if minIndex != i:
        temp = test_list[i]
        test_list[i] = test_list[minIndex]
        test_list[minIndex] = temp
    i += 1
print(test_list)