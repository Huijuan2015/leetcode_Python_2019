Time/Space: log(n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.myPow(x,-n)
        half = self.myPow(x, n//2) #// 向下取整
        if n%2 == 0:
            return half * half
        else:
            return half * half * x

            https://leetcode.com/problems/powx-n/discuss/19544/5-different-choices-when-talk-with-interviewers


1.00001
123456 cant pass, TLE?
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 :
            return 1
        res = x*self.myPow(x, n-1) if n > 0 else 1.0/x*self.myPow(x, -n-1)
        return res