"""

函数的参数类型：
 1，必选参数 2，默认参数 3，可变参数 4，命名(限定)关键词参数 5，关键词参数


"""


def f1(a, b, *args, **kw):
    print(a, b, args, kw)

f1(1, 2, 12, 35, 12, 65, x=2, y ="3")


def f2(a, b, *, right1, right2, **kw):
    pass


def f3(a, b, *args, city, hobby, **kws):
    print(a, b, args, "city:", city, "hobby:", hobby, kws)

# 使用命令关键字时调用参数必须有key
# 推而广之：即所有的关键字参数都需要key
f3(1, 2, 3, 42, city ="beijing", hobby = "badmindon", k = "kfc", l = "lol")
# 另一种方式输入参数来调用函数
# list1 = [1,12,3,4,5,7]
# list2 = {"first": 1, "second": 2, "third": 3, "fourth":4}
tuple = (1,12,3,4,5,7)
dict = {"city": "beijing", 'hobby': "badmindon", "first": 1, "second": 2, "third": 3, "fourth":4}
f3(*tuple, **dict)


=========================================================
"""

匿名函数
对与简单函数进行的简单构建

lambda 参数：函数式  == f（x） = x+2...

"""
list1 = map(lambda x: x * x, [1,2,3,4,5,6,7,8,9,10])
print(list(list1))
list2 = map(lambda x: x + 2 , [1,2,3,4,5])
# r = list(list2)
# print(r)
r = next(list2)
r1 =next(list2)
print(r1)


list_4 = [1,2,3,4,5,6,7,8,9,0,12]
list_3 = [i for i in list_4 if i%2 == 0]
list_10 = list(filter(lambda x:x%2 == 0, range(1, 20)))
print(list_10)


==================================================
"""

1,字符串与字符串之间/数字与数字之间（不同类型没关系布尔值为1或0）分别可以进行操作
  不可字符串与数字进行操作！若想得进行；类型转换函数

2，什么是函数：
    已经封装好的代码，可以直接调用

3，记录输入
字符串变量 = input(“提示内容”)
注意：返回的都是字符串变量

4，类型转换函数
int()
float()
str()
set()---转换为数列

5，调试器与控制台的使用
打点 - 调试 - F8

6，变量的格式化输出
带格式化操作符%号的字符串叫做格式化操作符
  %s %d %f  ("" % 变量1)
            ("" % (变量1， 变量2))
  % x d 小数点前有x位（原数不到x位则0占位补全，超过x位则失效）
  % y f 小数点后保留y位

7，变量的命名
关键字和标识符
标识符 --- 变量名和函数名（需要见名知义）
关键字 --- 内部已经提前使用的变量名
命名法 ：驼峰命名法 （大驼峰 小驼峰）   新单词首字母大写


"""

# import keyword

# print(keyword.kwlist)



# ---输入与转换
price= float(input("输入单价"))
weight = float(input("输入重量"))
# price = float(price_str)
# weight = float(weight_str)

money = price * weight
print("%12f  ,%.02f  ,%0.2f" % (money,money,money))

========================================================
"""

if相关


"""

import random

num = {}
num[1] = "石头"
num[2] = "剪刀"
num[3] = "布"

def SJB():
    player = input("剪刀石头布")
    i = random.randint(1,3)
    computer = num[i]


    if computer == "石头":
        print("对方出了---[%s]" % computer)
        if player == "石头":
            print("平局")
        elif player == "剪刀":
            print("lose")
        elif player == "布":
            print("win")
    elif computer == "剪刀":
        print("对方出了---[%s]" % computer)
        if player == "石头":
            print("win")
        elif player == "剪刀":
            print("平局")
        elif player == "布":
            print("lose")
    else:
        print("对方出了---[%s]" % computer)
        if player == "石头":
            print("lose")
        elif player == "剪刀":
            print("win")
        elif player == "布":
            print("平局")

