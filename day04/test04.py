"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

import random

rand = random.randint(1, 101)

counter = 0
while True:
    counter += 1
    inputValue = int(input("猜一猜数字是几？"))

    if inputValue > rand:
        print("大一点")
    elif inputValue < rand:
        print("小一点")
    else:
        print("猜对了")
        break
print("你一共猜了%d次" % counter)
if counter > 7:
    print("你的智商有点欠缺")
