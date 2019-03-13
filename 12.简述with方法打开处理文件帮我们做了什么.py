# f = open("file_name", 'wb')
# try:
#     f.write("Hello World")
# except:
#     pass
# finally:
#     f.close()


"""
打开文件在进行读写的时候可能会出现一些异常状态，
如果按照常规的f.open写法，我们需要try,except,finally，做异常判断，
并且文件最终不管遇到什么情况，
都要执行finally f.close()关闭文件，
with方法帮我们实现了finally中的f.close()
（当然还有其他自定义功能，有兴趣的可以研究一下with方法的源码）
"""