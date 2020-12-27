# 合并两个递增序列

# l1 = [1,3,6,48,91]
# l2 = [2,53,63]

class Solution_1(object):
    def together(self, l1, l2):
        l3 = sorted(l1+l2)
        return l3

class Solution_2(object):
    def together(self, l1, l2):
        k1, k2 = 0, 0
        l3 = []
        # if k2 == 1 and l1[k1] > l2[k2]:
        #     l1[k1:k1] = l2[k2]
        # if k2 == len(l2) - 1 and l1[len(l1) - 1] < l2[len(l2) - 1]:
        #     l1[len(l1) - 1: len(l1) - 1] = l2[len(l2) - 1]
        # else:
        while k1 < len(l1) - 1 and k2 < len(l2) - 1:
            if l1[k1] <= l2[k2]:
                l3.append(l1[k1])
                k1 += 1
                while l1[k1] == l1[k1 - 1]:
                    l3.append(l1[k1])
                    k1 += 1

            elif l1[k1] > l2[k2]:
                l3.append(l2[k2])
                k2 += 1
                while l2[k2] == l2[k2 - 1]:
                    l3.append(l2[k2])
                    k2 += 1

            else:
                l3.append(l1[k1]+l2[k2])
                k2 += 1
                k1 += 1
                while l2[k2] == l2[k2 - 1]:
                    k2 += 1
                    l3.append(l2[k2])
                while l1[k1] == l1[k1 - 1]:
                    k1 += 1
                    l3.append(l1[k1])

        if k1 >= len(l1) - 1:
            l3.append(l2[k2:])
        elif k2 >= len(l2) - 1:
            l3.append(l1[k1:])

        return l3
lll = Solution_2()
print(lll.together([2,53,63],[1,3,6,6,6,48,91]))



