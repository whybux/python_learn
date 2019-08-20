"""
输入两个正整数计算最大公约数和最小公倍数

"""

aInput = int(input("请输入一个正整数："))
bInput = int(input("请再输入一个正整数："))

if aInput > bInput:
    aInput, bInput = bInput, aInput

for factor in range(aInput, 0, -1):
    if aInput % factor == 0 and bInput % factor == 0:
        print("%d,%d的最大公约数是 %d" % (aInput, bInput, factor))
        print("%d,%d的最小公倍数是 %d" % (aInput, bInput, aInput * bInput / factor))
        break
