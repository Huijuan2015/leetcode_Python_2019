class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


        # 数学排列组合（最优）

        # 从左上角到右下角总共要走：
        # 	•	向下：m - 1 步
        # 	•	向右：n - 1 步

        # 总共 m+n-2 步，从中选 m-1 步向下，其余是向右。
        # Python 3.8 +
        # import math
        # return math.comb(m + n - 2, m - 1)

            
