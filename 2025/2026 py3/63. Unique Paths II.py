class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        #如果第一行或者第一列obstacle，那右边和下边都无法达到
        # 初始化第一行第一列
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

还可以用一维数组？


递归，更直观
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[-1] * n for _ in range(m)]
        return self.helper(0, 0, m, n, obstacleGrid, memo)

    def helper(self, i, j, m, n, obstacleGrid, memo):
        if i >= m or j >= n or obstacleGrid[i][j] == 1:
            return 0
        
        if i == m-1 and j == n-1:
            return 1
        
        if memo[i][j] != -1:
            return memo[i][j]

        memo[i][j] = self.helper(i + 1, j, m, n, obstacleGrid, memo) + self.helper(i, j+1, m, n, obstacleGrid, memo)
        return memo[i][j]