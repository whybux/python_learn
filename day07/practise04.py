"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

"""
import math


def max2(x):
    max_value1, max_value2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(0, len(x)):
        value = x[index]
        if value > max_value1:
            max_value2 = max_value1
            max_value1 = value
        elif value > max_value2:
            max_value2 = value
    return max_value1, max_value2


def main():
    print(max2([1, 2, 3, 4, 5, 21, 6, 2]))
    print(max2([1, 2, 3, 5, 5, 21, 2]))


if __name__ == '__main__':
    main()
