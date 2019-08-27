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