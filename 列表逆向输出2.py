# 列表逆向输出
def shuchu():
    a = []
    b = []
    n = int(input("序列数字个数："))
    while True:
        a.append(int(input("num")))
        if len(a) == n:
            print("输入结束")
            break
    for i in range(len(a),-1):
        print(i)
        b.append(a[i])
    print(a)
    print(b)

if __name__ == "__main__":
    shuchu()
