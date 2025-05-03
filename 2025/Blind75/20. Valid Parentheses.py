class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # can define
        # pairs = {
        #     ')': '(',
        #     '}': '{',
        #     ']': '['
        # }
        stk = []
        for ch in s:
            if ch in "({[":
                stk.append(ch)
            elif ch in ")}]":
                if not stk:
                    return False
                top = stk.pop()
                if (ch == ')' and top != '(') or (ch == '}' and top != '{') or (ch == ']' and top != '['):
                    return False
            else:
                return False
        return True if not stk else False
                    

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) <= 1:
            return False
        stk = []
        i = 0

        while i < len(s):
            if s[i] in "({[":
                stk.append(s[i])
            elif s[i] in ")}]":
                if not stk:
                    return False
                else:
                    top = stk.pop()
                    if (s[i] == ')' and top != '(') or (s[i] == '}' and top != '{') or (s[i] == ']' and top != '['):
                        return False
            i += 1
        return True if not stk else False
                