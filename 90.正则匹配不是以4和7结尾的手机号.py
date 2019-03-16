import re

tels = ['13112341234', '15812344321', '10000', '18800001117']

for tel in tels:
    ret = re.match("1\d{9}[0-3,5-6,8-9]", tel)
    if ret:
        print("符合条件的号码：", ret.group())
    else:
        print("不符合条件的号码：", tel)
