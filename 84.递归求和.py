"""
递归完成1+2+3+4+5+6+7+8+9+10的和
"""


def get_sum(num):
    if num >= 1:
        res = num + get_sum(num - 1)
    else:
        res = 0

    return res


if __name__ == '__main__':
    res = get_sum(10)
    print(res)
