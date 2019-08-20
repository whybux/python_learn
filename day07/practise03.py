"""
练习3：设计一个函数返回给定文件名的后缀名。

 获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
"""


def get_suffix(filename='', has_dot=True):
    index = filename.rfind(".")
    if index >= 0:
        index = index if has_dot else index + 1
        return filename[index:]
    return ""


def main():
    print(get_suffix("aaa.bbb", True))
    print(get_suffix("aaa.bbb", False))
    print(get_suffix("aaa.c.bbb", True))
    print(get_suffix("aaa.c.bbb", False))
    print(get_suffix("aaabbb", False))
    print("___", get_suffix())


if __name__ == "__main__":
    main()
