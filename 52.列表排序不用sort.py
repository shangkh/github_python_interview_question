"""
list = [2, 3, 5, 4, 9, 6]，从小到大排序，不许用sort，输出[2, 3, 4, 5, 6, 9]
"""
list = [2, 3, 5, 4, 9, 6]
new_list = []


def get_min(list):
    # 获取列表的最小值
    a = min(list)
    # 删除列表中最小值
    list.remove(a)
    # 将最小值加入新列表
    new_list.append(a)
    # 保证最后列里面有值，递归调用获取最小值
    # 直到所有值获取完，并加入新列表返回
    if len(list) > 0:
        get_min(list)
    return new_list


if __name__ == '__main__':
    new_list = get_min(list)
    print(new_list)
