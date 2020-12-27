"""
法一:
字典模拟哈希表 哈希求解法
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素

"""
import random

#二分查找法
def twocut(item, arr):
    high = len(arr) - 1
    low = 0
    while high >= low:
        mid = (high + low) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
#获得和为该值的两个数

def getnumbers(target, arr):

    while 1:
        number1 = random.randint(0, len(arr) - 1)
        number2 = random.randint(0, len(arr) - 1)
        if number1 != number2 and arr[number1] + arr[number2] == target:
            return [number1, number2]
            break



arr = [1,2,3,4,5,6,7,8,9]
nums = getnumbers(4,arr)
yi = nums[0]
er = nums[1]
print(nums, yi, er  )



# #方法一:字典模拟哈希表法
# class TwoSum():
#     def twoSum(nums, target):
#         hashmap = {}
#         #使用enumerate函数将一个可以遍历的数据对象(如列表,元组或字符串)组合成一个索引序列,同时列出它的数据和其数据下标.
#         for ind, num in enumerate(nums, start=1):
#             hashmap[num] = ind
#         for i, num in enumerate(nums, start=1):
#             j = hashmap.get(target - num)
#             if j is not None and i != j:
#                 return [i,j]


# #方法二:正常
# def twoSum(nums, target):
#     lens = len(nums)
#     j = -1
#     for i in range(lens):
#         if (target - nums[i]) in nums:
#             if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
#                 continue
#             else:
#                 j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2
#                 break
#     if j > 0:
#         return [i,j]
#     else:
#         return []
