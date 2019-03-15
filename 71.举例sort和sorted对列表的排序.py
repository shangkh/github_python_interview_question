"""
举例sort和sorted对列表的排序,llist = [0, -1, 3, -10, 5, 9]

sort 与 sorted 区别：
    Python list内置sort()方法用来排序，
    也可以用python内置的全局sorted()方法来对可迭代的序列排序生成新的序列
        sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
            sort()不能对dict字典进行排序
        list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
            而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
            对dict字典排序默认会按照dict的key值进行排序，最后返回的结果是一个对key值排序好的list,
            注意：返回的list只有key的内容，没有value
"""
list = [0, -1, 3, -10, 5, 9]
new_list = list.sort(reverse=False)
print("sort在list的基础上修改，没有返回值：", list)
print(new_list)

list = [0, -1, 3, -10, 5, 9]

new_list = sorted(list, reverse=False)
print("sorted生成新的list，有返回值：", list)
print("返回值：", new_list)
