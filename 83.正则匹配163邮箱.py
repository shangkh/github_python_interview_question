import re

email_list = ["xiaowang@163.com", "xiaoli@qq.com", "xiaozhang@gmail.com"]

for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$", email)
    if ret:
        print("%s 是符合的邮箱，匹配后的结果是：%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)
