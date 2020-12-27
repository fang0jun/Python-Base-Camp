"""

使用二分查找算法   输入一个有序数组, 返回指定元素的位置
1，将整个有序列表标好长度
2，每次都检查中间的元素
3，判断所猜中间元素与指定数字的大小---若猜少改底，若猜多则改顶

中心思想：
二分查找是一种排除查找法，每次必能排除1/2
迭代器先通过规定长度(目的是为了获得索引)，以取中间值二分为一排除

tips: 一种新颖的获得列表索引的方法---先标好列表长度
"""


def twoSort(list_sorted, item):
    low = 0
    high = len(list_sorted)-1
    # 为什么少了一个 = 就无法运行？？？？
    # 解：最后一步前low/high会改变自己“1”，此时low = high
    while low <= high:
        mid = (high + low) // 2
        guess = list_sorted[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return

print(twoSort([2,3,4,5,6,7,8,9],4))


