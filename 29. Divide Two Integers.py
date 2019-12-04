class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return
        isNeg = 1
        if dividend<0:
            isNeg *= -1
            dividend = -dividend
        if divisor<0:
            isNeg *= -1
            divisor = -divisor
        times = 0
        
        while  divisor <= dividend:
            temp, i = divisor, 1
            while temp <= dividend:
                print temp, i, dividend
                dividend -= temp
                times += i
                # i <<= 1
                # temp <<= 1
                i *= 2
                temp *= 2
        times *= isNeg
        return min(max(-2147483648, times), 2147483647)
                
       