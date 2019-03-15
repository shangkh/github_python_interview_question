"""
1.赋值不可变数据类型，不管copy还是deepcopy，都是同一个地址，
    当浅拷贝的值是不可变对象（数值，字符串，元祖）时和"="赋值的情况一样，
    对象的id的值与浅拷贝原来的值相同。
2.复制的值是可变对象（列表和字典）
    浅拷贝copy有两种情况：
        第一种情况：复制的对象中无复杂子对象，原来值的改变不会影响浅拷贝的值，
            同时浅拷贝的值改变也不会影响原来的值。原来值的id与浅拷贝的不同。
        第二种情况：复制的对象中有复杂的子对象（例如列表中有一个子元素是列表），
            改变原来的值中子对象的值，会影响浅拷贝的值
    深拷贝deepcopy：完全复制独立，包括内层列表和字典
"""
import copy

a = "你好"
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))

print("-"*20)
list = [1, 2, [3, 4]]
a = copy.copy(list)
b = copy.deepcopy(list)

# id都不相同
print(list, id(list))
print(a, id(a))
print(b, id(b))

print("-"*20)
# 简单子元素改变，都没有改变
list[0] = 10
print(list, id(list))
print(a, id(a))
print(b, id(b))

print("-"*20)
# 复杂子元素改变，浅拷贝随之改变，深拷贝没有改变
list[2][0] = 5
print(list, id(list))
print(a, id(a))
print(b, id(b))
