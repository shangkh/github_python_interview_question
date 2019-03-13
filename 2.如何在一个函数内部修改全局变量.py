a = 5

def func():
    global a
    a = 4


if __name__ == '__main__':
    func()
    print(a)