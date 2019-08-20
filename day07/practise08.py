"""
综合案例2：约瑟夫环问题

《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。

"""


def main():
    persons = [True] * 30
    start = 0
    for _ in range(15):
        num = 1
        while True:
            index = start % 30
            start += 1

            if persons[index]:
                if num == 9:
                    persons[index] = False
                    print(index)
                    break
                num += 1

    print(persons)

    index = 0
    for _ in range(15):
        index += 8
        if index >= len(persons):
            index = index - len(persons)
        persons.pop(index)

    print(persons)


if __name__ == '__main__':
    main()
