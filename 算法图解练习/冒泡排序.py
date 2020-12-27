class Solution(object):
    def __init__(self,l):
        self.l = l

    def mp_sort(self):
        for i in range(len(self.l) - 1):   # 数组长度 - 1
            for j in range(len(self.l)-i-1): # 数组长度 - 轮数 -1
                if self.l[j] > self.l[j+1]:
                    self.l[j+1], self.l[j]= self.l[j], self.l[j+1]
                else:
                    pass
        print(self.l)

P = Solution([2,7,3,11,25,9,14,3])
P.mp_sort()

#[2, 3, 3, 7, 9, 11, 14, 25]
