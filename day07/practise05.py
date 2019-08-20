"""
练习5：计算指定的年月日是这一年的第几天

"""


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    months = [[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
              [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    mon = months[0] if is_leap_year(year) else months[1]
    day = date
    for index in range(0, month - 1):
        day += mon[index]
    return day


def main():
    day = which_day(2017, 12, 31)
    print("day = %d" % day)


if __name__ == '__main__':
    main()
