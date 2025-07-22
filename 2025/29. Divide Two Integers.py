class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        a = abs(dividend)
        b = abs(divisor)
        res = 0

        while a >= b:
            temp = b
            multiple = 1

            while a >= (temp << 1):
                temp <<= 1 # 原地左移（等价于 temp = temp << 1）
                multiple <<= 1
            
            a -= temp
            res += multiple
        
        if (dividend > 0) == (divisor > 0):
            return res
        else:
            return -res
