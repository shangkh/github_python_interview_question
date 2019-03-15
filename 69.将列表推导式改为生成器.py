"""
生成器是特殊的迭代器：
    1.列表推导式的[]改为（）即可变成生成器
    2.函数在返回值的时候出现yield就变成生成器，而不是函数了
"""
a = [i for i in range(3)]
print(type(a))

a = (i for i in range(3))
print(type(a))