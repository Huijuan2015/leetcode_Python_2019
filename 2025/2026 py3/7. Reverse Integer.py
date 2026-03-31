class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        INT_MIN = -2**31
        INT_MAX = 2**31-1

        res, sign = 0, 1

        if x < 0:
            sign = -1
        x = abs(x)

        while x > 0:
            digit = x%10
            # if (res * 10 + digit) * sign > INT_MAX or (res * 10 + digit) * sign < INT_MIN:
            #     return 0
            # 这样写更好因为不用计算出这个巨大的数
            if res > (INT_MAX-digit) // 10:
                return 0
            res = res * 10 + digit
            x = x // 10
        return res * sign
