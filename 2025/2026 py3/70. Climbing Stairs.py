class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f = [0]*n
        f[0] = 1
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]
        return f[n-1]

节省空间
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return third
