class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j] i~j需要的最小次数
        # dp[i][j] = min(dp[i][j], dp[i+1][k-1]+dp[k][j])
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1+dp[i+1][j]
                for k in range(i+1, j+1):
                    if s[k] ==s[i]:
                        dp[i][j] = min(dp[i][j], dp[i+1][k-1]+dp[k][j])
        return 0 if n == 0 else dp[0][-1]

对于字符串"abbac"，因为位置0上的a和位置3上的a相同，那么整个字符串的步数相当于"bb"和"ac"的步数之和，为3

recursive

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [[0 for _ in range(n)] for _ in range(n)]
        return self.helper(s, memo, 0, n-1)
    
    def helper(self, s, memo, i, j):
        if i > j :
            return 0
        if memo[i][j]:
            return memo[i][j]
        memo[i][j] = self.helper(s, memo, i+1, j) +1
        for k in range(i+1, j+1):
            if s[k] == s[i]:
                memo[i][j] = min(memo[i][j], self.helper(s, memo, i+1, k-1)+self.helper(s, memo, k, j))
        return memo[i][j]