"""

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:
输入: [1,2,3]
输出: 6
示例 2:
输入: [1,2,3,4]
输出: 24

注意:
	给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
	输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

"""

# r = 0 要在循环，才能重新找max
# def find_biggest(l):
#     l2 = []
#     product = 1
#     for _ in range(3):
#         for i in l:
#             r = 0
#             r = max(r, i)
#         index = l.index(r)
#         l2.append(l.pop(index))
#
# print(find_biggest([1,2,3,4,5,6,8,9,1,2,31,23,21]))

def find_biggest_product(nums):
    positive = 0
    product = 1
    nums.sort(reverse=True)
    for i in nums[:3]:
        if i > 0:
            positive += 1
    if positive == 0 or positive == 3:
        product = nums[0] * nums[1] * nums[2]
    elif positive == 1:
        product = nums[0] * nums[-1] * nums[-2]
    elif positive == 2:
        product = max(nums[0] * nums[1] * nums[-1], nums[0] * nums[-1] * nums[-2])

    return product
print(find_biggest_product([1,2, 3, 5]))


def maximumProduct(nums):
    # 最大三个数, 要么都是正数, 要么是两个负数+一个正数
    nums.sort()
    v1 = nums[-1] * nums[-2] * nums[-3]
    v2 = nums[0] * nums[1] * nums[-1]
    return max(v1, v2)

