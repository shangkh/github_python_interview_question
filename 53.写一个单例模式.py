"""
因为创建对象时__new__方法执行，并且必须return返回实例化出来的对象cls.__instance是否存在，
不存在的话就创建对象，存在的话就返回该对象，来保证只有一个实例对象存在（单例），
答应id，值一样，说明对象同一个
"""


class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        """
        如果类属性__insrance的值为None.
        那么就创建一个对象，并且赋值为这个对象的引用，
        保证下次调用这个方法时，能够知道之前已经创建过对象了，
        这样就保证了只有一个对象
        """
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


if __name__ == '__main__':
    a = Singleton(18, "xiaohong")
    b = Singleton(19, "xiaoming")

    print("id(a): %s" % id(a))
    print("id(b): %s" % id(b))

    a.age = 20  # 给a指向的对象添加一个属性
    print("a.age=%s" % a.age)  # 获取a指向对象的age属性
    print("b.age=%s" % b.age)  # 获取b指向对象的age属性
