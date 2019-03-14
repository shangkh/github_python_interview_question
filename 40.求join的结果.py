"""
x = "abc", y = "def", z = ["d", "e", "f"],分别求出x.join(y)和x.join(z)返回的结果

join()括号里面的是可迭代对象，x插入可迭代队形中间，形成字符串，结果一致
"""

x = "abc"
y = "def"
z = ["d", "e", "f"]

a = x.join(y)
print(a)

b = x.join(z)
print(b)