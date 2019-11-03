import math
class Solution:
    
    def getFactorsFrom(self, n, frm):
        res = []
        for i in range(frm, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                res.append([i, n // i])
                for partial in self.getFactorsFrom(n // i, i):
                    res.append([i] + partial)
        return res
    
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.getFactorsFrom(n, 2)


class Solution(object):

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 1:
            return []
        res = []
        # ans = []
        # stack, x = [], 2
        # while True:
        #     if x > n / x:
        #         if not stack:
        #             return ans
        #         ans.append(stack + [n])
        #         x = stack.pop()
        #         n *= x
        #         x += 1
        #     elif n % x == 0:
        #         stack.append(x)
        #         n /= x
        #     else:
        #         x += 1
        # return ans

        i = 2
        while i * i <= n:
            if n%i == 0:
                q = n/i
                print i, q
                res.append([i, q])
                print res
                sub = self.getFactors(q)
                for r in sub:
                    # is used for checking and avoiding duplicates, 
                    #for example when n=24, only [2,2,2,3]should be recorded, not [2,3,2,2]
                    if r[0] >= i:
                        res.append([i] + r)
            i += 1
        return res
        
        
        