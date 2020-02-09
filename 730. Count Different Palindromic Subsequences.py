class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        # i = j: dp[i][j] = 2*dp[i+1][j-1] +2
            # 中间有一个重复 bcbcb
            # dp[i][j] = 2*dp[i+1][j-1] +1
            # 中间有2或以上个重复 bbcabb
            # dp[i][j] = 2*dp[i+1][j-1] -dp[c][d]
            
        # i != j: dp[i][j] = dp[i+1][j] + dp[i][j-1]-dp[i+1][j-1]
        # i<=j
        # 重复
        M = 1e9+7
        n = len(S)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
          
        for l in range(1, n+1):
            for i in range(n-l):
                j = i+l
                # print l, i, j
                if S[i] == S[j]:
                    dp[i][j] = dp[i+1][j-1] *2
                    c, d = i+1, j-1
                    #
                    while c <= d and S[i] != S[c]:
                        c += 1
                    while c <= d and S[i] != S[d]:
                        d -= 1
                    #出现2次
                    if c == d:
                        dp[i][j] += 1
                    #没有出现
                    elif c > d:
                        dp[i][j] += 2 #?
                    #出现2次以上
                    else:
                        dp[i][j] -= dp[c+1][d-1]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1]-dp[i+1][j-1]
                dp[i][j] %= M
        return int(dp[0][n-1])
        