"""
实现计算求最大公约数和最小公倍数的函数
"""


def gcd(x, y):
    if x > y:
        x, y = y, x
    result = 0
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            result = factor
            break
    return result


def lcm(x, y):
    return x * y / gcd(x, y)


xInput = int(input("请输入一个正整数"))
yInput = int(input("请输入一个正整数"))

print("%d,%d的最大公约数是%d" % (xInput, yInput, gcd(xInput, yInput)))
print("%d,%d的最小公倍数是%d" % (xInput, yInput, lcm(xInput, yInput)))
