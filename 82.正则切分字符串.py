import re

s = "info:xiaozhang 33 shandong"
res = re.split(r":| ", s)  # | 表示或，根据冒号后 空格切分
print(res)
