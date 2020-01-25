class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-1] -2* dp[i-1][j-1]
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i-1>=0:
                        dp[i][j] += dp[i-1][j]
                    if j-1>=0:
                        dp[i][j] += dp[i][j-1]
        # print dp
        return dp[m-1][n-1]