# raise自定义异常

def func():
    try:
        for i in range(5):
            if i > 2:
                raise Exception("数字大于2了")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    func()
