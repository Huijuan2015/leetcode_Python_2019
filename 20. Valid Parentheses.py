class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for ch in s:
            if ch in "({[":
                stk.append(ch)
            elif ch in ')}]':
                if not stk:
                    return False
                top = stk.pop()
                if (ch == ')' and top != '(') or (ch == '}' and top != '{') or (ch == ']' and top != '['):
                    return False
            else:
                return False
        return True if not stk else False