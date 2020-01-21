class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        
        for i in range(len(s)):
            if s[i] != ']':
                stk.append(s[i])
                continue
            else:
                curr = ""
                while stk and stk[-1] != '[':
                    curr += stk.pop()
                stk.pop()
                # get string 
                curr = curr[::-1]
                # get number
                n = ""
                while stk and stk[-1] in "0123456789":
                    n += stk.pop()
                curr *= int(n[::-1])
                stk += list(curr)
        return "".join(stk)