"""
给列表对象发出排序消息直接在列表对象上进行排序
"""
import sys


def main():
    list1 = [x for x in range(1, 10)]
    print(list1)
    list1 = [x + y for x in "12345" for y in "abcdef"]
    print(list1)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    list1 = [x ** 2 for x in range(1, 1000)]
    # 查看对象占用内存的字节数
    print(sys.getsizeof(list1))
    print(list1)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    list1 = (x**2 for x in range(1,1000))
    print(sys.getsizeof(list1))
    print(list1)

    for var in list1:
        print(var)






if __name__ == "__main__":
    main()
