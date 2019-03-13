"""
log日志中，我们需要用时间戳记录error,warning等的发生时间，
请用datetime模块打印当前时间戳
"""

import datetime

a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) \
    + ' 星期：' \
    + str(datetime.datetime.now().isoweekday())
print(a)