class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """

        dirs = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
        memo = {}

        def dfs(k, x, y):
            if x < 0 or y < 0 or x >= n or y >= n:
                return 0
            if k == 0:
                return 1
            if (k, x, y) in memo:
                return memo[(k, x, y)]
            prob = 0
            for dx, dy in dirs:
                prob += dfs(k-1, x+dx, y+dy) / 8.0
            memo[(k, x, y)] = prob
            return prob
        return dfs(k, row, column)