"""

行走的机器人算法演示
转向问题 1，方向与方向控制器  --- xy正负位移量列表表示方向 索引为列表表示方向选择
        2，转向后的数值表示  --- 奇数次转向只改变x，偶数次转向只改变y ， 使用数对进行选择（确定了两个列表的上下对应关系）
        3，方向的相关联问题 --- 转换为前后次异同问题(若与上一次相同则 / 不同则) 使用两个列表进行分别选择（确定了列表的左右对应关系）
        4，移动时的阻碍判断问题 --- 分解（遍历）步数     逐步移动 依次判断
        自己尝试：使用单列表通过不同的取索引方式也可以达到该效果 ————等同于使用两个列表
                  --- 但是不需要复杂的索引表达式 (di = (di +- 1) % 4 ---生成周期性列表的标准表达式)

"""
class Robit():
    def move(self, moves, stones):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        stonesSet = set(map(tuple, stones))
        ans = 0
        # 这一次左右与上一次左右相关联， 则转换为 --- 与上一次选择相同则继续使用该列表下一列的数，
        # 若与上一次选择不同则调用另一个列表的下一列对应数
        # 之所以选择双列表是为了转向时有两个选择
        for movess in moves:
            if movess == -2:
                # 3 0 1 2
                di = (di - 1) % 4
            elif movess == -1:
                # 1 2 3 0
                di = (di + 1) % 4
            else:
                for k in range(movess):
                    if (x + dx[di], y + dy[di]) not in stonesSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)
        return ans

list_1 = (1, 2, -2)
list_2 = [[2,3]]
robit = Robit()
print(robit.move(list_1, list_2))
