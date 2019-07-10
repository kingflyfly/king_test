# 阶梯电价
number = float(input("请输入度数： "))
def test(number):
# 链式赋值
    a1,a2,a3 = 1,0.5,0.25
    try:
        if number <= 10:
            print(number * a1,"元")
        elif 10 < number <= 30:
            print(a1 * 10 + a2 * (number - 10),"元")
        elif number > 30:
            print(a1 * 10 + a2 * 20 + a3 * (number - 30),"元")
        else:
            print("error")
    except:
        print("found error!")
    else:
        print("电费计算完成！")
    finally:
        print("清除数据完成")
if __name__ == "__main__":
    test(number)