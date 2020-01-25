class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp[i][j] = min(dp[i][j-1], dp[i-1][j])+grid[i][j]
        m, n = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                if not (i== 0 and j == 0):
                    dp[i][j] += grid[i][j]
        print dp
        return dp[m-1][n-1]