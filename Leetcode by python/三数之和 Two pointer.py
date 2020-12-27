"""

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
# 使用三浮标指针，时间复杂度太大，解法失败(完成度90%)
class Solution(object):
    def sum_of_three(self, nums):
        l = []
        for i in range(len(nums)):
            # 边界问题的出错 + 1
            for j in range(len(nums)):
                # 使用递增获得指针j的值
                # j = i + 1

                # x = -(nums[i] + nums[j])
                # if x in nums and nums.index(x) != i and nums.index(x) != j:
                if j != i:
                    for k in range(len(nums)):
                        if nums[k] != nums[k - 1]:
                            s = nums[k] + nums[i] + nums[j]
                            if s == 0 and k != i and k != j:
                                l2 = sorted([nums[k], nums[i], nums[j]])
                                if l2 not in l:
                                    l.append(l2)

        return l

# 解法二 使用双指针，通过条件判断来防止重复

class Solution_2:
    def threeSum(self, nums):
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break  # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res