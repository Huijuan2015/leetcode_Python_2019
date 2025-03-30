class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # solution 1：Compare entire string, 正反一致
        # if x < 0:
        #     return False
        # else:
        #     x = str(x)
        #     if x == x[::-1]:
        #         return True
        #     else:
        #         return False

        # Solution 2: 不转成string
        if x < 0:
            return False
        newNum = 0
        inputNum = x
        while x > 0:
            newNum = newNum * 10 + x % 10
            x //= 10
        return newNum == inputNum
