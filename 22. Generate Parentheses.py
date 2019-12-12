class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.findPath(n, 0, 0, "")
        return self.res
    
    def findPath(self, n, open, close, path):
        if close > open or open > n or close > n:
            return
        if open == n and close == n:
            self.res.append(path)
            return
        self.findPath(n, open+1, close, path+'(')
        self.findPath(n, open, close+1, path+')')
        
        
recursive
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.findPath(n, 0, 0, "")
        return self.res
    
    def findPath(self, n, open, close, path):
        if len(path) == 2* n:
            self.res.append(path)
            return
        if open < n:
            self.findPath(n, open+1, close, path+"(")
        if open > close:
            self.findPath(n, open, close+1, path + ")")

//iterative
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.generate(n, "")
        return self.res
    def generate(self, n, path):
        if len(path) == 2*n:
            
            if self.valid(path):
                # print path
                self.res.append(path)
        else:
            # path.append('(')
            self.generate(n, path + '(')
            self.generate(n, path + ')')
            
    def valid(self, path):
        balance = 0
        for c in path:
            if c == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0