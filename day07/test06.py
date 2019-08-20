"""
实现一个生成斐波拉切数列的生成器
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for x in fib(20):
        print(x, end=",")


if __name__ == "__main__":
    main()