SJB()
==================================================
"""
不可变对象汇总：字符串，整数，元组
可变对象：列表

有关列表

列表的常用方法：
增 append("str")  insert(index, "str") extend([list])
删 del list[index]/ del(list[index])   remove[value]  pop[index]
改 list[index] = new_value
排 sort() sort(reverse = True) reverse()
查 len(list)   --- 一 获得的长度为 n(最后一个索引值) + 1
                   二 且从0开始计数！
   count(value)



元组的常用方法：
查 count() len()

元组与列表之间的转换：  可且仅可在元组与列表之间转换
list（tuple）
tuple（list）

有关集合 --- 不存在重复元素
set(list) = {} 要通过集合来输入数据
可进行交集并集补集的操作  &交 | 并


有关字典
字典的常用方法：
增 dic[key] = value key原本存在  dic[key] = setdefault(key, value) 不改可增  dic.update(new_dic)
改 dic[key] = value key原本不存在
删 del dic[key]/del(dic[key])   dic.pop[key]
查 len()---键值对的数量


有关字符串
字符串的常用方法
极多操作：
一类：is型  isspace(标识符也是空格字符) isalnum() isalpha() isdecimal() istitle()
二类：查找与替换  startswith("str") endswith("str")
        返回-1find/rfind/报错index/rindex("str", start = 0, end = len(str))
        replace(old_str, new_str, num = string.count(old_str))
三类：大小写转换 capitalize()/title()/upper()  lower()
四类：文本对齐 ljust(width)/rjust(width) center(width)
五类：去除空白字符 lstrip/rstrip/strip
六类：拆分与连接  partition(str)-前中后 rpartition(str)
                split(str="str", num = number) - 一str为分割符拆分，num+1个字符串
                唯一的合并 join(seq)


字符串的切片
区间都是左闭右开的
当步长为负时，字符串就当当成倒过来一样计数

公共
len() in / not in / + / *
"""
string = "hello,myfriend"
string1 = "123456789n"
print("|" + string.center(50) + "|")

str = string.join(string.partition("llo"))
print(str)

print(string[6:4:-1])

===================================================
"""


生成器
生成器你要把它看成有而不显的列表，有但是不说。一旦下一个数被next后，则生成器中就没有这个数了
区别：外形上 列表生成式的方括号改为圆括号 --- 生成式就变成了生成器
有循环时通过打印输出 ， 无循环时通过next(generator)一个个地返回下一个值（原理，遇到 genetator中的 yield 时就存档返回）
生成器的创建方法 ：1 生成式的for循环  2 调用函数 在其中使用yield next



迭代器
可用于迭代的数据类型叫做迭代器
生成器一定是迭代器，迭代器不一定是生成器

"""

from collections import Iterable
from collections import Iterator

print(isinstance(iter("abc"), Iterator))
=======================================================
"""

生成器二次复习   --- 生成器的作用并没有想象中的那么高深，它只不过是“暂停”功能，来实现一种空间的动态分配
生成器就像一个 “包着函数吐值” 的懒惰机器(惰性计算)
运行完都可以获得所有结果但是！它使得函数形成阶段性返值的功能(丧失一次性返值的功能)

生成器（generator）具有 ：一边运行其中保存的算法一边惰性计算的机制
                        因为不算完，所以它有了代表全体数的可能性 （迭代器不可能实现）
创建方法：当保存的算法较简单时---1，列表生成式改装
         当保存的算法较复杂时---2，通过函数改装   --- 形成阶段性返值的功能

打印方法：1, print(next())获得下一步的值
         2,通过循环print


"""
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
    n, a, b  = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b ,a + b
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

=====================================================
"""

装饰器
在代码动态运行中增加功能的方式， 叫做装饰器decorator


"""


# 装饰(函数)器
def log(func):
    def wraper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wraper()

@log
def now():
    print("2019-09-20")

now()
# @log
# def sum(l):
#     sum = 0
#     for i in l:
#         sum = sum + i
#
# print(log(sum([1,8,5,5,6,9])))
======================================================
"""

 遍历与列表生成式

遍历存在的意义---对序列中的每一个数据都进行一次操作
                想对列表里的列表元组字典进行操作调用各自的方法，也得用遍历提出来
                一，全体 二，提取

列表生成式
总结：对于一个列表来说，第一：需要获得元素(遍历和添加) 第二：每个元素以什么样的形式
    列表生成式默认内含append！来生成一个列表 ---for..in.. / if / append(形式)
    使用两循环获得双遍历，以获得全排列


"""

list = []
for i in range(1,11):
    if i % 2 == 0:
        list.append(str(i) + "*" + str(i))
