class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        # dp[i][j] 是 0~i的数字，以j为结尾的组合数量->s[i-1]
        res = 0
        n = len(S)
        M = 1e9+7
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(i+1):
                当是降序时，下一个数字不小于当前最后一个数字，反之是升序时，下一个数字小于当前最后一个数字
                if S[i-1] == 'D':
                    for k in range(j, i):
                        dp[i][j] += dp[i-1][k]      
                else:
                    for k in range(j):
                        dp[i][j] += dp[i-1][k]
                dp[i][j] %= M
        res = sum(dp[-1])%M
        return int(res)
        