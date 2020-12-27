"""

爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
先女后男 奇数项为女 偶数项为男

选出任一 x，满足 0 < x < N 且 N % x == 0 。 ---选出必N小的N 的倍数Q
用 N - x 替换黑板上的数字 N 。      ---使用N-X替换原有的X （N = N(Q - 1)/Q）

如果玩家无法执行这些操作，就会输掉游戏。  ---获得N 为 1者则胜利
只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
若奇数项为1，则True，否则则False）
"""
N = int(input())
count = 0
while True:
    # try:

    x = int(input("女生请输入"))
    N = N - x
    if N == 0:
        print("TRUE")
        break
    y = int(input("男生请输入"))

    N = N - x
    if N == 0:
        print("FALSE")
        break


