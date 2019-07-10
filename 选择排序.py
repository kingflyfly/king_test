# 选择排序
test_list = [5,4,2,1,3,0.5,20]
i = 0
while i < len(test_list) - 1:
    for j in range(i+1,len(test_list)):
        if test_list[i] > test_list[j]:
            test_list[i],test_list[j] = test_list[j],test_list[i]
    i += 1
print(test_list)