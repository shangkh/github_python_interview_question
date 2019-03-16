import re

labels = ["<html><h1>www.baidu.com</h1></html>", "<html><h1>www.baidu.com</h2></html>"]

for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*?</\2></\1>", label)
    if ret:
        print("符合条件的标签：", ret.group())
    else:
        print("不符合条件的标签：", label)
