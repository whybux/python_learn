"""
输入一个正整数判断它是不是素数

"""
import math

num = int(input("请输入一个数"))
is_pr = True
end = int(math.sqrt(num))
for x in range(2, end):
    if num % x == 0:
        is_pr = False
        break
    else:
        is_pr = True

if is_pr and num != 1:
    print("%d 是个素数" % num)
else:
    print("%d 不是个素数" % num)
