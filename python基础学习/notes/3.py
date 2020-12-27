==================================================
"""

二分查找

"""
def bin_find(item, list):
    up = len(list) - 1
    low = 0
    while low <= up:
        mid = (up + low) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            up = mid - 1
        else:
            low = mid + 1

    return None

print(bin_find(7,[1,3,4,5,7,9,12,23,45,54,67]))

====================================================
"""

后进先出的数据结构为栈 /（与之对应的是先进先出的队列）

一基线二叠栈三调用   一基二叠三调---一终二靠三调
在递归中需要考虑
1，何为终止的基线
2，如何让叠栈以靠近基线
3，调用时的逻辑

递归小目标：解决欧几里得算法
"""


def countdown(i):
    if i == 0:
        print(0)
    else:
        print(i)
        countdown(i-1)

countdown(5)

def number(i):
    if i == 1:
        return 1
    else:
        result = i * number(i - 1)
    return result
print(number(5))

def sum(arr):
    #基线找对了，但是终止，调用，靠近方法存在疑问
    if len(arr):
        return arr[0] + sum(arr[1:])
    else:
        return 0

print(sum([1,2,3,4,5,7,8]))
============================================
"""

动态规划算法
当一个复杂问题可以被分解为独立且离散的子问题时，使用动态规划求解，求取相似度问题和可分解子问题的优化指标问题
步骤：
1，动态规划需要一张网格 一，单元格的值是什么（待优化值）  二，如何将这个问题划分为子问题（单元格）三，坐标轴

"""

==============================================
"""

广度优先算法
针对边无权重的图（非加权图），只考虑其段数，算出段数最小的路径

"""
from collections import deque


# 实现 图
picture = {}
picture["you"] = ["bob", "alice", "claire"]
picture["bob"] = ["anuj", "peggy",]
picture["alice"] = ["prggy"]
picture["claire"] = ["thom", "jonny"]


picture["anuj"] = []
picture["penny"] = []
picture["jonny"] = []
picture["thom"] = []
picture["alice"] = []

def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_deque = deque()
    search_deque += picture[name]
    while search_deque:
        person_first = search_deque.popleft()
        #在此 person_first 作为一个值，进入条件判断
        if person_is_seller(person_first):
            print(person_first + " is a mongo seller!")
            return True
        #在此 person_first 只作为键，带来对应值
        else:
            search_deque += picture[person_first]
    return False

search("you")
==============================================
"""

快速排序   母子孙基准分

qiuck排序的实质其实就是   比较大小+交换位置

"""

#当参数为数组时，将数组单独进行操作
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <=pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([1,2,4,5,6,4,1,4,6,83,21,3,5,35]))
============================================
"""

狄克斯拉特算法
针对 有向无环正加权图，算出总权重最小的路径
算法原理   ：获得第一梯队各节点跨入下一梯队各节点的权重，
            然后更新迈入二梯队的最小权重并以第一梯队的某节点为新的父节点，直到终点
具体步骤：
1，找本梯队进入下一梯队最小权重的节点
2，进行邻居检查---若有前往下一梯队较之更短的路径，则更新开销
3,对同一梯队的节点重复，直至获得进入下一梯队的路径（更新父节点与权重值）
（本梯队各节点路径权重对比 + 更新）---重复

"""
#实现无环正加权图
graph = {}
graph["start"] = {}
graph['start']["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

#每一梯队的节点和其权重列表
infinity = float("inf") #正无穷大
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

#每一梯队的父节点列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

#记录已经处理过的节点
processed = []


def find_lowest_cost_node(costs):
    """找到最小路径

    :param costs: 权重
    :return:
    """
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        global processed
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def diKeSiTeLa(costs):
    """狄克斯特拉算法"""
    node = find_lowest_cost_node(costs)
    while costs is not None:
        cost = costs[node]
        neighbors = graph[node]   #邻居们是一个列表变量
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


diKeSiTeLa([costs])

================================================
"""

贪婪算法  --- 解决NP完全问题
当你每一步都采用了局部最优解时，你就能获得接近全局最优解的结果


"""
# #集合操作
# fruits = ["a", "b", "c"]
# vegetables = ["a","d", "e", "f"]
# fruit = set(fruits)
# vegetable = set(vegetables)
# print(vegetable-fruit)

states_neededs = ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
states_needed = set(states_neededs)
stations = {}
kones = ["id", "nv", "ut"]
ktwos = ["wa", "id", "mt"]
kthrees = ["or", "nv", "ca"]
kfours = ["nv", "ut"]
kfives = ["ca", "az"]
kone = set(kones)
ktwo = set(ktwos)
kthree = set(kthrees)
kfour = set(kfours)
kfive = set(kfives)
stations["kone"] = kone
stations["ktwo"] = ktwo
stations["kthree"] = kthree
stations["kfour"] = kfour
stations["kfive"] = kfive
final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()

    for station,states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_for_station):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
    del stations[best_station]
# print(final_stations)
print(final_stations)
==========================================
# """
#
# 选择排序
#
# """
#
# def findSmall(arr):
#     small = arr[0]
#     small_index = 0
#     for i in range(len(arr)):
#         if arr[i] < small:
#             small = arr[i]
#             small_index = i
#     return (small_index, small)
#
# def selectionSelect(arr):
#     newArr = []
#     for i in range(len(arr)):
#         small_index = findSmall(arr)[0]
#         newArr.append(arr.pop(small_index))
#     return newArr
#
# print(selectionSelect([1,34,5,6,7,43,8,5,4.78]))
def findSmall(arr):
    small = arr[0]
    small_index = 0
    for i in range(len(arr)):
        if arr[i] < small:
            small = arr[i]
            small_index = i
    return small_index

def seletion(arr):
    newArr = []
    for i in range(len(arr)):
        small_index = findSmall(arr)
        newArr.append(arr.pop(small_index))
    return newArr

print(seletion([123,4,5,756,85,38,22]))