"""

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

"""

class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 如果起始单元格有障碍物，则只需返回即可
        # 没有到达目的地的路径。
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # 填写第一列的值
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # 填写第一行的值
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # 从cell（1,1）开始填充值
        # 到达单元格[i] [j]的方式数量=单元格[i-1] [j] +单元格[i] [j-1]
        # i.e.从左到右.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value
        return obstacleGrid[m-1][n-1]
