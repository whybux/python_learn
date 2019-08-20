"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""
import math

aLength = float(input("请输入边长a:"))
bLength = float(input("请输入边长b:"))
cLength = float(input("请输入边长c:"))

if aLength+bLength>cLength and aLength+cLength>bLength and bLength+cLength>aLength:
    totalLength = aLength+bLength+cLength;
    p = (aLength+bLength+cLength)/2
    area = math.sqrt(p*(p-aLength)*(p-bLength)*(p-cLength))
    print("边长为 %f,%f,%f 对应的边长为 %f,面积为 %f" % (aLength,bLength,cLength,totalLength,area))
else:
    print("输入的变成不能组成三角形")
