class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        open = 0
        res = ""
        for ch in S:
            if ch == '(':
                if open > 0:
                    res+=ch
                open += 1
            if ch == ')':
                if open > 1:
                    res+=ch
                open -= 1
        return res
                