n
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        if N == 2:
            return 1
        curr, prev1, prev2 = 0,1,1
        for i in range(3, N+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr

2^n
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

    
#         if N == 0:
#             return 0
#         if N == 1:
#             return 1
        
#         return self.fib(N-1) + self.fib(N-2)
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a+b
        return a
