"""
fn("one", 1) 直接将键值对传给字典
fn("two", 2) 因为字大点在内存中是可变数据类型，所以指向同一个地址，传了新的参数后，相当于给字典增加键值对
fn("three", 3, {}) 因为传了一个新字典，多以不再是原先某人参数的字典
"""


def func(k, v, dic={}):
    dic[k] = v
    print(dic)


if __name__ == '__main__':
    func("one", 1)
    func("two", 2)
    func("three", 3, {})
