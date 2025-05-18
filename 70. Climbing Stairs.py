class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
#         if n <= 2:
#             return n
#         res = [None] * n
#         res[0] = 1
#         res[1] = 2
#         for i in range(2, n):
#             res[i] = res[i-1] + res[i-2]
        
#         return res[n-1]
        # 0~n-1
        # 1, 2, 3...
        if n == 1: return 1
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a+b
        return b



//memoization
class Solution(object):s
    d = {}
    d[1] = 1
    d[2] = 2
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        # d = [_ for _ in range(n+1)]
        # d[:3] = [0,1,2]
        
        # print d
#         for i in range(3, n+1):
            
#             d[i] = d[i-1] + d[i-2]
#         return d[n]
        
        if n in self.d:
            return self.d[n]
        self.d[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.d[n]


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        res = [_ for _ in range(n+1)]
        res[:3] = 0, 1, 2
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]