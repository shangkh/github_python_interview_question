"""
当以字符串格式化书写的方式的时候，如果用户输入的有;+SQL语句，后面的SQL语句会执行
"""

input_name = "wang"
sql = 'select * from demo where name="%s"' % input_name
print("正常SQL语句：", sql)

input_name = "wang;drop database demo"
sql = 'select * from demo where name="%s"' % input_name
print("SQL注入语句：", sql)

"""
解决方式：通过传参方式解决SQL注入
"""
params = [input_name]
count = cs1.execut('select * from demo where name=%s', params)