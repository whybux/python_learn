"""
输入半径计算圆的周长和面积
"""
import math

PI = math.pi
radInput = float(input("请输入圆的半径 "))

circumference = 2 * PI * radInput
area = PI * (radInput ** 2)
print("半径%.2f 对应的周长是%.2f,对应的面积是%.2f" % (radInput,circumference,area))