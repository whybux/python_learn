"""
使用元组
"""


def main():
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # t[0] = '王大锤'
    t = ('王大锤', 20, True, '云南昆明')
    print(t)

    # 将元组转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple =tuple(fruits_list)
    print(fruits_tuple)

if __name__ == "__main__":
    main()
