"""
python中函数参数是引用传递（注意不是指传递）。
    对于不可变类型（数值型、字符串、元祖），因变量不能修改，多以运算不会影响变量自身；
    而对于可变类型（列表、字典）来说，函数体运算可能会更改传入的参数变量
"""


def func(a):
    a += a


a_int = 1
print(a_int)
func(a_int)
print(a_int)

a_list = [1, 2]
print(a_list)
func(a_list)
print(a_list)
