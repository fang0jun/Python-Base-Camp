"""

高阶函数
原理：把函数的参数设置为函数
目标：为了将运算规则抽象

高阶函数之一 --- map
map(f, iterable) ---> iterator
map 将迭代器中的各个元素 ,分别地 进行函数运算，并返回生成器
输入一个函数和迭代器  返回一个生成器（记得接收）

高阶函数之二 --- reduce
reduce(f, [list]) ---> value
reduce 将列表中的各个元素作为自变量，以特定的方式（f(f(x1,x2),x3)）进行f函数运算

高阶函数之三 --- filter（筛选）
filter(f, iterable) ---> iterater
filter将迭代器中的各个元素，分别地 进行函数 “判断 ” ，并返回生成器

高阶函数之四 --- sortsd(排序)
sorted(iterable, key = fn )
将迭代器中的每一个元素（for...in...），执行 fn（不改变原来的序列函数!!） //以执行操作后的隐藏序列进行排序，以原元素显示

#函数的返回值可以是 一个值 或者 一个操作方法 或者一个判断条件
"""



def f(x):
    return x * x

r = map(f,[1,2,3,4,6,7])  # ---r 是一个惰性序列iterator
print(list(r))           # ---故将r转化为list，使得整个序列全部运算出来，并返回到list上
s = map(str,[1,2,3,4,6,7])
print(list(s))
#
from functools import reduce

def fn(x,y):
    return x * 10 + y
def get_int(str):
    list_int = []

    # （字典-字符串：int） 通过字典把字符串中的字符转化为int
    dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    for i in str:
        list_int.append(dic[i])
    return list_int

print(reduce(fn,get_int("12452")))


#
def fn1(name):
    return name.title()
list1 = ['adam', 'LISA', 'barT']
name = map(fn1, ['adam', 'LISA', 'barT'])
print(list(name))


#
names = ['adam', 'LISA', 'barT']
list_name = []
for name in names:
    list_name.append(name.title())

print(list_name)


#
list_name1 = [name.title() for name in names]
print(list_name1)


#筛选复数
def is_old(n):
    return n % 2 == 0

r = filter(is_old,[1,2,3,4,5,6,7,8,9,10])
print(list(r))

#筛选素数


#筛选回文数
def huiWen(num):

    return num.reverse() == num
def dic_int(num):
    # dic = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    list_3 = [str(n) for n in num]
    return list_3

itertator = filter(huiWen,dic_int([123321,1222344,236632,1247565432,12332098765]))
print(list(itertator))