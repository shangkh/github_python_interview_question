"""
使用pop和del删除字典中的"name"字段，dic = {"name": "xiaowang", "age": 18}
"""

dic = {"name": "xiaowang", "age": 18}
dic.pop("name")
print(dic)

dic = {"name": "xiaowang", "age": 18}
del dic["name"]
print(dic)