"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E
"""

value = float(input("请输入分数"))

if value >= 90:
    str = "A"
elif value >= 80:
    str = "B"
elif value >= 70:
    str = "C"
elif value >= 60:
    str = "D"
else:
    str = "E"

print("%f分对应的成绩是%s" % (value,str))
