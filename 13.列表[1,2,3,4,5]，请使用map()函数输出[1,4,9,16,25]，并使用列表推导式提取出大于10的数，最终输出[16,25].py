"""
列表[1,2,3,4,5]，
请使用map()函数输出[1,4,9,16,25]，
并使用列表推导式提取出大于10的数，
最终输出[16,25]
"""

my_list = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


res = map(func, my_list)
res = [i for i in res if i > 10]

print(res)
