import os
# 提供了不少于与操作系统相关联的函数

# os.name()：判断现在正在使用的平台，widows返回'nt'；Linux返回'posix'。
# os.getcwd()：得到当前工作的目录。
# os.listdir()：指定所有目录下所有的文件和目录名。
# os.remove()：删除指定文件。
# os.rmdir()：删除指定目录。
# os.mkdir()：创建目录，只能建立一层。
# os.makedirs()：递归创建目录。
# os.path.isfile()：判断制定对象是否为文件。是返回True，否则False。
# os.path.isdir()：判断指定对象是否为目录。是True，否则False。
# os.path.exists()：检验指定的对象是否存在。是True，否则False。
# os.path.split()：返回路径的目录和文件名。
# os.getcwd()：获得当前工作的目录。
# os.system()：执行shell命令。
# os.chdir()：改变目录到指定目录。
# os.path.getsize()：获得文件的大小，如果为目录，返回0。
# os.path.abspath()：获得绝对路径。
# os.path.join(path, name)：连接目录和文件名。
# os.path.basename(path)：返回文件名。
# os.path.dirname(path)：返回文件路径。


import sys
# 通常用于命令行参数

# sys.stdin
# sys.argv[i]：获取到执行文件时，对应的参数信息


import re
# 正则匹配

# result=re.match(正则表达式，要匹配的字符串)：从第一个字符向后依次进行正则匹配操作，匹配出对应的数据信息。
# result.group()：如果上一步匹配到数据的话，可以使用group方法来提取数据。
# result=re.search(正则表达式，要匹配的字符串)：从匹配到的第一个字符向后依次进行匹配操作。
# result==None：判断获取的书数据是否为空。
# re.search(r'\d+','my hight 177 cm').group()：匹配出指定字符串中符合正则表达式的第一条数据（只能匹配一个）。
# re.findall(r'\d+','my hight 177 cm my weight 100 kg')：配匹配出指定字符串中所有符合正则表达式的有效数据，并以列表的形式进行返回。
# re.sub(r'\d+','100','my high 177 cm')：将匹配到的数据进行替换，参数：对应的正则表达式，要替换的数据，匹配出来的数据；

import math
# 数学运算，为浮点运算提供了对底层 C 函数库的访问


import datetime
# 为日期和时间处理同时提供了简单和复杂的方法。
# 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
# 该模块还支持时区处理


import zlib
# 直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile