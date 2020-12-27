"""

数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。

你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：

将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
将第 i 个筹码向左或者右移动 1 个单位，代价为 1。


最开始的时候，同一位置上也可能放着两个或者更多的筹码。

返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。

"""
import math
# [2,2,2,3,4]
def total(chips):
    result = []
    total = 0
    for i in range(len(chips) - 1):
        if i == 0 or chips[i - 1] != chips[i]:
            for num in chips:
                if num != chips[i]:
                    total = total + (abs(num - chips[i]) % 2)
            result.append(total)   # 改造成列表生成式
            total = 0
    if not result:
        result.append(0)
    return min(result)
print(total([2,2,2,3,3]))

# 运用了玩转数字的  位运算!(奇偶性问题中可以使用)
def minCostToMoveChips(chips):
    odds = sum(i & 1 for i in chips)
    odds_1 = [i & 1 for i in chips]
    print(odds_1, odds)
    return min(odds, len(chips) - odds)
print(minCostToMoveChips([1, 33, 2, 2, 2, 3, 3, 7, 19]))

