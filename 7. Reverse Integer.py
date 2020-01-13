class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        carry = 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        while x:
            carry += x%10
            ans  = ans*10+carry%10
            carry = carry // 10
            x = x // 10
            if ans >= 2**31-1:
                return 0
        ans *= sign
        return ans