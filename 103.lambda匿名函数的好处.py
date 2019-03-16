"""
精简代码，lambda省去了定义函数，map省去了写for循环的过程
"""

a = ["a", "", "b", "", "c", "", "d"]
res = list(map(lambda x: "填充值" if x == "" else x, a))
print(res)