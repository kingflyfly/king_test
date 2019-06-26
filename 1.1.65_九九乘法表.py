# 九九乘法表
def jiujiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print(j,"*",i,"=",i * j," ",end=" ")
        print()

if __name__ == "__main__":
    jiujiu()