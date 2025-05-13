class Solution(object):
    d = {}
    d[1] = 1
    d[2] = 2
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.d:
            return self.d[n]
        self.d[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.d[n]