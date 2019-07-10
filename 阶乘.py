# 阶乘
def jiecheng(a):
    sum = 1
    for i in range(1,a+1):
        print(sum,"*",i,"=",end=" ")
        sum = sum * i
        print(sum)
    print("阶乘结果为:",sum)

if __name__ == "__main__":
    b = int(input("请输入你知道的阶乘："))
jiecheng(b)




