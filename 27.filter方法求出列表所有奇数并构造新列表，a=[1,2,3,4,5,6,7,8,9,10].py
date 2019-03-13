"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，
    返回由符合条件的元素组成的新列表。
    该函数接收两个参数，第一个为函数，第二个为序列，
    序列的每个元素作为参数传递给函数进行判断，
    然后返回True或False，
    最后将返回True的元素放到新列表
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(a):
    return a % 2 == 1

new_list = filter(func, a)
new_list = [i for i in new_list]
print(new_list)