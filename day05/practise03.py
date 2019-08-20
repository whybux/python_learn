"""
“百钱百鸡”问题
"""

total = 100
faValue = 5
maValue = 3
littleValue = 3
for fa in range(0, total // faValue):
    for ma in range(0, total // maValue):
        last = total - fa - ma
        if total == (fa * faValue + ma * maValue + last / littleValue):
            print("%d只公鸡 %d母鸡 %d小鸡" % (fa, ma, last))
