# 计算分数
total = 0.0
def jisuan():
    global total
    for i in range(1,101):
        if i % 2:
            total += 1 / float(i)
        else:
            total -= 1/float(i)
    print(total)

if __name__ == "__main__":
    jisuan()