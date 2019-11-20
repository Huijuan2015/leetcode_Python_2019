class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str = str.strip()
        if len(str) == 0:
            return 0
        # print str
        sign = -1 if str[0] == '-' else 1
        if str[0] in ['+', '-']:
            str = str[1:]
        res = 0
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        for ch in str:
            if ch.isdigit():
                res = res*10 + ord(ch) - ord('0')
            else:
                break
        return max(MIN_INT, min(sign * res, MAX_INT))