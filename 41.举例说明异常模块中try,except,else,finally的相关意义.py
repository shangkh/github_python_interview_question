"""
try...except...else 没有捕获到异常，执行else语句
try...except...finally 不管是否捕获到异常，都执行finally语句
"""

try:
    num = 100
    print(num)
except NameError as e:
    print("产生错误了：%s" % e)
else:
    print("没有捕获到异常，则执行该语句")


try:
    num = 100
    print(num)
except NameError as e:
    print("产生错误了：%s" % e)
finally:
    print("不管是否捕获到异常，都执行该句")