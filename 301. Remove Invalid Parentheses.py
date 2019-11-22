class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.findPath(0, 0, s, 0, "")
        return set(self.res)
        
    def findPath(self, open, close, s, i, path):
        if close > open:
            return
        if i == len(s):
            if open == close:
                if not self.res or len(path) > len(self.res[-1]):
                    self.res = []
                    self.res.append(path)
                elif len(path) == len(self.res[-1]):
                    self.res.append(path)
            return
        
        if s[i] not in ['(', ')']:
            self.findPath(open, close, s, i+1, path + s[i])
        else:
            self.findPath(open, close, s, i+1, path)
            if s[i] == '(':
                self.findPath(open+1, close, s, i+1, path +s[i])
            else:
                self.findPath(open, close+1, s, i+1, path +s[i])
        # 停：i to end
        # 走：删 open > close and i== ( / close > 
        # 不删
        