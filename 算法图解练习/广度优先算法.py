"""

广度优先算法   ---   广度（大）优先（一梯队）算法
也是一种查找方法，用于回答。能不能/怎样能（更快）找到

键值转换！ / 队列使用（+=/popleft）
1，创图  --- 广度
2，创队列  --- 优先
3，键值互换  --- 搜索

"""
from collections import deque

def person_is_slaer(name):
    # 返回一个条件
    return name[-1] == "m"

# 图的实现
picture = {}
picture["you"] = ["bob", "claire", "alice"]
picture["bob"] = ["peggy", "anuj"]
picture["claire"] = ["thom", "jonny"]
picture["alice"] = ["peggy"]
picture["anuj"] = []
picture["peggy"] = []
picture["jonny"] = []
picture["thom"] = []


def guangdu():
    search_deque = deque()
    search_deque += picture["you"]
    while search_deque:
        person = search_deque.popleft()
        if person_is_slaer(person):
            print(person + ",ok!")
            return
        else:
            search_deque += picture[person]
    return

guangdu()


#     search_deque = deque()
#     search_deque += picture["you"]
#     searched = []
#     while search_deque:
#         person_first = search_deque.popleft()
#         if person_first not in searched:
#             if person_is_saler(person_first):
#                 print(person_first + " is a mango seller!")
#             else:
#                 search_deque += picture[person_first]
#                 searched.append(person_first)
#     return False
#
# spanPrefer("tom")