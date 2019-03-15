a = zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))
a0 = dict(a)
a1 = range(10)
a2 = [i for i in a1 if i in a0]
a3 = [a0[i] for i in a0]

print("a0:", a0)
print(list(zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))))
print(a2)
print(a3)

# dicr()创建字典新方法
s = dict([["name", "wang"], ["age", 18]])  # 列表
print(s)

s = dict([("name", "wang"), ("age", 18)])  # 元祖
print(s)
