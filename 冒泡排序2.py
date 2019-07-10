# 复习起泡法排序
def paixu():
    try:
        a = []
        n = int(input("序列数字个数："))
        while True:
            a.append(int(input("num")))
            if len(a) == n:
                print("输入结束")
                break
    except:
        print("Please input right num!!!")
    print("您输入的序列：",a)
    for j in range(len(a)-1):
        for i in range(len(a)-1-j):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
    print("修改后的序列：",a)

if __name__ == "__main__":
    paixu()