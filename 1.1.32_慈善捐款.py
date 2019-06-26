# 捐款金额
def test():
    sum,i = 0,1
    while i<= 1000:
        num = float(input("捐款金额："))
        sum += num
        if sum >= 100000:
            break
        else:
            i += 1
    print("捐款人数","=",i)
    print("平均捐款金额","=",round(sum / i,2))
if __name__ == "__main__":
    test()
