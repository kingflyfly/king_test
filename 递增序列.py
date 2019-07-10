# 序列递增
att = False
a = []
def xulie():
    global att
    n = int(input("序列数字个数："))
    while True:
        a.append(int(input("num")))
        if len(a) == n:
            print("输入结束")
        # print(a)
            break
    for i in range(len(a)-1):
        if att == False:
            if a[i] > a[i+1]:
                a[i+1] = a[i]
                att = True
                continue
        else:
            if a[i] > a[i+1]:
                print("不是递增序列")
                break
    else:
        print("是递增序列")

if __name__ == "__main__":
    xulie()