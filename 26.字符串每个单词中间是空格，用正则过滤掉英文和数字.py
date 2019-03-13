# 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"

import re

# 方法一：
a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)
res = re.findall('\d+|[a-zA-Z]+', a)  # | 连接多个匹配方式

for i in res:
    if i in list:
        list.remove(i)
new_str = " ".join(list)

print(res)
print(new_str)

print(('----------------------------------------------'))

# 方法二：
a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)

res = re.findall('[\u4e00-\u9fa5]+', a)
new_str = " ".join(res)
print(res)
print(new_str)
