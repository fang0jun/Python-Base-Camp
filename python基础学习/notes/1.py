"""

ip地址无效化
1，使用input获取用户输入
2，判断用户输入是否包含 .

"""
adress = "111.222.333"
print(adress.replace(".", "[.]"))


=================================================

"""

判断某一个值是否是 数组中某两数之和，如果是请返回他们的值和下标

"""
def twoSum(nums, target):
    pass

def high():
    pass





=================================================
"""

给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有?X?张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回?true。

X是最大相等数的数字个数

示例 1：
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：
输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
示例 3：
输入：[1]
输出：false
解释：没有满足要求的分组。
示例 4：

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]
示例 5：

输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]

提示：

1 <= deck.length <= 10000
0 <= deck[i] <?10000

"""
# 找出X --- 若X为奇数 若X为偶数
# 分组 --- 若分出的组数 != len(list) / X


class Deck(object):
    def partition(self,list, size):
        return [list[i:i + size] for i in range(0, len(list), size)]


    def find_X(self, decks):
        X_list = 0
        for deck in decks:
            X = 0
            for i in range(len(decks) - 1):
                if deck == decks[i]:
                    X = X + 1
                    X_list = max(X_list, X)
        # return X_list
        if X_list % 2 == 0:
            if len(decks) % 2 != 0:
                return False
            else:
                decks.sort()

                # list = [decks[i:i + X_list] for i in range(len(decks) // X_list)]
                list = [decks[i:i + X_list] for i in range(0, len(decks), X_list)]
                print(list)

        if X_list % 2 != 0:

            if len(decks) % 2 == 0:
                return False
            else:
                print("right")



first = Deck()
print(first.find_X([1,2,3,1,2,3,1,2,3,1,2,3]))

class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        N = len(deck)
        for X in xrange(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False

deckk = Solution()
deckk.hasGroupsSizeX([1,2,3,1,2,3,1,2,3,1,2,3])

=================================================

 def shitou(S, J):
    return len([i for i in S if i in J])


print(shitou(["f", "i","s" ,"h"], ["h","i","s","h"]))
