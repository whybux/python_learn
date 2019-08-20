"""
寻找“完美数”。
"""
import math

start = 1
while True:
    start += 1
    sum = 0
    for x in range(1, int(math.sqrt(start)) + 1):
        if start % x == 0:
            sum += x
            if x != 1:
                sum += start / x

    if start == sum:
        print("%d 是一个完美数" % start)
