# 一个元素替换成多个元素，可将原列表切片替换
l = list(range(10))

l[0] = [1234,222,111]
l[-1:-2] = [1231,124,222]
l[3 : 3] = [111,222,333]  # 直接插入不替换

print(l)

# 列表解包
elems = [1,2,3,4]
a, b, c, d = elems
print(a, b, c, d)

# 列表拉平
list_of_lists = [[1],[2],[3],[4,5,6,7]]
l = sum(list_of_lists, [])

# 列表和生成器的区别
li = (i for i in list(range(10)))
print(next(li))

# first_step : create a generator
list_ex = [1,2,3,4,5,6,7,8,9]
list_1 = [i for i in list_ex]
generator_1 = (i for i in list_ex)
print(list_1)
# 以下代码的返回结果为：StopIteration
# print(list(generator_1))
# print(next(generator_1))

# 以下代码的返回结果为：
# 1
# [2, 3, 4, 5, 6, 7, 8, 9]
# 可得出next（）--- have the ability to get and pop a value!
print(next(generator_1))
print(list(generator_1))

# second_step 斐波那契数列


def fib(max):
    """正常步骤获得斐波那契数列"""
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # 注意多值赋值语句  ==> t[0],t[1] = (b, a+b) 以元组保护数据！
        a, b = b, a + b   # 此处的a+b 值不会受到前方a，b互换的影响！
        n += 1
    return

def fib_2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n += 1
    return

generator_2 = fib_2(5)
# print(next(fib_2(5)))
print(list(generator_2))

# 此节练习题
def sanjiao():
    """使用生成器制作出杨辉三角算法"""
    # n = 1
    # L = [0] + [1] + [0]
    # while n < low:
    #     yield L
    #     n += 1
    #     L = [L[i] + L[i + 1] for i in range(len(L))]

    # L = [1]
    # while 1:
    #     yield [0] + L + [0]
    # 错因分析，[0]并不随着生成器吐出，应该吐后再加上
    #     L = [L[i] + L[i + 1] for i in range(len(L) - 1)]

    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]


generator_YangHuiTriangle = sanjiao()
for i in range(100):
    print(str(next(generator_YangHuiTriangle)).center(150))

# reduce函数的使用
from functools import reduce

def sum_of_produt(l):
    r = reduce(lambda x, y: 10*x + y, l)
    return r

print(sum_of_produt([1,2,3]))