"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。
# 错误法一 ： 误认为相配对的括号， 序号一定是一个奇数一个偶数

"""

def ads(n):
    d = {")": "(", "}": "{", "]": "[", "[": "]", "{": "}", "(": ")"}
    return d[n]

# 给字符串排序的思考：1，转为数字/记数再转数(对于字符种类不多)
#                    2，模块operator中attrgetter和itemgetter方法:可将想要排列的特定字符与数字捆绑


def sort_1(j):
    d = {"(": "(", "[": "[", "{": "{",
         ")": "(", "]": "[", "}": "{"
         }
    return d[j]


# s = ")}{()"
# stack = map(sort_1, s)
# print(list(stack))


def sort_2(l):
    li = sorted(l, key=sort_1)
    return li


class Solution(object):
    def judge(self, s):
        d = {"(": 1, "[": 2, "{": 3,
             ")": -1, "]": -2, "}": -3
        }
        stack = []
        for i in s:
            if not stack or stack[-1][1] + d[i] != 0:
                stack.append([i, d[i]])
            elif stack[-1][1] + d[i] == 0:
                stack.pop()
        if not stack:
            return True
        else:
            return False


s = Solution()
print(s.judge("[(]"))

# # 错误法一 ： 误认为相配对的括号， 序号一定是一个奇数一个偶数
# class Solution():
#     def isValid(self, s):
#         s1 = s[::2]
#         s2 = s[1::2]
#         s11 = list(s1)
#         s22 = list(map(ads, s2))
#         s11.sort(key=sort)
#         s22.sort(key=sort)
#         # s22 = list(map(self.ads, s2))
#         if s11 == s22:
#             print("true")
#             return True
#         else:
#             print("false")
#             print(s11)
#             print(s22)
#             return
