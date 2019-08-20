"""
字符串的使用
"""

def main():
    str = "hello world"
    # 通过len函数计算字符串的长度
    print(len(str))
    # 获得字符串首字母大写的拷贝
    print(str.capitalize())
    # 获得字符串变大写后的拷贝
    print(str.upper())
    # 从字符串中查找子串所在位置
    print(str.find("or"))
    print(str.find("shit"))
    # 与find类似但找不到子串时会引发异常
    print(str.index("or"))
    # print(str.index("shit"))
    # 检查字符串是否以指定的字符串开头
    print(str.startswith("He"))
    print(str.startswith("hell"))
    # 检查字符串是否以指定的字符串结尾
    print(str.endswith("ld"))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str.center(50, "*"))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str.rjust(50, "*"))
    str = "abc123456"
    # 从字符串中取出指定位置的字符(下标运算)
    print(str[2])
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str[2:5])
    print(str[2:])
    print(str[2::2])
    print(str[::2])
    print(str[::-1])
    print(str[-3:-1])
    # 检查字符串是否由数字构成
    print(str.isdigit())
    # 检查字符串是否以字母构成
    print(str.isalpha())
    # 检查字符串是否以数字和字母构成
    print(str.isalnum())
    str = "    123   "
    print(str)
    print(str.strip())


if __name__ == "__main__":
    main()
