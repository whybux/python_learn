"""
掷骰子决定做什么事情

"""

import random

num = random.randint(1, 6)
if num == 1:
    str = "123"
elif num == 2:
    str = "2"
elif num == 3:
    str = "3"
elif num == 4:
    str = "4"
elif num == 5:
    str = "5"
else:
    str = "6"


print("随机值%s" % str)
