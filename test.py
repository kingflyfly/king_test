# moudle_test
name = "yazhe"
__doc__ = "asd"
def fun(a = 1):
    print(a)
class Person:
    a = "test"
    def __init__(self,a="test"):
        self.r = a
    def test(self):
        print("输出",self.r)
if __name__ == "__main__":
    b = "yanzhe"
    Person(b).test()