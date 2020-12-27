"""

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

"""
# 选择排序 1，基线条件 2，叠栈 3，调用规律


def sort(L):
    if len(L) < 2:
        return L
    else:
        mid = L[0]
        list_left = [i for i in L if i < mid]
        list_right = [i for i in L if i > mid]
        list = sort(list_left) + [mid] + sort(list_right)
        return list


LIST = [1,242,242,241,42,5,5,5,26,457,458,3597,6,765,4]
LIST_1 =[1,23,23,23,23]
print(sort(LIST))