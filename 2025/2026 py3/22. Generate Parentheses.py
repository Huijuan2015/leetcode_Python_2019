class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.findPath(n, 0, 0, "")
        return self.res


    def findPath(self, n, open, close, path):
        if len(path) == 2* n:
            self.res.append(path)
            return
        if open < n:
            self.findPath(n, open + 1, close, path+'(')
        if open > close:
            self.findPath(n, open, close+ 1, path + ')')


