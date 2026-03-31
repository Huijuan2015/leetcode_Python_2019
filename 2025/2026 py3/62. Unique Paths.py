class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 设 $dp[i][j] 为到达坐标 $(i, j)$ 的路径总数
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


递归＋memo
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)] #memo（防重复计算）
        return self.helper(0, 0, m, n, memo)

    def helper(self, i, j, m, n, memo):
        if i == m-1 and j == n-1:
            return 1
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        memo[i][j] = self.helper(i + 1, j, m, n, memo) + self.helper(i, j + 1, m, n, memo)
        return memo[i][j]