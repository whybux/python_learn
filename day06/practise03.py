"""
实现判断一个数是不是素数的函数
"""
import math


def is_prime(num):
    is_prime1 = True
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            is_prime1 = False
            break
    return is_prime1


inputValue = int(input("请输入一个正整数"))

if is_prime(inputValue):
    print("%d是一个素数" % inputValue)
else:
    print("%d不是一个素数" % inputValue)
