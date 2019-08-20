"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""

inpuValue = float(input('请输入华氏温度 '))

result = 1.8 * inpuValue + 32
print("%.1fC 对应的摄氏温度为 %.1f" % (inpuValue, result))
