class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(op, val):
            if op == '+':
                stk.append(val)
            elif op == '-':
                stk.append(-val)
            elif op == '*':
                stk.append(stk.pop()*val)
            elif op == '/':
                l, r = stk.pop() , val
                if l * r < 0 and l % r != 0:
                    stk.append(l // r  + 1)
                else:
                    stk.append(l // r)
                 
        stk, val, op = [], 0, '+'
        # op: 当前数字前的符号
        for ch in s:
            # print stk
            if ch.isdigit():
                val = val*10 + int(ch)
            elif ch in "+-*/":
                helper(op, val)
                op, val = ch, 0
         
        helper(op, val)
        # print stk
        return sum(stk)