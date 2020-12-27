"""

矩阵的python实现

"""

# 列表法  --- 广义表（列表中的列表）
m, n = map(int, input("请输入矩阵的行数和列数").split(" ", 1))
jlist = [[0]*n for i in range(m)]
# jlist = [[0]*m] * n
jlist[1][1] = 9
print(jlist)

# numpy法

import numpy as np

x,y = map(int,input().split())
a = np.ones((x+1,y+1))
