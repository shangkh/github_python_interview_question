"""
zip() 函数在运算时，会以一个或多个序列（可迭代对象）作为参数，
返回一个元祖的列表。同时将这些序列中并排的元素配对。
zip() 参数可以接受任何类型的序列，同时也可以有两个以上的参数；
当传入的参数的长度不同时，zip能自动以最短序列长度为准进行截取，获取元祖。
"""

a = [1, 2]
b = [3, 4]
res = [i for i in zip(a, b)]
print(res)

a = (1, 2)
b = (3, 4)
res = [i for i in zip(a, b)]
print(res)

a = "ab"
b = "xyz"
res = [i for i in zip(a, b)]
print(res)
