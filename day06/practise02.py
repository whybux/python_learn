"""
实现判断一个数是不是回文数的函数。
"""


def is_palindrome(num):
    tempNum = num
    revergeNum = 0
    while tempNum > 0:
        revergeNum = revergeNum * 10 + tempNum % 10
        tempNum //= 10
    return revergeNum == num


# inputValue = int(input("请输入一个正整数"))

# if is_palindrome(inputValue):
#     print("%d是一个回文数" % inputValue)
# else:
#     print("%d不是一个回文数" % inputValue)

if __name__ == "__main__":
    inputValue = int(input("请输入一个正整数"))
    if is_palindrome(inputValue):
        print("%d是一个回文数" % inputValue)
    else:
        print("%d不是一个回文数" % inputValue)
