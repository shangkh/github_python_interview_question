my_list = [{"name": "wang", "age": 19}, {"name": "li", "age": 54},
           {"name": "zhang", "age": 17}, {"name": "xiong", "age": 23}]

a = sorted(my_list, key=lambda x: x["age"], reverse=True)  # 年龄从大到小
print(a)

a = sorted(my_list, key=lambda x: x["name"])  # 姓名从小到大
print(a)
