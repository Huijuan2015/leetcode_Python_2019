class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        remove = set()
        res = ""
        for i, ch in enumerate(s):
            if ch not in "()":
                continue
            if ch == '(':
                stk.append(i)
            elif not stk:
                remove.add(i)
            else:
                stk.pop()
        while stk:
            remove.add(stk.pop())
        for i in range(len(s)):
            if i not in remove:
                res += s[i]
        return res