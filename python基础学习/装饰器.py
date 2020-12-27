"""

装饰器
返回的还是函数，但是可以在运行中修改函数

"""


def log(func):
    def first(*args, **kw):
        print("it call %s" % func.__name__)
        return func(*args, **kw)
    return first


@log
def now():
    print("2019-09-24")

now = log(now)
print(now)