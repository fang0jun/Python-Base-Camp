"""

快速排序算法 --- 一个涉及递归的算法
quicksort的实质是

"""
import random

def quicksort(list_unsorted):
    if len(list_unsorted) < 2:
        return list_unsorted                    # ----------------分而治之第一步：设置基线条件
    else:                                       # ----------------分而治之第二步：
        num = random.randint(0, len(list_unsorted) - 1)
        mid = list_unsorted[num]
        list_left = [i for i in list_unsorted[1:] if i > mid]
        list_right = [i for i in list_unsorted[1:] if i <= mid]
        return quicksort(list_left) + [mid] + quicksort(list_right)


print(quicksort([1,2,2,12,123,121,24124,123]))
# 错误写法：len(list) == 1 （返回TypeError）/ 正确解法：len(list) < 2  ????????
# 写法一把空序列排除到else中，故检索不到空序列的第一个值！



# def oujimide(height, weight):
#     n = 0
#     m = 0
#     if weight % height == 0:
#         return height
#     else:
#         n = height // weight
#         m = height - (weight * n)
#         height = weight
#         weight = m
#
#
# result = oujimide(1680, 640)
# print(result)