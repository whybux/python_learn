"""
生成“斐波拉切数列”
"""

inpuValu = int(input("请输入一个正整数"))

last = 0
now = 0
for x in range(1, inpuValu + 1):
    if x == 1:
        now = 1
    else:
        now = last + now
        last = now - last;
    print(now, end=",")