class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(n, 1, k, [])
        return self.res
    def helper(self, n, start, k, path):
        if k == 0:
            self.res.append(path)
            return
        for i in range(start, n+1):
            self.helper(n, i+1, k-1, path+[i])

