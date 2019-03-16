import re

s = '<img data-original="https://rpic.douyudn.cn/appCovers/2016/11/13/1234.jpg ' \
    '"https://rpic.douyudn.cn/appCovers/2016/11/13/1234-seall.jpg style="display:inline">'

res = re.findall(r"https://.*?\.jpg", s)[0]
print(res)

res = re.search(r'https://.*?\.jpg', s)
print(res.group())
