无空间做法

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        balance = 0
        res = 0
        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    res += 1
        return res + balance


栈
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        stk = []
        for ch in s:
            if ch == '(':
                stk.append(ch)
            elif ch == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(ch)
        return len(stk)