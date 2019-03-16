my_list = [["wang", 19], ["shang", 34], ["zhang", 23], ["liu", 23], ["xiao", 23]]

a = sorted(my_list, key=lambda x: (x[1], x[0]))  # 年龄相同添加参数，按字母排序
print(a)

a = sorted(my_list, key=lambda x: x[0])
print(a)