print(list)

list_2 = [i * i for i in range(1,11) if i%2 == 0]
print(list_2)

#
list_3 =[m + n for m in "ABC" for n in "abc"]
del(list_3[0])
# del list_3[0]
print(list_3)

list_4 = [m*n for m in range(1,10) for n in range(1,10)]
print(list_4)

# 用列表生成式 将列表改造成字典的样式
dic = {"a":1, "b":2, "c":3, "d":5}
del(dic["a"])
del dic["b"]
print(dic)
print(dic)

#想要对列表中的字符串们进行操作 --- 遍历以提取
list_5 = ["Tom", "Peter", "Bob"]
print([l.lower() for l in list_5])

#当列表中不仅包含字符串还有其他数据类型时 ---
list_6 = ["Tom", 18, "man"]
# num = str(list_6[1])
# print(num)
# print([i.upper() for i in list_6])
print([str(i).upper() for i in list_6])
==================================================
"""

返回函数   --- 可形成闭包的结构，即：相关参数都保存在返回的函数中
当一个函数返回一个函数那就是闭包操作
闭包操作中函数的参数只会在返回函数时调变量为参数，而不会立即在函数中调用
（故在其中一定要留意使用后续变化的量），若要使用则新函数绑定当前值

不仅接收一个函数为参数，而且返回一个函数的高级函数

"""


# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# print(sum([1,2,3,4,5]))
# print(lazy_sum(1,2,3,4,5,6,7))

# # 错例示范：在闭包中错误使用改变的数据
# def count_error():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i * i
#         fs.append(f)
#
#     return fs
#
# f1, f2, f3= count_error()
# print(f1)
# print(f1())
# print(f2())
# print(f3())
#
# def count():
#     # 既然闭包只能返回一个最终值，那么我每一步都做一个闭包，每一个值都作为被返回的最终值
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
#
# f1, f2, f3 = count()
# print(f1())

"""

利用闭包返回一个计数器函数，每次调用它返回递增整数：

"""
import time

# def countdown():
#     def count_down(count):
#         def down():
#             return count
#         return down
#
#     for i in range():
#         count -= 1
#         print(count)
#
# ft = countdown()

def countdown():
    # !!!闭包中整数型变量无法传入其中
    # t = 1
    # def counter():
    #     t = t + 1

    # !!!闭包中可以将列表传入其中！
    s = [0]
    def counter():
        s[0] = s[0] + 1
        return s[0]
    return counter()

ft = countdown()
print(ft)


===================================================
"""

高阶函数
将函数作为参数导入，让函数的参数是一个函数
函数名 --- 是一个指向内置函数的向量 eg:abs

高阶函数之四 ---sorted()
赋予非数字迭代器进行排列的各种方式
--- 默认（for...in...）对序列中的各个元素 先进行key操作后进行默认(sort)排序  = sort()+map()
sorted(iterable, key = 函数) eg : 返回一个数去作比较/把所有str变为大写后
"""

def add(x, y, f):
    return f(x) + f(y)
print(add(-1,-2,abs))

#----------------------------------------------------------------------------
def _add_iter():
    """构造一个3开始的奇数序列 生成器"""
    n = 1
    while True:
        n = n + 2
        yield n


# def _not_divisible(n):
#     """构造并返回   选择出n的所有倍数"""
#     return lambda x: x % n > 0
#
# def primes():
#     """找出所有素数，奇数序列除去它们的倍数"""
#     yield 2
#     # 生成器的使用可以将不需要操作的数next给出去（变相的是一种优雅删除）
#     # 使用生成器是为了在while中使用next把 数字本身(位于第一位) 提出来,使之不在筛选列表内
#     it = _add_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible, it)
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break
#



#-------------------------------------------------------------------------
# def fnnn(x):
#     return x % 2 == 0
#
# def asd():
#     f = (i for i in range(1000))
#     while True:
#         n = next(f)
#         print(n)
#         if f:
#             break
# asd()
#
# # print(next(f))
# # print(next(f))
# # print(next(f))
# # print(list(f))

"""

假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：

"""
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def fnnnn(t):
    return t[0]


print(sorted(L, key= fnnnn))


def fN(t):
    return t.upper()
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=fN))


