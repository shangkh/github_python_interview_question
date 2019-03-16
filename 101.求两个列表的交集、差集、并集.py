a = [1,2,3,4]
b = [3,4,5,6]

# 交集
j_list1 = [i for i in a if i in b]  # 在a中的i，并且也在b中
j_list2 = list(set(a).intersection(set(b)))

print("交集：", j_list1)
print("交集：", j_list2)

# 并集
b_list = list(set(a).union(set(b)))
print("并集：", b_list)
# 差集
c_list1 = list(set(b).difference(set(a)))  # b中有而a中没有的
c_list2 = list(set(a).difference(set(b)))  # a中有而b中没有的
print("差集：",c_list1)
print("差集：",c_list2)