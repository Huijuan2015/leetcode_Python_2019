class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # O(log n)

        def fast_pow(x, n):
            if n == 0:
                return 1.0
            half = fast_pow(x, n//2)
            if n%2 == 0:
                return half * half
            else:
                return half * half * x
        # n 是负数时，要转换为 x = 1 / x, n = -n；
        if n < 0:
            x = 1/x
            n = -n
        return fast_pow(x, n)