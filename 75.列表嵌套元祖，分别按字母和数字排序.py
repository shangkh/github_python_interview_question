my_list = [("wang", 19), ("li", 55), ("xia", 24), ("shang", 11)]

a = sorted(my_list, key=lambda x: x[1], reverse=True)  # 年龄从大到小
print(a)

a = sorted(my_list, key=lambda x: x[0])  # 姓名从小到大
print(a)
