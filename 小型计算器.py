# 小型计算器
def test():
    try:
        a = float(input("Please input first number : "))
        string = str(input("Please input( + - * / ) :"))
        list1 = ["+","-","*","/"]
        while string not in list1:
            string = str(input("Please input( + - * / ) again :"))
        b = float(input("Please input second number : "))
        if string == "+":
            print(a + b)
        elif string == "-":
            print(a - b)
        elif string == "*":
            print(a * b)
        elif string == "/":
            print(a / b)
    except (ZeroDivisionError,ValueError) as e:
        print("Find error:",end=" ")
        print(e)
    else:
        print("Think you !!")
    finally:
        print("Clean up......")
        del a,b
if __name__ == "__main__":
    test()