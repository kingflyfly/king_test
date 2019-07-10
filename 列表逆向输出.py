# 列表逆向输出
def shuchu():
    a = []
    b = []
    n = int(input("序列数字个数："))
    while True:
        a.append(int(input("num")))
        if len(a) == n:
            print("输入结束")
           # print(a)
            break
    c = a.copy()
    for i in range(len(c)):
        b.append(c.pop())
    print(a)
    print(c)
    print(b)

if __name__ == "__main__":
    shuchu()
