"""

返回函数
高阶函数的一种，将函数作为参数导入，并返回一个函数。同时形成一个威力巨大的闭包结构

"""


def calc_sum(*args):
    """求和函数"""
    ax = 0
    for n in args:
        x = ax + n
        return ax

print(calc_sum([1,2,4,5,7,8,]))


def lazy_sum():
    pass
