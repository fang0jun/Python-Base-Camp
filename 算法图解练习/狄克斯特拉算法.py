"""

狄克斯特拉算法
针对有向无环正加权图，算出总权重最小路径
算法原理：
获得一个梯队到达另一个梯度各节点的权重
更新重新迈入第二梯队的最小权重 / 并以此为新的父节点，重复直到终点

"""


# 实现单向无环正加权图
graph = {}
graph["start"] = {"a": 6, "b": 2}
graph["b"] = {"a": 3, "end": 5}
graph["a"] = {"end": 1}
graph["end"] = {}

# 创建每一梯队的节点和其权重列表
infinity = float("inf")
costs = {"a": 6, "b": 2, "end": infinity}


# 每一梯队的父节点列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

# 记录已经处理过的节点


def find_lowest_cost_code(costs):
    """
    找到最小路径
    :param costs: 权重
    :return:
    """
    lowest_cost = infinity
    lowest_cost_code = None
    for node in costs:
        if node < lowest_cost:
            node = lowest_cost
            lowest_cost_code = costs.index(node)



def dekesitela():
    pass