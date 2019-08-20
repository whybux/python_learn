"""
案例1：双色球选号
"""
import random


def print_select(balls):
    # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for 循环当中。
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")
        print("%02d" % ball, end=" ")


def random_select():
    red_balls = [x for x in range(1, 34)]
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(random.randint(1, 16))
    return selected_balls


def main():
    input_value = int(input("请输入选择注数："))
    for _ in range(input_value):
        select_balls = random_select()
        print_select(select_balls)
        print()


if __name__ == '__main__':
    main()
