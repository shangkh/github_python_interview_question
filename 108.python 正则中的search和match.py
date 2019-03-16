import re

s = "小红年龄18岁，工资10000"
res = re.search(r"\d+", s).group()  # search匹配到第一个数据
print("search的结果：", res)

res = re.findall(r"\d+", s)  # 满足正则，都匹配，不用加group()
print("findall的结果：", res)

res = re.match("小红", s).group()  # 匹配以"小明"开头的字符串
print("match的结果：", res)

res = re.match(r"\d+", s)
print("match不加group匹配不到：", res)  # 不加group匹配不到

res = re.match("工资", s).group()  # 工资不是字符串的开头匹配不到，报错
print("match的结果：", res)
