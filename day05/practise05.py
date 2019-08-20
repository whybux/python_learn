"""
Craps赌博游戏
"""
import random

isFirst = True
lastTotal = 0
while True:
    one = random.randint(1, 6)
    two = random.randint(1, 6)
    total = one + two
    print(total)
    if isFirst:
        isFirst = False
        if total == 7 or total == 1:
            print("玩家胜")
            break
        elif total == 2 or total == 3 or total == 12:
            print("庄家胜")
            break
    else:
        if total == 7:
            print("庄家胜")
            break
        elif lastTotal == total:
            print("玩家胜")
            break

    lastTotal = total
