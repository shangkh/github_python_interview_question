dic = {"name": "wang", "sex": "man", "city": "beijin"}
print(dic.items())
b = sorted(dic.items(), key=lambda x: x[0])
print("根据键排序：", b)
new_dic = {i[0]: i[1] for i in b}
print("字典推导式构造新字典：", new_dic)
