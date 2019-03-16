dic = {"name": "wang", "sex": "man", "city": "beijin"}
foo = zip(dic.keys(), dic.values())  # 字典转列表嵌套元祖
foo = [i for i in foo]
print("字典转换为列表嵌套元祖：", foo)  # 字典嵌套元祖排序
b = sorted(foo, key=lambda x: x[0])
print("根据键排序：", b)
new_dict = {i[0]: i[1] for i in b}  # 排序完构造在新字典
print("字典推导式构造新字典：", new_dict)
