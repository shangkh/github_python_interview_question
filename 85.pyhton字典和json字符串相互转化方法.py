import json

dic = {"name": "wang", "age": "18"}

res = json.dumps(dic)
print(res, type(res))

ret = json.loads(res)
print(ret, type(ret))
