class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        # length of leftover in stack
        stk = []
        for ch in S:
            if ch in "()":
                if ch == "(":
                    stk.append(ch)
                else:
                    if stk and stk[-1] == "(":
                        stk.pop()
                    else:
                        stk.append(ch)
                        
        return len(stk)