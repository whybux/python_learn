"""
练习6：打印杨辉三角。

"""


def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for a in range(len(yh)):
        yh[a] = [None] * (a + 1)
        for b in range(len(yh[a])):
            if b == 0 or b == len(yh[a]) - 1:
                yh[a][b] = 1
            else:
                yh[a][b] = yh[a - 1][b - 1] + yh[a - 1][b]
        print(yh[a])


if __name__ == '__main__':
    main()
