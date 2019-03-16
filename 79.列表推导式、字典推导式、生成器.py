import random

td_list = [i for i in range(9)]
print("列表推导式：", td_list, type(td_list))

ge_list = {i for i in range(9)}
print("生成器：", ge_list, type(ge_list))

dic = {k: random.randint(4, 9) for k in ["a", "b", "c", "d"]}
print("字典推导式：", dic, type(dic))
