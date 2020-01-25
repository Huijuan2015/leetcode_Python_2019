class Solution(object):
    memo = {}
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.memo:
            return self.memo[s]
        for i in range(len(s)-1):
            if s[i:i+2] == "++":
                next = s[:i] + "--" + s[i+2:]
                if not self.canWin(next):  下一步输了
                    self.memo[s] = True  当前步会赢
                    return True
        self.memo[s] = False  全走完了，都没赢，就全输了
        return False