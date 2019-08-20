"""
使用列表
"""


def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ["hello"] * 5
    print(list2)
    # 计算列表长度(元素个数)
    print(len(list1))
    # 下标(索引)运算
    print(list1[1])
    print(list1[4])
    print(list1[-1])
    print(list1[-3])
    list1[3] = 100
    print(list1)
    # 添加元素
    list1.append(200)
    print(list1)
    list1.insert(1, 400)
    print(list1)
    list1 += [1000, 2000]
    print(list1)
    print(len(list1))
    # 删除元素
    list1.remove(1)
    print(list1)
    if 1234 in list1:
        list1.remove(1234)
    print(list1)
    del list1[0]
    print(list1)
    # 清空列表元素
    list1.clear()
    print(list1)


if __name__ == "__main__":
    main()
