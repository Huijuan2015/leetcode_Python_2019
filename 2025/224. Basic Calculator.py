class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        res = 0
        num = 0
        sign = 1

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                res += sign * num
                num = 0
                sign  = 1
            elif char == '-':
                res += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stk.append(res)
                stk.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += sign * num
                num = 0
                sign = stk.pop()
                prev_res = stk.pop()
                res = prev_res + sign * res
            
        res += sign * num
        return res