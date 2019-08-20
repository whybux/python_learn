"""
输入两个正整数计算最大公约数和最小公倍数
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""
length = int(input("请输入一个正整数"))

for x in range(0, length):
    for y in range(0, length):
        if x >= y:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for x in range(length, 0, -1):
    for y in range(0, length):
        if y + 1 >= x:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for x in range(0, length):
    for y in range(0, length + x):
        if y >= length - 1 - x:
            print("*", end="")
        else:
            print(" ", end="")
    print()
