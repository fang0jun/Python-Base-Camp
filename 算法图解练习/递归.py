"""
递归感想：多多积累 基线条件和靠方案
递归案例
1,倒计时
2,数的阶乘
3,递归求和
"""
import time


def countdown(i):
    print(i)
    time.sleep(1)
    # 设定基线条件
    if i == 0:
        return
    elif i > 0:
        countdown(i - 1)


countdown(3)


# 计算阶乘的递归逻辑
def fact(i):
    # 阶乘的运算逻辑：3*2*1
    if i == 1:
        # 如果需要参加计算时，基线条件下的return值同样要加入最终运算！！
        # 当然如果不需要参加计算时，使用return
        # return / return 1 前者报错type类型（最后一栈返回了“None”）后者成功运行
        return 1
    elif i > 0:
        return i * fact(i - 1)
        # return fact_result
print(fact(5))
# 给定一个数组，求数组中所有元素的和


# 一种新颖的基线条件：切到数组为空
def findsum(list_sum):
    if len(list_sum) == 1:
        return list_sum[0]
    else:
        return list_sum[0] + findsum(list_sum[1:])

print(findsum([11,11,11]))
