"""

选择排序
根据一种属性每次筛选出一个特定值，通过遍历重复这种筛选


"""
# 遍历元素，再获得索引//遍历索引，再获得元素


def find_smallest(list_unsorted):
    smallest = list_unsorted[0]
    smallest_index = 0
    for i in list_unsorted:
        if i <= smallest:
            smallest = i
            smallest_index = list_unsorted.index(i)
        return smallest_index


def smallest_put(list_unsorted):
    new_list = []
    for i in range((len(list_unsorted) - 1)):
        # smallest = find_smallest(list_unsorted)[1]
        smallest_index = find_smallest(list_unsorted)
        new_list.append(list.pop(smallest_index))
    return new_list

print(smallest_put([12,3452,3,542525,3542,2342,234,234]))








# def smallestsort(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     #选择排序,把最小的筛选出来
#     for i in range(len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#         return smallest_index


