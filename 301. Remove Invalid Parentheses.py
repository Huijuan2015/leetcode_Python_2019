class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        # remove curr and see if it's valid, if valid: push to res
        # if remove cnt increase, stop
        # if close > open, stop
        # idx to end=> update all var
        # dfs: if remove current index, remove the least=> remove cnt
        self.res = []
        self.minRemove = len(s)
        self.findPath(0, 0, 0, s, 0, "")
        return set(self.res)
        
    def findPath(self, open, close, removeCnt, s, idx, path):
        if close > open or removeCnt > self.minRemove:
            return
        if idx == len(s):
            # valid
            if open == close:
                if removeCnt <= self.minRemove:
                    if removeCnt < self.minRemove:
                        self.minRemove = removeCnt
                        self.res = []
                    self.res.append(path)
            return
        if s[idx] not in ['(', ')']:
            self.findPath(open, close, removeCnt, s, idx+1, path+s[idx])   注意这个时候要return，与下面条件的关系， 不return就会继续向下跑
        else:
            # remove
            self.findPath(open, close, removeCnt+1, s, idx+1, path)
            # not remove
            if s[idx] =='(':
                self.findPath(open+1, close, removeCnt, s, idx+1, path + s[idx])
            else:
                self.findPath(open, close+1, removeCnt, s, idx+1, path + s[idx])
            
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
        