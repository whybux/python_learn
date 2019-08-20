"""
寻找“水仙花数”
"""
import math

for x in range(100, 1000):
    b = x // 100
    s = (x - b * 100) // 10
    g = x - b * 100 - s * 10

    c = (math.pow(b, 3) + math.pow(s, 3) + math.pow(g, 3))

    if c == x:
        print("%d是一个水仙花数" % x)
