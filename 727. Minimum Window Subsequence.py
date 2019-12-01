class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m, n = len(S), len(T)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        #dp[i][j] S[0:i] 与T[0:j]匹配的起始坐标
        #dp[i][0] = i, T为空串
        #dp[0][j] = -1， S为空串
        for i in range(m+1):
            dp[i][0] = i
        minLen = m+1#min 
        start = -1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
            if dp[i][n] != -1:
                if (i-dp[i][n]) < minLen:
                    # print i, n, dp[i][n]
                    minLen = i-dp[i][n]
                    start = dp[i][n]
        # print start, minLen
        if start == -1:
            return ""
        return S[start: start+minLen]