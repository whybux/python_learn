"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

xInput = float(input("请输入变量X "))
result = 0
if xInput > 1:
    result = 3 * xInput - 5
elif xInput < -1:
    result = 5 * xInput + 3
else:
    result = xInput + 2

print("result=",result)