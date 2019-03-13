# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"

s = "ajldjlajfdljfddd"

s = set(s)
print(s)

s = list(s)
print(s)

# s.sort()
s.sort(reverse=False)  # False和空都是从小到大排序
# s.sort(reverse=True)  # True是从大到小排序
print(s)

res = "".join(s)
print(res)