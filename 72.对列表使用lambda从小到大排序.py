"""
key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较。
这个技术是快速的因为key指定的函数将准确地对每个元素调用。
"""

foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]

# 对key的思考过程
# b = lambda x: x
# print(b(foo))
# b = b(foo)
# b.sort(reverse=False)
# print(b)

# ---------------------------------------------

a = sorted(foo, key=lambda x: x)
print(a)
